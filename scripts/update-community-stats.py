#!/usr/bin/env python3
"""Update community plugin/template markdown with GitHub stars, forks, and last push.

Prefers the GitHub GraphQL API (batch) when ``GITHUB_TOKEN`` / ``GH_TOKEN`` is set.
Falls back to REST, then to public HTML counters, so local runs without a token still work.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "plugins": ROOT / "PLUGINS.md",
    "templates": ROOT / "TEMPLATES.md",
}

GRAPHQL_URL = "https://api.github.com/graphql"
REST_URL = "https://api.github.com/repos/{owner}/{repo}"
# GraphQL allows many aliased repository fields per request
BATCH_SIZE = 50

SECTION_START = {
    "plugins": re.compile(r"^## Community / 社区插件\s*$", re.M),
    "templates": re.compile(r"^## Community Templates / 社区模板\s*$", re.M),
}
SECTION_END = re.compile(r"^## ", re.M)

GITHUB_REPO_RE = re.compile(
    r"https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)"
    r"(?:/(?:tree|blob)/[^)\s]*)?"
)

# Matches prior stats suffix, including empty-repo marker
STATS_RE = re.compile(
    r"\s*·\s*★\d+\s*·\s*forks\s+\d+"
    r"(?:\s*·\s*updated\s+\d{4}-\d{2}-\d{2}|\s*·\s*empty)?\s*$"
)

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDER_REPOS = {"org/repo", "user/repo", "owner/repo"}
USER_AGENT = "awesome-emdash-community-stats/1.1"


def strip_html_comments(text: str) -> str:
    return HTML_COMMENT_RE.sub("", text)


def extract_section(text: str, kind: str) -> tuple[int, int] | None:
    start_match = SECTION_START[kind].search(text)
    if not start_match:
        return None
    start = start_match.end()
    end_match = SECTION_END.search(text, start)
    end = end_match.start() if end_match else len(text)
    return start, end


def unique_repos_in_section(section: str) -> list[str]:
    seen: set[str] = set()
    repos: list[str] = []
    for match in GITHUB_REPO_RE.finditer(strip_html_comments(section)):
        full = f"{match.group('owner')}/{match.group('repo')}"
        key = full.lower()
        if key in PLACEHOLDER_REPOS or key in seen:
            continue
        seen.add(key)
        repos.append(full)
    return repos


def auth_headers(token: str | None, *, accept: str = "application/json") -> dict[str, str]:
    headers = {
        "Accept": accept,
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def http_json(url: str, token: str | None, *, data: bytes | None = None) -> dict:
    headers = auth_headers(
        token,
        accept="application/json" if data else "application/vnd.github+json",
    )
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub HTTP {exc.code} for {url}: {err[:300]}") from exc


def graphql_request(query: str, token: str | None) -> dict:
    payload = http_json(GRAPHQL_URL, token, data=json.dumps({"query": query}).encode("utf-8"))
    if payload.get("errors"):
        messages = "; ".join(
            e.get("message", str(e)) for e in payload["errors"] if isinstance(e, dict)
        )
        if not payload.get("data"):
            raise RuntimeError(f"GitHub GraphQL errors: {messages}")
        print(f"warn: GraphQL partial errors: {messages}", file=sys.stderr)
    return payload.get("data") or {}


def build_batch_query(repos: list[str]) -> str:
    parts: list[str] = ["query {"]
    for i, full in enumerate(repos):
        owner, name = full.split("/", 1)
        owner_s = owner.replace("\\", "\\\\").replace('"', '\\"')
        name_s = name.replace("\\", "\\\\").replace('"', '\\"')
        parts.append(
            f'  r{i}: repository(owner: "{owner_s}", name: "{name_s}") {{'
            f" nameWithOwner stargazerCount forkCount isEmpty "
            f"pushedAt updatedAt createdAt }}"
        )
    parts.append("}")
    return "\n".join(parts)


def node_to_stats(full: str, node: dict) -> dict:
    empty = bool(node.get("isEmpty"))
    pushed = (node.get("pushedAt") or node.get("updatedAt") or node.get("createdAt") or "")[:10]
    return {
        "full_name": node.get("nameWithOwner") or full,
        "stars": int(node.get("stargazerCount") or 0),
        "forks": int(node.get("forkCount") or 0),
        "updated": pushed,
        "empty": empty or not pushed,
    }


def fetch_graphql(repos: list[str], token: str | None) -> dict[str, dict]:
    stats_by_repo: dict[str, dict] = {}
    for offset in range(0, len(repos), BATCH_SIZE):
        batch = repos[offset : offset + BATCH_SIZE]
        data = graphql_request(build_batch_query(batch), token)
        for i, full in enumerate(batch):
            node = data.get(f"r{i}")
            if not node:
                print(f"warn: no GraphQL data for {full}", file=sys.stderr)
                continue
            stats = node_to_stats(full, node)
            # Empty repos still return null pushedAt
            if node.get("isEmpty") or not stats["updated"]:
                stats["empty"] = True
            stats_by_repo[full.lower()] = stats
            print(
                f"  {stats['full_name']}: ★{stats['stars']} forks {stats['forks']} "
                f"{'empty' if stats.get('empty') else 'updated ' + stats['updated']}"
            )
    return stats_by_repo


def fetch_rest_one(full: str, token: str | None) -> dict | None:
    owner, repo = full.split("/", 1)
    try:
        payload = http_json(REST_URL.format(owner=owner, repo=repo), token)
    except RuntimeError as exc:
        print(f"warn: REST {full}: {exc}", file=sys.stderr)
        return None
    if payload.get("message"):
        print(f"warn: REST {full}: {payload['message']}", file=sys.stderr)
        return None
    pushed = (payload.get("pushed_at") or payload.get("updated_at") or "")[:10]
    size = int(payload.get("size") or 0)
    empty = size == 0 and not payload.get("pushed_at")
    return {
        "full_name": payload.get("full_name") or full,
        "stars": int(payload.get("stargazers_count") or 0),
        "forks": int(payload.get("forks_count") or 0),
        "updated": pushed,
        "empty": empty,
    }


def fetch_html_one(full: str) -> dict | None:
    """Public HTML counters — no API token required."""
    owner, repo = full.split("/", 1)
    url = f"https://github.com/{owner}/{repo}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        print(f"warn: HTML {full}: {exc}", file=sys.stderr)
        return None

    stars = forks = None
    m = re.search(r'id="repo-stars-counter-star"[^>]*title="([0-9,]+)"', html)
    if m:
        stars = int(m.group(1).replace(",", ""))
    else:
        m = re.search(r'aria-label="([0-9,]+) users? starred this repository"', html)
        if m:
            stars = int(m.group(1).replace(",", ""))

    m = re.search(r'id="repo-network-counter"[^>]*title="([0-9,]+)"', html)
    if m:
        forks = int(m.group(1).replace(",", ""))

    empty = "This repository is empty" in html
    updated = ""
    if not empty:
        for branch in ("main", "master"):
            atom_url = f"https://github.com/{owner}/{repo}/commits/{branch}.atom"
            try:
                areq = urllib.request.Request(
                    atom_url, headers={"User-Agent": USER_AGENT, "Accept": "application/atom+xml"}
                )
                with urllib.request.urlopen(areq, timeout=20) as resp:
                    atom = resp.read().decode("utf-8", errors="replace")
                if atom.lstrip().startswith("<?xml") or "<feed" in atom[:200]:
                    am = re.search(r"<updated>(\d{4}-\d{2}-\d{2})", atom)
                    if am:
                        updated = am.group(1)
                        break
            except Exception:  # noqa: BLE001
                continue

    if stars is None and forks is None and not empty:
        print(f"warn: HTML parse failed for {full}", file=sys.stderr)
        return None

    return {
        "full_name": full,
        "stars": stars or 0,
        "forks": forks or 0,
        "updated": updated,
        "empty": empty or not updated,
    }


def fetch_all_stats(repos: list[str], token: str | None) -> dict[str, dict]:
    stats_by_repo: dict[str, dict] = {}

    # 1) GraphQL batch when token present
    if token:
        try:
            stats_by_repo = fetch_graphql(repos, token)
        except Exception as exc:  # noqa: BLE001
            print(f"warn: GraphQL failed, falling back: {exc}", file=sys.stderr)

    missing = [r for r in repos if r.lower() not in stats_by_repo]
    if not missing:
        return stats_by_repo

    # 2) REST for remaining (works better with token; limited without)
    still: list[str] = []
    for full in missing:
        stats = fetch_rest_one(full, token)
        if stats:
            stats_by_repo[full.lower()] = stats
            print(
                f"  {stats['full_name']}: ★{stats['stars']} forks {stats['forks']} "
                f"{'empty' if stats.get('empty') else 'updated ' + stats['updated']}"
            )
            time.sleep(0.15 if token else 0.4)
        else:
            still.append(full)

    # 3) HTML scrape for anything left (no token / rate limited)
    for full in still:
        stats = fetch_html_one(full)
        if stats:
            stats_by_repo[full.lower()] = stats
            print(
                f"  {stats['full_name']}: ★{stats['stars']} forks {stats['forks']} "
                f"{'empty' if stats.get('empty') else 'updated ' + stats['updated']}"
            )
        else:
            print(f"warn: no data for {full}", file=sys.stderr)
        time.sleep(0.45)

    return stats_by_repo


def format_stats(stats: dict) -> str:
    if stats.get("empty") or not stats.get("updated"):
        return f" · ★{stats['stars']} · forks {stats['forks']} · empty"
    return f" · ★{stats['stars']} · forks {stats['forks']} · updated {stats['updated']}"


def update_list_item(line: str, stats_by_repo: dict[str, dict]) -> str:
    # Only annotate top-level list items (skip nested suite packages)
    if not line.startswith("- "):
        if line.lstrip().startswith("- ") and STATS_RE.search(line):
            return STATS_RE.sub("", line.rstrip())
        return line

    if line.lstrip().startswith("<!--"):
        return line

    match = GITHUB_REPO_RE.search(line)
    if not match:
        return line

    key = f"{match.group('owner')}/{match.group('repo')}".lower()
    if key in PLACEHOLDER_REPOS:
        return line

    stats = stats_by_repo.get(key)
    if not stats:
        return line

    base = STATS_RE.sub("", line.rstrip())
    return base + format_stats(stats)


def update_file(path: Path, kind: str, stats_by_repo: dict[str, dict]) -> bool:
    text = path.read_text(encoding="utf-8")
    bounds = extract_section(text, kind)
    if not bounds:
        print(f"warn: section not found in {path.name}", file=sys.stderr)
        return False

    start, end = bounds
    section = text[start:end]
    lines = section.splitlines(keepends=True)
    new_lines: list[str] = []
    changed = False

    for line in lines:
        if line.endswith("\n"):
            body, nl = line[:-1], "\n"
        else:
            body, nl = line, ""
        updated = update_list_item(body, stats_by_repo)
        if updated != body:
            changed = True
        new_lines.append(updated + nl)

    if not changed:
        return False

    path.write_text(text[:start] + "".join(new_lines) + text[end:], encoding="utf-8")
    return True


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print(
            "warn: GITHUB_TOKEN / GH_TOKEN not set; using REST/HTML fallbacks "
            "(slower, rate-limited).\n"
            "      export GITHUB_TOKEN=... for best results.",
            file=sys.stderr,
        )

    all_repos: list[str] = []
    for kind, path in FILES.items():
        if not path.exists():
            print(f"error: missing {path}", file=sys.stderr)
            return 1
        text = path.read_text(encoding="utf-8")
        bounds = extract_section(text, kind)
        if not bounds:
            print(f"warn: no community section in {path.name}", file=sys.stderr)
            continue
        start, end = bounds
        repos = unique_repos_in_section(text[start:end])
        print(f"{path.name}: {len(repos)} repo(s)")
        for repo in repos:
            if repo.lower() not in {r.lower() for r in all_repos}:
                all_repos.append(repo)

    if not all_repos:
        print("No community GitHub repos found.")
        return 0

    print(f"fetching {len(all_repos)} repo(s)…")
    try:
        stats_by_repo = fetch_all_stats(all_repos, token)
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1

    changed_any = False
    for kind, path in FILES.items():
        if update_file(path, kind, stats_by_repo):
            print(f"updated {path.name}")
            changed_any = True
        else:
            print(f"unchanged {path.name}")

    if not stats_by_repo:
        print("No stats fetched.", file=sys.stderr)
        return 1

    missing = len(all_repos) - len(stats_by_repo)
    if missing:
        print(f"warn: {missing} repo(s) still missing stats", file=sys.stderr)

    print(f"done ({'changes' if changed_any else 'no file changes'}; {len(stats_by_repo)}/{len(all_repos)} repos)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

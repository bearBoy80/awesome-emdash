#!/usr/bin/env python3
"""Update community plugin/template markdown with GitHub stars, forks, and last push.

Uses the GitHub GraphQL API so all repos are fetched in one (or few) request(s).
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "plugins": ROOT / "PLUGINS.md",
    "templates": ROOT / "TEMPLATES.md",
}

GRAPHQL_URL = "https://api.github.com/graphql"
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

STATS_RE = re.compile(
    r"\s*·\s*★\d+\s*·\s*forks\s+\d+\s*·\s*updated\s+\d{4}-\d{2}-\d{2}\s*$"
)

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDER_REPOS = {"org/repo", "user/repo", "owner/repo"}


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


def graphql_request(query: str, token: str | None) -> dict:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "awesome-emdash-community-stats",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    body = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(GRAPHQL_URL, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub GraphQL API {exc.code}: {err}") from exc

    if payload.get("errors"):
        # Partial data is still usable when some repos are missing
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
        # Escape GraphQL string values
        owner_s = owner.replace("\\", "\\\\").replace('"', '\\"')
        name_s = name.replace("\\", "\\\\").replace('"', '\\"')
        parts.append(
            f'  r{i}: repository(owner: "{owner_s}", name: "{name_s}") {{'
            f" nameWithOwner stargazerCount forkCount pushedAt updatedAt }}"
        )
    parts.append("}")
    return "\n".join(parts)


def fetch_all_stats(repos: list[str], token: str | None) -> dict[str, dict]:
    stats_by_repo: dict[str, dict] = {}

    for offset in range(0, len(repos), BATCH_SIZE):
        batch = repos[offset : offset + BATCH_SIZE]
        data = graphql_request(build_batch_query(batch), token)

        for i, full in enumerate(batch):
            node = data.get(f"r{i}")
            if not node:
                print(f"warn: no data for {full}", file=sys.stderr)
                continue
            pushed = (node.get("pushedAt") or node.get("updatedAt") or "")[:10]
            stats = {
                "full_name": node.get("nameWithOwner") or full,
                "stars": int(node.get("stargazerCount") or 0),
                "forks": int(node.get("forkCount") or 0),
                "updated": pushed,
            }
            stats_by_repo[full.lower()] = stats
            print(
                f"  {stats['full_name']}: ★{stats['stars']} forks {stats['forks']} "
                f"updated {stats['updated']}"
            )

    return stats_by_repo


def format_stats(stats: dict) -> str:
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
            "warn: GITHUB_TOKEN / GH_TOKEN not set; GraphQL may fail or rate-limit quickly.\n"
            "      export GITHUB_TOKEN=... or rely on Actions GITHUB_TOKEN.",
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

    print(f"fetching {len(all_repos)} repo(s) via GitHub GraphQL API…")
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

    print(f"done ({'changes' if changed_any else 'no file changes'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

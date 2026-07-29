# Awesome EmDash

> A curated list of awesome resources for [EmDash](https://github.com/emdash-cms/emdash) — the modern, secure, TypeScript-based CMS built on Astro.
>
> EmDash 精选资源列表 —— 面向 [EmDash](https://github.com/emdash-cms/emdash) 的现代、安全、基于 TypeScript 的 Astro CMS。

EmDash is a full-stack TypeScript CMS that aims to be the spiritual successor to WordPress, with sandboxed plugins, Portable Text, and strong AI integration. / EmDash 是全栈 TypeScript CMS，定位为 WordPress 的精神续作，具备沙箱插件、Portable Text 与强大的 AI 集成。

## Contents / 目录

- [Official Resources](#official-resources--官方资源)
- [Templates](#templates--模板)
- [Plugins](#plugins--插件)
- [Tools & Tooling](#tools--tooling--工具)
- [Tutorials & Guides](#tutorials--guides--教程与指南)
- [Videos](#videos--视频)
- [Examples & Demos](#examples--demos--示例与演示)
- [Migration from WordPress](#migration-from-wordpress--从-wordpress-迁移)
- [Community](#community--社区)
- [Contributing](#contributing--贡献)

## Official Resources / 官方资源

- [EmDash GitHub](https://github.com/emdash-cms/emdash) - Main repository / 主仓库
- [Documentation](https://docs.emdashcms.com/) - Official docs / 官方文档
- [npm Organization](https://www.npmjs.com/org/emdash-cms) - Official packages / 官方包
- [EmDash Website](https://emdashcms.com/) - Project homepage / 项目官网
- [Plugin Development Guide](https://docs.emdashcms.com/plugins/creating-plugins/your-first-plugin/) - Official guide to building sandboxed plugins / 官方沙箱插件开发指南
- [wp-emdash](https://github.com/emdash-cms/wp-emdash) - Official plugins to help transition from WordPress to EmDash / 官方 WordPress → EmDash 迁移辅助插件

## Templates / 模板

- [Templates List](./TEMPLATES.md) - Most complete curated template list (official + community) / 目前最完整的模板收录列表（官方 + 社区）
- [emdash-cms/templates](https://github.com/emdash-cms/templates) - Official starter templates mirror / 官方起步模板镜像

Quick start / 快速开始：

```bash
npm create emdash@latest
```

PRs welcome / 欢迎投稿 — see [TEMPLATES.md](./TEMPLATES.md) and [CONTRIBUTING.md](./CONTRIBUTING.md).

## Plugins / 插件

- [Plugins List](./PLUGINS.md) - Most complete curated plugin list (official + community) / 目前最完整的插件收录列表（官方 + 社区）
- [emdashcms.org Marketplace](https://emdashcms.org) - Unofficial community marketplace for plugins and themes / 非官方社区插件与主题市场

PRs welcome / 欢迎投稿 — see [PLUGINS.md](./PLUGINS.md) and [CONTRIBUTING.md](./CONTRIBUTING.md).

## Tools & Tooling / 工具

- [emdash-docker](https://github.com/MarianSEO/emdash-docker) - Run EmDash locally with Docker (blog stack in a few commands) / Docker 本地跑 EmDash
- [docker-emdash](https://github.com/jstgnkl/docker-emdash) - Docker image for emdash-cms / EmDash Docker 镜像
- [EmdashDeploy](https://github.com/web-casa/EmdashDeploy) - Interactive VPS installer: Docker/Podman, Caddy HTTPS, backup/restore / VPS 交互安装（Docker/Podman、Caddy、备份恢复）
- [emdash-claude-plugin](https://github.com/EngDawood/emdash-claude-plugin) - Claude Code plugin: skills and agents for Astro + Cloudflare EmDash sites / Claude Code 插件（EmDash 站点构建技能与 Agent）
- [emdash-skills](https://github.com/OziNetworkVN/emdash-skills) - Skill library and workflow guide for building EmDash with Claude / 用 Claude 构建 EmDash 的技能库与工作流
- [emdash-akari](https://github.com/bnomei/emdash-akari) - Agent-focused discovery CLI for content targets and nested JSON / 面向 Agent 的内容发现 CLI
- [emdash-template-switcher](https://github.com/pk1983/emdash-template-switcher) - Admin-switchable templates with a shadcn-style CLI / 后台可切换模板 + CLI
- [emdash-astro-sidecar](https://github.com/Ola-Turmo/emdash-astro-sidecar) - Astro sidecar utilities, themes, and plugins / Astro 侧车工具、主题与插件
- [emdash-render](https://github.com/awesomeem/emdash-render) - Direct-D1 reader + Portable Text renderer for Hono/Workers / D1 直读 + Portable Text 渲染（Hono/Workers）

PRs welcome / 欢迎投稿.

## Tutorials & Guides / 教程与指南

- [EmDash CMS by Cloudflare — the open-source TypeScript successor to WordPress](https://wppoland.com/en/emdash-cloudflare-open-source-cms-wordpress-successor-2026/) - In-depth analysis of architecture, security, and WordPress implications / 深度分析：架构、安全与对 WordPress 的影响
- [A Full-Stack TypeScript CMS Built on Astro + Cloudflare](https://github.com/emdash-cms/emdash) - Project overview on GitHub / GitHub 项目总览
- [Introducing EmDash — WordPress Plugin Security Rebuilt](https://blog.cloudflare.com/emdash-wordpress/) - Official Cloudflare announcement / 官方介绍

PRs welcome / 欢迎投稿.

## Videos / 视频

- [Cloudflare Just Killed WordPress?!](https://www.youtube.com/watch?v=sBXC63ULDAE) - Launch overview and admin walkthrough / 发布解读与后台演示
- [What Everyone Missed About EmDash](https://www.youtube.com/watch?v=hgOJH9bp75k) - Deep dive on Dynamic Workers / Dynamic Workers 深度解析
- [EmDash on Cloudflare TV](https://cloudflare.tv/this-week-in-net/emdash-the-wordpress-successor-that-fixes-plugin-security/5vpEE7aP) - Official team discussion / 官方团队访谈

PRs welcome / 欢迎投稿.

## Examples & Demos / 示例与演示

Official demo (run locally) / 官方演示（本地运行）：

```bash
git clone https://github.com/emdash-cms/emdash.git
cd emdash
pnpm install
pnpm --filter emdash-demo seed && pnpm --filter emdash-demo dev
```

Admin UI / 后台地址：`http://localhost:4321/_emdash/admin`

PRs welcome / 欢迎投稿.

## Migration from WordPress / 从 WordPress 迁移

- [wp-emdash](https://github.com/emdash-cms/wp-emdash) - Official transition helpers from WordPress to EmDash / 官方 WordPress → EmDash 过渡插件
- [Porting WordPress Themes Guide](https://docs.emdashcms.com/themes/porting-wp-themes/) - Convert PHP themes to Astro / 将主题移植为 Astro
- [Porting WordPress Plugins Guide](https://docs.emdashcms.com/migration/porting-plugins/) - Rewrite plugins in TypeScript / 将插件改写为 TypeScript
- [WordPress Import Wizard](https://docs.emdashcms.com/migration/from-wordpress/) - Built-in WXR / REST / WordPress.com import / 内置导入向导

## Community / 社区

- [GitHub Discussions](https://github.com/emdash-cms/emdash/discussions) - Main community forum / 主仓库讨论区
- [EmDash Discord](https://discord.com/invite/YY9vBaQRYt) - Chat with maintainers and community / 与维护者及社区交流
- [EmDash on X / Twitter](https://x.com/EmDashCMS) - Official account / 官方账号

## Contributing / 贡献

Contributions welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md).

欢迎贡献！请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, contributors have waived all copyright and related rights to this work.

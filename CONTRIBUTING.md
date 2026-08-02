# Contributing / 贡献指南

Thanks for contributing to **Awesome EmDash**!

感谢为 **Awesome EmDash** 贡献！

## Language / 语言

- **English is enough.** Write a clear one-line English description.
- Chinese is welcome if you can, but **not required**.
- Bilingual (`English / 中文`) is optional — do not block a PR for missing Chinese.

- **英文即可。** 写清一行英文描述。
- 会中文可补充，但**不强制**。
- 双语（`English / 中文`）可选 —— 缺中文不应成为拒稿理由。

Examples / 示例：

```md
- [plugin-name](https://github.com/org/repo) - Short English description
- [plugin-name](https://github.com/org/repo) - Short English description / 中文简述
```

## Guidelines / 准则

- Resource must be useful, maintained, and relevant to EmDash.
- Prefer official docs and high-quality community content.
- One link per line; check for duplicates before opening a PR.
- Put new items in the right file and section (see below).

- 资源需对 EmDash 有用、仍在维护、且相关。
- 优先官方文档与高质量社区内容。
- 一行一条链接；提交前检查是否重复。
- 放入正确的文件与分类（见下文）。

## Where to add / 放到哪里

| Type | File | Section |
| --- | --- | --- |
| Plugin | [PLUGINS.md](./PLUGINS.md) | Community category that fits best |
| Template / theme | [TEMPLATES.md](./TEMPLATES.md) | Community Templates |
| Guide, video, demo, etc. | [README.md](./README.md) | Matching section |

## Plugins / 插件

Add community plugins to [PLUGINS.md](./PLUGINS.md) under the best **Community** category:

| Category | Examples |
| --- | --- |
| Analytics & SEO / 分析与 SEO | Search Console, GA4, meta/OG/JSON-LD |
| Email & Forms / 邮件与表单 | Mailers, email providers, form builders |
| Commerce / 电商 | Store / checkout / inventory |
| Engagement & Social / 互动与社交 | Ratings, sharing, likes, campaigns |
| Media, Code & Galleries / 媒体与图库 | Photo galleries, code blocks, 3D |
| Content, Fields & Editor / 内容、字段与编辑器 | Field widgets, blocks, TOC, related content |
| Accessibility, Privacy & Security / 无障碍、隐私与安全 | Cookie consent, a11y, CAPTCHA, moderation |
| Internationalization / 国际化 | i18n / locales |
| Integrations & Notifications / 集成与通知 | Slack, SMS, backup, RSS |
| Learning & Verticals / 学习与垂直领域 | LMS, events, industry-specific |
| Auth & Identity / 认证与身份 | Login providers, membership auth methods |
| Plugin Suites / 插件合集 | Multi-plugin monorepos / catalogs |

If nothing fits, **add a new category** under Community (bilingual `### English / 中文` heading when possible), put the entry there, and add the category to the table above. Prefer a domain-level name that can hold more than one project. Do not force-fit into an unrelated section.

Include:

- Name + repository URL
- One-line description (English required; Chinese optional)
- Marketplace, homepage, or npm link when useful

Official / first-party plugins belong under **Official** (synced from `packages/plugins`).

## Templates / 模板与主题

Add community templates or themes to [TEMPLATES.md](./TEMPLATES.md) under **Community Templates**, in the best **category** (`###` heading):

| Category | Examples |
| --- | --- |
| Catalogs & Marketplaces / 模板目录与市场 | Theme directories, template packs, switchers |
| Blog & Content / 博客与内容 | Blog, magazine, docs starters |
| Marketing & Landing / 营销与落地页 | Marketing / landing starters |
| Portfolio & Personal / 作品集与个人站 | Portfolio, personal sites |
| Commerce & Business / 电商与商业 | Shop, services, real estate, booking |
| Vertical / Industry / 垂直行业 | Niche / industry starters (TCG, media, …) |
| Themes / 主题 | Visual themes (Bootstrap, minimal, …) |
| Deploy & Stack Starters / 部署与技术栈脚手架 | Alchemy, special deploy stacks, unusual runtimes |
| Multi-template packs / 多模板合集 | Orgs shipping many templates |

If nothing fits, **add a new category** under Community Templates (same bilingual `###` style), put the entry there, and add the category to this table. Do not force-fit into an unrelated section.

Official starters stay under **Official Templates** (Blog / Marketing / Portfolio / Starter & Blank / Reference Sites).

Include:

- Name + repository URL
- One-line description (English required; Chinese optional)
- Live demo URL or deploy target when available
- Node vs Cloudflare target when relevant

## Pull request / PR

1. Fork this repository
2. Create a branch
3. Add your entry in the correct file and category
4. Open a PR with a short note on why it belongs here

## Questions / 疑问

Open an issue or PR discussion if you are unsure where something belongs.

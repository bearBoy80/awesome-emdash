# EmDash Plugins List / 插件列表

> Curated list of EmDash plugins (official + community). / EmDash 插件精选列表（官方 + 社区）。
>
> Submit additions via PR — see [CONTRIBUTING.md](./CONTRIBUTING.md). / 通过 PR 投稿 —— 见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## Marketplace / 市场

- [emdashcms.org](https://emdashcms.org) - Unofficial community marketplace for plugins and themes (sandboxed, scanned, AI-reviewed; not affiliated with Cloudflare / EmDash) / 非官方社区插件与主题市场（沙箱 + 扫描 + AI 审核；与 Cloudflare / EmDash 官方无关）
  - [Plugins catalog](https://emdashcms.org/plugins) - Browse community plugins / 浏览社区插件
  - [Source: chrisjohnleah/emdashcms-org](https://github.com/chrisjohnleah/emdashcms-org) - Marketplace source repo / 市场源码仓库
- [Installing Plugins](https://docs.emdashcms.com/plugins/installing/) - Official install guide / 官方安装指南

## Official / First-party / 官方插件

Shipped in the [emdash monorepo `packages/plugins`](https://github.com/emdash-cms/emdash/tree/main/packages/plugins):

### Feature plugins / 功能插件

| Plugin | Package | Description / 说明 |
| --- | --- | --- |
| [ai-moderation](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/ai-moderation) | `@emdash-cms/plugin-ai-moderation` | AI-powered comment moderation via Cloudflare Workers AI (Llama Guard) / 基于 Workers AI（Llama Guard）的评论审核 |
| [atproto](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/atproto) | `@emdash-cms/plugin-atproto` | AT Protocol / standard.site syndication / AT Protocol / standard.site 联合发布 |
| [audit-log](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/audit-log) | `@emdash-cms/plugin-audit-log` | Audit logging for content changes / 内容变更审计日志 |
| [color](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/color) | `@emdash-cms/plugin-color` | Color picker field widget / 颜色选择器字段组件 |
| [embeds](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/embeds) | `@emdash-cms/plugin-embeds` | Embed blocks (YouTube, Vimeo, Twitter, Bluesky, Mastodon, and more) / 嵌入块（YouTube、Vimeo、Twitter、Bluesky、Mastodon 等） |
| [field-kit](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/field-kit) | `@emdash-cms/plugin-field-kit` | Composable field widgets for JSON fields (object forms, lists, grids, tags) / JSON 字段组合组件（对象表单、列表、网格、标签） |
| [forms](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/forms) | `@emdash-cms/plugin-forms` | Build forms, collect submissions, send notifications / 表单构建、提交收集与通知 |
| [webhook-notifier](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/webhook-notifier) | `@emdash-cms/plugin-webhook-notifier` | Post webhooks to external URLs on content changes / 内容变更时向外部 URL 发送 Webhook |

### Test / Dev plugins / 测试插件

| Plugin | Package | Description / 说明 |
| --- | --- | --- |
| [api-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/api-test) | `@emdash-cms/plugin-api-test` | Exercises all EmDash plugin APIs / 覆盖全部 EmDash 插件 API 的测试插件 |
| [marketplace-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/marketplace-test) | `@emdash-cms/plugin-marketplace-test` | End-to-end registry publishing and audit workflow testing / 注册表发布与审核流程端到端测试 |
| [sandboxed-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/sandboxed-test) | `@emdash-cms/plugin-sandboxed-test` | Test plugin for the sandboxed plugin system / 沙箱插件系统测试插件 |

## Community / 社区插件

### Analytics & SEO / 分析与 SEO

- [SerpDelta](https://github.com/SerpDelta/emdash-plugin) - Google Search Console tracking for ranking changes ([marketplace](https://emdashcms.org/plugins/serpdelta)) / Google Search Console 排名变化追踪 · ★0 · forks 0 · updated 2026-04-09
- [emdash-analytics-plugin](https://github.com/yourbright-jp/emdash-analytics-plugin) - Google Search Console + GA4 analytics with opportunity scoring / Search Console + GA4 分析与内容机会评分 · ★0 · forks 0 · updated 2026-07-23
- [em-content-insights](https://github.com/facuzarate04/em-content-insights) - Privacy-first post analytics (views, read rate, time on page, referrers) / 隐私优先的文章分析（浏览、阅读率、停留、来源） · ★3 · forks 0 · updated 2026-04-05
- [em-analytics-hub](https://github.com/facuzarate04/em-analytics-hub) - Privacy-first analytics with dashboards, funnels, goals, and campaigns / 隐私优先分析（看板、漏斗、目标与活动） · ★1 · forks 0 · updated 2026-04-18
- [emdash-plugin-analytics](https://github.com/MosierData/emdash-plugin-analytics) - GTM, GA4, Search Console, UTM attribution, and call tracking / GTM、GA4、Search Console、UTM 归因与来电追踪 · ★7 · forks 0 · updated 2026-04-10
- [emdash-plugin-seo](https://github.com/jdevalk/emdash-plugin-seo) - SEO: meta tags, Open Graph, canonical URLs, robots, JSON-LD / SEO：meta、OG、canonical、robots、JSON-LD · ★13 · forks 2 · updated 2026-06-18

### Email & Forms / 邮件与表单

- [form-mailer](https://github.com/coleprice/form-mailer) - Contact and lead-form email delivery with spam protection ([marketplace](https://emdashcms.org/plugins/form-mailer)) / 联系与线索表单邮件发送，含反垃圾保护 · ★0 · forks 0 · updated 2026-04-24
- [emdash-contact-forms](https://github.com/masonjames/emdash-contact-forms) - Production-ready contact forms / 生产可用的联系表单 · ★3 · forks 0 · updated 2026-06-11
- [emdash-plugin-lettermint](https://github.com/jdevalk/emdash-plugin-lettermint) - Lettermint email provider / Lettermint 邮件服务提供商插件 · ★3 · forks 1 · updated 2026-06-29
- [jetemail-emdash](https://github.com/jetemail/jetemail-emdash) - JetEmail email provider / JetEmail 邮件服务提供商插件 · ★1 · forks 0 · updated 2026-04-04

### Commerce / 电商

- [DashCommerce](https://github.com/emdashCommerce/dashcommerce) - WooCommerce-equivalent commerce plugin ([dashcommerce.dev](https://dashcommerce.dev)) / 对标 WooCommerce 的电商插件 · ★15 · forks 3 · updated 2026-07-09

### Engagement & Social / 互动与社交

- [emdash-rating](https://github.com/99points/emdash-rating) - Star ratings for posts and pages ([marketplace](https://emdashcms.org/plugins/emdash-rating)) / 文章与页面星级评分 · ★0 · forks 0 · updated 2026-04-09
- [emdash-social-sharing](https://github.com/masonjames/emdash-social-sharing) - Privacy-light social sharing controls / 轻量隐私友好的社交分享 · ★0 · forks 0 · updated 2026-05-12

### Media & Galleries / 媒体与图库

- [emdash-plugin-gallery-images](https://github.com/marcusbellamyshaw-cell/emdash-plugin-gallery-images) - Multi-image photo galleries with media library picker / 多图相册，支持媒体库选择器 · ★4 · forks 0 · updated 2026-07-12
- [emdash-plugin-modern-images](https://github.com/adrianoamalfi/emdash-plugin-modern-images) - WebP/AVIF conversion, responsive srcset, caching, and LCP preload / WebP/AVIF 转换、响应式 srcset、缓存与 LCP preload · ★3 · forks 0 · updated 2026-07-22

### Internationalization / 国际化

- [emdash-i18n](https://github.com/alfgago/emdash-i18n) - Internationalization with REST API, admin UI, and coverage tracking / 国际化（REST API、后台管理与覆盖率追踪） · ★0 · forks 0 · updated 2026-04-06

### Plugin Suites / 插件合集

- [PlugDash](https://github.com/plugdash/plugdash) - Community plugin catalog (`@plugdash/*` on npm) / 社区插件合集（npm `@plugdash/*`） · ★2 · forks 0 · updated 2026-04-07
  - [readtime](https://github.com/plugdash/plugdash/tree/main/packages/readtime) - Word count and reading time / 字数与阅读时间
  - [callout](https://github.com/plugdash/plugdash/tree/main/packages/callout) - Info / warning / tip / danger callout blocks / 提示块
  - [tocgen](https://github.com/plugdash/plugdash/tree/main/packages/tocgen) - Nested TOC from Portable Text headings / 从标题生成目录
  - [shortlink](https://github.com/plugdash/plugdash/tree/main/packages/shortlink) - Short URLs for posts / 文章短链
  - [sharepost](https://github.com/plugdash/plugdash/tree/main/packages/sharepost) - Social share button URLs / 社交分享链接
  - [heartpost](https://github.com/plugdash/plugdash/tree/main/packages/heartpost) - Heart / like counter / 点赞计数
  - [engage](https://github.com/plugdash/plugdash/tree/main/packages/engage) - Heart + share + copy-link combo / 互动组合组件
  - [autobuild](https://github.com/plugdash/plugdash/tree/main/packages/autobuild) - Trigger Pages / Netlify / Vercel builds on publish / 发布时触发构建钩子

PRs welcome / 欢迎投稿.

## Related / 相关资源

- [Plugin Development Guide](https://docs.emdashcms.com/plugins/creating-plugins/your-first-plugin/) - Official guide to building sandboxed plugins / 官方沙箱插件开发指南
- [Porting WordPress Plugins](https://docs.emdashcms.com/migration/porting-plugins/) - Migrate from WordPress / 从 WordPress 移植
- Back to [Awesome EmDash](./README.md)

# EmDash Plugins List / 插件列表

> Curated list of EmDash plugins (official + community). / EmDash 插件精选列表（官方 + 社区）。
>
> Submit additions via PR — see [CONTRIBUTING.md](./CONTRIBUTING.md). / 通过 PR 投稿 —— 见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## Marketplace / 市场

- [emdashcms.org](https://emdashcms.org) - Unofficial community marketplace for plugins and themes (sandboxed, scanned, AI-reviewed; not affiliated with Cloudflare / EmDash) / 非官方社区插件与主题市场（沙箱运行 + 安全扫描 + AI 审核；与 Cloudflare / EmDash 官方无关）
  - [Plugins catalog](https://emdashcms.org/plugins) - Browse community plugins / 浏览社区插件
  - [Source: chrisjohnleah/emdashcms-org](https://github.com/chrisjohnleah/emdashcms-org) - Marketplace source repo / 市场源码仓库
- [Installing Plugins](https://docs.emdashcms.com/plugins/installing/) - Official install guide / 官方安装指南

## Official / First-party / 官方插件

Shipped in the [emdash monorepo `packages/plugins`](https://github.com/emdash-cms/emdash/tree/main/packages/plugins):

### Feature plugins / 功能插件

| Plugin | Package | Description / 说明 |
| --- | --- | --- |
| [ai-moderation](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/ai-moderation) | `@emdash-cms/plugin-ai-moderation` | AI-powered comment moderation via Cloudflare Workers AI (Llama Guard) / 基于 Workers AI（Llama Guard）的评论审核 |
| [atproto](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/atproto) | `@emdash-cms/plugin-atproto` | AT Protocol / standard.site syndication / AT Protocol / standard.site 内容联合发布 |
| [audit-log](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/audit-log) | `@emdash-cms/plugin-audit-log` | Audit logging for content changes / 内容变更审计日志 |
| [color](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/color) | `@emdash-cms/plugin-color` | Color picker field widget / 颜色选择器字段组件 |
| [embeds](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/embeds) | `@emdash-cms/plugin-embeds` | Embed blocks (YouTube, Vimeo, Twitter, Bluesky, Mastodon, and more) / 嵌入块（YouTube、Vimeo、Twitter、Bluesky、Mastodon 等） |
| [field-kit](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/field-kit) | `@emdash-cms/plugin-field-kit` | Composable field widgets for JSON fields (object forms, lists, grids, tags) / 可组合的 JSON 字段组件（对象表单、列表、网格、标签） |
| [forms](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/forms) | `@emdash-cms/plugin-forms` | Build forms, collect submissions, send notifications / 表单构建、提交收集与通知 |
| [webhook-notifier](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/webhook-notifier) | `@emdash-cms/plugin-webhook-notifier` | Post webhooks to external URLs on content changes / 内容变更时向外部 URL 发送 Webhook |

### Test / Dev plugins / 测试插件

| Plugin | Package | Description / 说明 |
| --- | --- | --- |
| [api-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/api-test) | `@emdash-cms/plugin-api-test` | Exercises all EmDash plugin APIs / 覆盖全部 EmDash 插件 API 的测试插件 |
| [marketplace-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/marketplace-test) | `@emdash-cms/plugin-marketplace-test` | End-to-end registry publishing and audit workflow testing / 注册表发布与审核流程的端到端测试 |
| [sandboxed-test](https://github.com/emdash-cms/emdash/tree/main/packages/plugins/sandboxed-test) | `@emdash-cms/plugin-sandboxed-test` | Test plugin for the sandboxed plugin system / 沙箱插件系统的测试插件 |

## Community / 社区插件

### Analytics & SEO / 分析与 SEO

- [SerpDelta](https://github.com/SerpDelta/emdash-plugin) - Google Search Console tracking for ranking changes ([marketplace](https://emdashcms.org/plugins/serpdelta)) / Google Search Console 排名变化追踪 · ★0 · forks 0 · updated 2026-04-09
- [emdash-analytics-plugin](https://github.com/yourbright-jp/emdash-analytics-plugin) - Google Search Console + GA4 analytics with opportunity scoring / Search Console + GA4 分析与内容机会评分 · ★0 · forks 0 · updated 2026-08-13
- [em-content-insights](https://github.com/facuzarate04/em-content-insights) - Privacy-first post analytics (views, read rate, time on page, referrers) / 隐私优先的文章分析（浏览量、阅读率、停留时长、来源） · ★3 · forks 0 · updated 2026-04-05
- [em-analytics-hub](https://github.com/facuzarate04/em-analytics-hub) - Privacy-first analytics with dashboards, funnels, goals, and campaigns / 隐私优先分析（看板、漏斗、目标与营销活动） · ★1 · forks 0 · updated 2026-04-18
- [emdash-plugin-analytics](https://github.com/MosierData/emdash-plugin-analytics) - GTM, GA4, Search Console, UTM attribution, and call tracking / GTM、GA4、Search Console、UTM 归因与来电追踪 · ★7 · forks 0 · updated 2026-04-10
- [emdash-plugin-seo](https://github.com/jdevalk/emdash-plugin-seo) - SEO: meta tags, Open Graph, canonical URLs, robots, JSON-LD / SEO：meta、OG、canonical、robots、JSON-LD · ★14 · forks 3 · updated 2026-06-18
- [emdash-plugin-seo (DreamsEngine)](https://github.com/DreamsEngine/emdash-plugin-seo) - SEO analysis and optimization — free Yoast-style alternative with AI suggestions / SEO 分析与优化（类 Yoast，含 AI 建议） · ★4 · forks 0 · updated 2026-04-06
- [emdash-seo-core](https://github.com/masonjames/emdash-seo-core) - Subset-first SEO metadata plugin / 精简版 SEO 元数据插件 · ★1 · forks 0 · updated 2026-05-12
- [emdash-auto-meta](https://github.com/marcusbellamyshaw-cell/emdash-auto-meta) - AI-generated SEO metadata, image alt text, and taxonomy tagging / AI 生成 SEO 元数据、图片 alt 与分类标签 · ★2 · forks 0 · updated 2026-07-12
- [statistics-em](https://github.com/6arshid/statistics-em) - Real-time visit analytics with daily and historical breakdowns / 实时访问分析（按日/历史明细） · ★0 · forks 0 · updated 2026-04-23
- [emdash-plugin-analytics (artemcluster)](https://github.com/artemcluster/emdash-plugin-analytics) - Page view analytics plugin for EmDash CMS / 页面浏览量分析插件 · ★0 · forks 0 · updated 2026-04-08
- [enhancely-emdash](https://github.com/enhancely/enhancely-emdash) - JSON-LD schema plugin with AI-powered structured data / AI 驱动的 JSON-LD 结构化数据插件 · ★0 · forks 0 · updated 2026-06-21
- [pixelseo-emdash-plugin](https://github.com/codebiwan/pixelseo-emdash-plugin) - AI-generated SEO images via pixelseo.ai into the media library / 经 pixelseo.ai 生成 SEO 图片并写入媒体库 · ★0 · forks 0 · updated 2026-04-17
- [plugin-ai-discovery](https://github.com/awesomeem/plugin-ai-discovery) - llms.txt, AI manifest, and JSON-LD for AI discovery (WIP) / 面向 AI 发现：llms.txt、AI manifest、JSON-LD（开发中） · ★0 · forks 0 · updated 2026-04-14
- [emdash-human-sitemap](https://github.com/masonjames/emdash-human-sitemap) - Human-readable sitemap block and Astro component (not XML crawler sitemaps) / 面向读者的可读站点地图区块与 Astro 组件（非 XML） · ★0 · forks 0 · updated 2026-05-12
- [emdash-seo (airockstar)](https://github.com/airockstar/emdash-seo) - SEO toolkit: meta tags, OpenGraph, JSON-LD, sitemaps, and content analysis (`@ai-rockstar/emdash-seo` / `@emdash-seo/toolkit`) / SEO 工具包：meta、OG、JSON-LD、站点地图与内容分析 · ★1 · forks 0 · updated 2026-04-07

### Email & Forms / 邮件与表单

- [form-mailer](https://github.com/coleprice/form-mailer) - Contact and lead-form email delivery with spam protection ([marketplace](https://emdashcms.org/plugins/form-mailer)) / 联系与线索表单邮件发送（含反垃圾保护） · ★0 · forks 0 · updated 2026-04-24
- [emdash-contact-forms](https://github.com/masonjames/emdash-contact-forms) - Production-ready contact forms / 生产级联系表单 · ★3 · forks 0 · updated 2026-06-11
- [emdash-plugin-lettermint](https://github.com/jdevalk/emdash-plugin-lettermint) - Lettermint email provider / Lettermint 邮件服务提供商 · ★4 · forks 1 · updated 2026-06-29
- [jetemail-emdash](https://github.com/jetemail/jetemail-emdash) - JetEmail email provider / JetEmail 邮件服务提供商 · ★1 · forks 0 · updated 2026-04-04
- [emdash-forms-builder](https://github.com/hassantafreshi/emdash-forms-builder) - Forms builder plugin / 表单构建插件 · ★4 · forks 0 · updated 2026-04-22
- [emdash-freeform](https://github.com/solspace/emdash-freeform) - Freeform form-building plugin for EmDash / Freeform 表单构建插件 · ★0 · forks 0 · updated 2026-07-14
- [emdash-cloudflare-form](https://github.com/tmyuu/emdash-cloudflare-form) - Contact form backend with Turnstile + Cloudflare Email Sending / 联系表单后端（Turnstile + Cloudflare Email） · ★1 · forks 0 · updated 2026-07-03
- [emdash-contact-inbox](https://github.com/MAV3Ndev/emdash-contact-inbox) - Contact form inbox plugin / 联系表单收件箱 · ★0 · forks 0 · updated 2026-07-06
- [emdash-inbox](https://github.com/proverbiallemon/emdash-inbox) - Inbox-style mailbox UI with Cloudflare Email Service transport / 类收件箱 UI + Cloudflare 邮件传输 · ★3 · forks 0 · updated 2026-07-15
- [emdash-plugin-resend](https://github.com/maikunari/emdash-plugin-resend) - Resend email provider / Resend 邮件提供商 · ★2 · forks 1 · updated 2026-04-15
- [emdash-resend](https://github.com/bison-digital/emdash-resend) - Resend email provider plugin / Resend 邮件提供商插件 · ★1 · forks 0 · updated 2026-07-11
- [emdash-plugin-postmark](https://github.com/drudge/emdash-plugin-postmark) - Postmark email delivery / Postmark 邮件投递 · ★2 · forks 0 · updated 2026-05-01
- [emdash-plugin-cloudflare-email](https://github.com/velvee-ai/emdash-plugin-cloudflare-email) - Cloudflare Email Sending Workers binding (no API token) / Cloudflare Email Sending Workers 绑定（无需 API token） · ★5 · forks 1 · updated 2026-04-27
- [emdash-cloudflare-email](https://github.com/tmyuu/emdash-cloudflare-email) - System email via Cloudflare Email Sending / 通过 Cloudflare Email Sending 发送系统邮件 · ★3 · forks 1 · updated 2026-07-03
- [emdash-cf-email-sending](https://github.com/cfreear/emdash-cf-email-sending) - Cloudflare Email Sending plugin / Cloudflare Email Sending 插件 · ★1 · forks 0 · updated 2026-06-26
- [emdash-plugin-brevo](https://github.com/marcusbellamyshaw-cell/emdash-plugin-brevo) - Brevo transactional email delivery / Brevo 事务性邮件投递 · ★1 · forks 1 · updated 2026-07-24
- [emdash-aws-ses](https://github.com/AB6162/emdash-aws-ses) - Amazon SES SMTP email transport / Amazon SES SMTP 邮件传输 · ★1 · forks 0 · updated 2026-07-21
- [emdash-plugin-emailit](https://github.com/dennisklappe/emdash-plugin-emailit) - Transactional email through Emailit / 通过 Emailit 发送事务性邮件 · ★0 · forks 0 · updated 2026-06-23
- [emdash-email](https://github.com/Dullaz/emdash-email) - Email transport with pluggable provider abstraction / 可插拔邮件传输层抽象 · ★0 · forks 0 · updated 2026-06-23
- [emdash-smtp](https://github.com/masonjames/emdash-smtp) - SMTP plugin family / SMTP 插件系列 · ★1 · forks 1 · updated 2026-05-12
- [emdash-larksuite-email](https://github.com/MAV3Ndev/emdash-larksuite-email) - LarkSuite Mail transport / 飞书 / Lark 邮件传输 · ★0 · forks 0 · updated 2026-07-06
- [emdash-plugin-cloudflare-email (Coastweb)](https://github.com/immber/emdash-plugin-cloudflare-email) - Cloudflare Email Service transport for EmDash / Cloudflare Email Service 邮件传输 · ★0 · forks 0 · updated 2026-04-30
- [email-provider](https://github.com/aekainal/email-provider) - EmDash CMS email-provider plugin / EmDash 邮件提供商插件 · ★0 · forks 0 · updated 2026-04-25
- [emdash-plugin-email (feronera)](https://github.com/feronera/emdash-plugin-email) - Email delivery over provider HTTP APIs (Resend default; Workers-friendly) / 通过提供商 HTTP API 发信（默认 Resend，适配 Workers） · ★0 · forks 0 · updated 2026-08-03
- [emdash-postal](https://github.com/undefined-charity/emdash-postal) - Postal self-hosted email provider (HTTP API; Node + Workers sandbox) / Postal 自托管邮件提供商（HTTP API，支持 Node 与 Workers 沙箱） · ★0 · forks 0 · updated 2026-08-09

### Commerce / 电商

- [DashCommerce](https://github.com/emdashCommerce/dashcommerce) - WooCommerce-equivalent commerce plugin ([dashcommerce.dev](https://dashcommerce.dev)) / 对标 WooCommerce 的电商插件 · ★15 · forks 3 · updated 2026-07-09
- [emdash-commerce](https://github.com/Dullaz/emdash-commerce) - Products, inventory, orders, checkout, pluggable payments / 商品、库存、订单、结账与可插拔支付能力 · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-store](https://github.com/marcusbellamyshaw-cell/emdash-plugin-store) - Printful print-on-demand storefront with Stripe checkout / Printful 按需印刷店面 + Stripe 结账 · ★0 · forks 0 · updated 2026-08-12
- [Carte](https://github.com/foreztgump/carte) - Restaurant plugin family: menus, reservations, Stripe ordering / 餐厅插件系列：菜单、预订、Stripe 点餐 · ★0 · forks 0 · updated 2026-06-24
- [inventory](https://github.com/dinkuskit/inventory) - Inventory ledger: locations, movements, reservations / 库存台账：仓位、出入库流水、预留 · ★0 · forks 0 · updated 2026-08-05
- [coupons](https://github.com/dinkuskit/coupons) - Advanced promotions for AICommerce (rules, BOGO, limits) / AICommerce 高级促销（规则、买赠 BOGO、限额） · ★0 · forks 0 · updated 2026-07-23
- [bundles](https://github.com/dinkuskit/bundles) - Mix-and-match product bundles for AICommerce / AICommerce 自由组合套装 · ★1 · forks 0 · updated 2026-07-23
- [emCommerce](https://github.com/cdurth/emCommerce) - eCommerce plugin for EmDash CMS / EmDash 电商插件 · ★6 · forks 3 · updated 2026-04-02
- [emdash-restrict-with-stripe](https://github.com/strangerstudios/emdash-restrict-with-stripe) - Restrict content and sell access with Stripe (membership) / 基于 Stripe 的内容访问限制与会员付费 · ★5 · forks 1 · updated 2026-04-02
- [emdash-shop (cristianmartinez)](https://github.com/cristianmartinez/emdash-shop) - Commerce plugin: products, cart, checkout, orders, payments / 电商插件：商品、购物车、结账、订单与支付 · ★0 · forks 0 · updated 2026-04-02
- [emdash-mika](https://github.com/bnomei/emdash-mika) - Agent-ready commerce primitives for content-led storefronts (cart, wishlist, checkout handoff) ([docs](https://mika.bnomei.com/)) / 面向内容驱动店面的 agent 就绪电商原语（购物车、心愿单、结账交接）

### Engagement & Social / 互动与社交

- [emdash-rating](https://github.com/99points/emdash-rating) - Star ratings for posts and pages ([marketplace](https://emdashcms.org/plugins/emdash-rating)) / 文章与页面星级评分 · ★0 · forks 0 · updated 2026-04-09
- [emdash-social-sharing](https://github.com/masonjames/emdash-social-sharing) - Privacy-light social sharing controls / 轻量且注重隐私的社交分享 · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-social-embed](https://github.com/marcusbellamyshaw-cell/emdash-plugin-social-embed) - Paste-URL social embeds via server-side oEmbed (10 platforms) / 粘贴 URL 即可嵌入社交内容（服务端 oEmbed，10 个平台） · ★3 · forks 0 · updated 2026-08-12
- [emdash-plugin-engagement](https://github.com/marcusbellamyshaw-cell/emdash-plugin-engagement) - Publish/reply digests + comment gamification (points, badges, leaderboard) / 发布/回复摘要 + 评论游戏化（积分、徽章、排行榜） · ★1 · forks 0 · updated 2026-08-12
- [emdash-plugin-shoebox](https://github.com/marcusbellamyshaw-cell/emdash-plugin-shoebox) - Community photo/story submissions with admin review queue / 社区照片/故事投稿 + 后台审核队列 · ★1 · forks 0 · updated 2026-07-27
- [emdash-to-buffer-plugin](https://github.com/devjusty/emdash-to-buffer-plugin) - Send blog posts to Buffer / 将博客文章发送到 Buffer · ★0 · forks 0 · updated 2026-08-03
- [emdash-plugin-social-share](https://github.com/drateberry/emdash-plugin-social-share) - Auto-share content to X, Bluesky, and Mastodon / 自动分享内容到 X、Bluesky、Mastodon · ★0 · forks 0 · updated 2026-04-22
- [bible-emdash-plugin](https://github.com/midvash/bible-emdash-plugin) - Auto-link Bible references with hover tooltips (EN/PT/ES) / 自动识别圣经经文链接，悬停显示提示（英/葡/西） · ★0 · forks 0 · updated 2026-07-23
- [emdash-author-box](https://github.com/masonjames/emdash-author-box) - Production-ready author box / 生产级作者信息框 · ★0 · forks 0 · updated 2026-06-11
- [action-pages](https://github.com/adpena/action-pages) - Campaign action pages: petitions, fundraising, GOTV, signups / 竞选/活动行动页：请愿、筹款、动员投票、报名 · ★2 · forks 0 · updated 2026-04-08

### Media & Galleries / 媒体与图库

- [emdash-plugin-gallery-images](https://github.com/marcusbellamyshaw-cell/emdash-plugin-gallery-images) - Multi-image photo galleries with media library picker / 多图相册，支持媒体库选择器 · ★4 · forks 0 · updated 2026-07-24
- [emdash-plugin-modern-images](https://github.com/adrianoamalfi/emdash-plugin-modern-images) - WebP/AVIF conversion, responsive srcset, caching, and LCP preload / WebP/AVIF 转换、响应式 srcset、缓存与 LCP 预加载 · ★3 · forks 0 · updated 2026-08-12
- [emdash-plugin-media-gallery](https://github.com/gg3orgiev/emdash-plugin-media-gallery) - Media gallery plugin / 媒体图库插件 · ★1 · forks 0 · updated 2026-08-09
- [emdash-syntax-highlighter](https://github.com/masonjames/emdash-syntax-highlighter) - Portable Text syntax highlighting / Portable Text 语法高亮 · ★2 · forks 0 · updated 2026-05-12
- [emdash-plugin-highlightjs](https://github.com/adrianoamalfi/emdash-plugin-highlightjs) - Highlight.js code blocks: themes, dark/light, copy button / Highlight.js 代码块（主题、深色/浅色、一键复制） · ★1 · forks 0 · updated 2026-08-12
- [emdash-plugin-code-block-pro](https://github.com/jimiryquai/emdash-plugin-code-block-pro) - Shiki code blocks: copy, line numbers, line highlight, themes / Shiki 代码块（复制、行号、行高亮、主题） · ★0 · forks 0 · updated 2026-05-24
- [emdash-plugin-stl-viewer](https://github.com/ebootheee/emdash-plugin-stl-viewer) - Interactive 3D STL/3MF previews in Portable Text / Portable Text 中的交互式 STL/3MF 三维预览 · ★2 · forks 0 · updated 2026-05-22
- [emdash-plugin-auto-cover](https://github.com/tableau-China/emdash-plugin-auto-cover) - Auto-generate post cover images via Tencent Hunyuan AI / 基于腾讯混元 AI 自动生成文章封面 · ★0 · forks 0 · empty
- [emdash-plugin-gallery-grid (feronera)](https://github.com/feronera/emdash-plugin-gallery-grid) - Drag-and-drop thumbnail grid field widget for image-array JSON fields / 图片数组 JSON 字段的拖拽缩略图网格组件 · ★0 · forks 0 · updated 2026-08-03

### Content, Fields & Editor / 内容、字段与编辑器

- [emdash-fields](https://github.com/bnomei/emdash-fields) - Structured JSON fields: object, structure, link, choices / 结构化 JSON 字段（对象、结构体、链接、选项） · ★5 · forks 0 · updated 2026-06-29
- [emdash-blocks](https://github.com/bnomei/emdash-blocks) - JSON block-list field widget with visibility state / JSON 区块列表字段（含可见性状态） · ★2 · forks 0 · updated 2026-06-30
- [emdash-bento](https://github.com/bnomei/emdash-bento) - Bento grid field widget using nested blocks / Bento 网格字段（嵌套区块） · ★2 · forks 0 · updated 2026-06-29
- [emdash-actions](https://github.com/bnomei/emdash-actions) - Action buttons for fields and dashboards / 字段与仪表盘操作按钮 · ★2 · forks 0 · updated 2026-06-29
- [emdash-plugin-blocks](https://github.com/dennisklappe/emdash-plugin-blocks) - Key/value copy fields with hidden lookup keys / 键值文案字段（含隐藏查找键） · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-stars](https://github.com/dennisklappe/emdash-plugin-stars) - Star rating field widget for integer fields / 整型字段星级评分组件 · ★0 · forks 0 · updated 2026-06-23
- [blocks](https://github.com/dinkuskit/blocks) - Section-block library for composing whole pages in admin / 后台整页拼装用的区块组件库 · ★0 · forks 0 · updated 2026-08-07
- [emdash-table-of-contents](https://github.com/masonjames/emdash-table-of-contents) - TOC for Portable Text with Astro components / Portable Text 目录（含 Astro 组件） · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-related-content](https://github.com/markuskiller/emdash-plugin-related-content) - Dynamic related content on public detail pages / 公开详情页的动态相关内容 · ★0 · forks 0 · updated 2026-08-12
- [emdash-plugin-reading-time](https://github.com/nozo-moto/emdash-plugin-reading-time) - Reading time plugin / 阅读时长插件 · ★0 · forks 0 · updated 2026-04-08
- [spark-emdash](https://github.com/dimitrisurber/spark-emdash) - Admin UX upgrades: wider modals, multi-column fields, illustration previews / 后台体验增强（更宽弹窗、多列字段、插图预览） · ★2 · forks 0 · updated 2026-05-24
- [empixel-builder](https://github.com/tiberiugabriel/empixel-builder) - Visual page builder for EmDash and Astro (WIP) / EmDash / Astro 可视化页面构建器（开发中） · ★1 · forks 0 · updated 2026-05-25
- [EmCanvas](https://github.com/emcanvas/emcanvas) - Visual page builder for EmDash CMS / EmDash 可视化页面构建器 · ★1 · forks 0 · updated 2026-04-23
- [Galley](https://github.com/raybasedev/galley) - Runtime-authored Liquid block templates for EmDash / Astro / 支持运行时编写的 Liquid 区块模板 · ★0 · forks 0 · updated 2026-06-27
- [plugin-rotating-tagline](https://github.com/jms42/plugin-rotating-tagline) - Rotates the site tagline from a configurable list / 按配置列表轮换站点标语 · ★0 · forks 0 · updated 2026-04-27
- [emdash-page-list](https://github.com/masonjames/emdash-page-list) - Collection- and menu-backed page lists (Portable Text block + Astro component) / 基于集合与菜单的页面列表（Portable Text 区块 + Astro 组件） · ★1 · forks 0 · updated 2026-06-11
- [emdash-reading-time (MasonJames)](https://github.com/masonjames/emdash-reading-time) - Reading-time badge: Portable Text block, Astro component, and sitewide defaults / 阅读时长徽章：Portable Text 区块、Astro 组件与全站默认值 · ★0 · forks 0 · updated 2026-06-11
- [emdash-simple-history](https://github.com/masonjames/emdash-simple-history) - Lightweight content activity history (admin page + dashboard widget) / 轻量内容变更历史（后台页 + 仪表盘小组件） · ★0 · forks 0 · updated 2026-06-11
- [hello-dolly-emdash](https://github.com/hetfirma/hello-dolly-emdash) - Hello Dolly-style demo plugin: dashboard widget and settings page / Hello Dolly 风格示例插件：仪表盘小组件与设置页 · ★0 · forks 0 · updated 2026-04-02
- [emdash-plugin-tabler-icons](https://github.com/wenke-studio/emdash-plugin-tabler-icons) - Tabler Icons Portable Text block with searchable picker (native Astro SVG) / Tabler Icons Portable Text 区块（可搜索选择器，原生 Astro SVG） · ★0 · forks 0 · updated 2026-08-08
- [emdash-plugin-bulk-upload](https://github.com/afonsojramos/emdash-plugin-bulk-upload) - Admin drag-and-drop bulk upload: draft entries, optional translations, month-year widget / 后台拖拽批量上传：草稿条目、可选翻译、年月字段组件

### Accessibility, Privacy & Security / 无障碍、隐私与安全

- [emdash-plugin-cookie-consent](https://github.com/adrianoamalfi/emdash-plugin-cookie-consent) - Cookie consent banner with category opt-in and admin settings / Cookie 同意横幅（分类授权 + 后台配置） · ★2 · forks 0 · updated 2026-08-12
- [emdash-plugin-a11y](https://github.com/Full-Stack-Tech/emdash-plugin-a11y) - WCAG 2.2 AA accessibility linting and author-time scorecard / WCAG 2.2 AA 无障碍检查与编辑时评分卡 · ★1 · forks 0 · updated 2026-07-13
- [EmPrivacy](https://github.com/EmPlugins/EmPrivacy) - Privacy plugin for EmDash / EmDash 隐私插件 · ★0 · forks 0 · updated 2026-07-14
- [emdash-captcha](https://github.com/Dullaz/emdash-captcha) - CAPTCHA / bot protection with pluggable providers (Turnstile first) / 验证码 / 反机器人（可插拔提供商，优先 Turnstile） · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-ai-comment-moderation](https://github.com/jimiryquai/emdash-plugin-ai-comment-moderation) - AI comment moderation via Cloudflare Workers AI / 基于 Workers AI 的评论审核 · ★1 · forks 0 · updated 2026-05-24
- [rankshield-emdash](https://github.com/jamie888-Elite/rankshield-emdash) - RankShield security: behavioral fingerprinting, bot detection, CTR protection / RankShield 安全防护：行为指纹、机器人检测、CTR 防护 · ★0 · forks 0 · updated 2026-04-05
- [plugin-emdash-sensitive-data-leak](https://github.com/sunak-tech/plugin-emdash-sensitive-data-leak) - Blocks save when sensitive patterns (API keys, tokens, emails, etc.) are detected / 检测到敏感信息（API key、token、邮箱等）时阻止保存 · ★0 · forks 0 · updated 2026-04-22

### Internationalization / 国际化

- [emdash-i18n](https://github.com/alfgago/emdash-i18n) - Internationalization with REST API, admin UI, and coverage tracking / 国际化（REST API、后台管理与覆盖率追踪） · ★0 · forks 0 · updated 2026-04-06
- [emdash-plugin-i18n-manager-Multilingual](https://github.com/artemcluster/emdash-plugin-i18n-manager-Multilingual) - Multilingual management plugin / 多语言管理插件 · ★2 · forks 0 · updated 2026-04-20
- [Translate-em](https://github.com/6arshid/Translate-em) - Multilingual translation plugin / 多语言翻译插件 · ★0 · forks 0 · updated 2026-04-24
- [emdash-plugin-admin-ja](https://github.com/mammosu/emdash-plugin-admin-ja) - Japanese localization for EmDash admin UI / EmDash 管理后台日语化 · ★0 · forks 0 · updated 2026-04-13
- [emdash-japanese-plugin](https://github.com/Azunyan1111/emdash-japanese-plugin) - Japanese localization for EmDash admin UI (menus, labels, buttons) / EmDash 管理后台日语化（菜单、标签、按钮） · ★0 · forks 0 · updated 2026-04-03

### Integrations & Notifications / 集成与通知

- [emdash-plugin-github-backup](https://github.com/dennisklappe/emdash-plugin-github-backup) - Backup content to a GitHub repo folder on every edit / 每次编辑时备份内容到 GitHub 仓库目录 · ★1 · forks 0 · updated 2026-06-28
- [emdash-plugin-slack](https://github.com/lsngmin/emdash-plugin-slack) - Slack notifications when content is published / 内容发布时发送 Slack 通知 · ★1 · forks 0 · updated 2026-04-21
- [emdash-plugin-twilio-sms](https://github.com/Full-Stack-Tech/emdash-plugin-twilio-sms) - Twilio SMS: broadcasts, opt-out, delivery webhooks, form bridge / Twilio 短信（群发、退订、投递 Webhook、表单桥接） · ★1 · forks 0 · updated 2026-07-13
- [emdash-rss-aggregator](https://github.com/EngDawood/emdash-rss-aggregator) - RSS/Atom aggregator: import and display feeds as content / RSS/Atom 聚合：将订阅源导入并展示为内容 · ★1 · forks 0 · updated 2026-06-20
- [emdash-action-maintenance](https://github.com/bnomei/emdash-action-maintenance) - Maintenance mode for EmDash sites / EmDash 站点维护模式 · ★1 · forks 0 · updated 2026-06-27
- [plugin-troubleshooting](https://github.com/emdash-cms/plugin-troubleshooting) - First-party troubleshooting plugin (object cache and runtime issues) / 官方故障排查插件（对象缓存与运行时问题） · ★0 · forks 0 · updated 2026-07-30
- [emdash-insert-scripts](https://github.com/danielstanica/emdash-insert-scripts) - Inject custom scripts, styles, and HTML into head/body from the admin (native plugin) / 从后台向 head/body 注入脚本、样式与 HTML（原生插件） · ★0 · forks 0 · updated 2026-08-05

### Learning & Verticals / 学习与垂直领域

- [emdashlearn](https://github.com/emdash-learn/emdashlearn) - Open-source LMS: courses, progress, edge learning / 开源 LMS：课程、学习进度、边缘端学习 · ★5 · forks 0 · updated 2026-07-27
- [dateline-events-plugin](https://github.com/foreztgump/dateline-events-plugin) - Events plugin (research + implementation for EmDash) / 活动 / 事件插件 · ★0 · forks 0 · updated 2026-06-14
- [tcg-emdash-plugins](https://github.com/KURTEcl/tcg-emdash-plugins) - TCG publishing and HUB connectivity plugins / TCG 内容发布与 HUB 连接插件 · ★0 · forks 0 · updated 2026-07-19
- [emdash-plugin-paibao-operator](https://github.com/iPythoning/emdash-plugin-paibao-operator) - Embed Paibao AI Operator (GEO content) console / 嵌入拍宝 AI Operator（GEO 内容）控制台 · ★0 · forks 0 · updated 2026-07-10
- [emdash-injectai](https://github.com/muzammildafedar/emdash-injectai) - RAG support across files / 跨文件 RAG 支持 · ★1 · forks 0 · updated 2026-08-15
- [emdash-learn](https://github.com/emdash-learn/emdash-learn) - Open-source LMS plugin for EmDash CMS (courses, progress) / 开源 LMS 插件（课程与学习进度） · ★0 · forks 0 · updated 2026-08-10
- [emdash-reservations](https://github.com/Lenny606/emdash-reservations) - Reservations plugin monorepo + starter for EmDash / 预订插件 monorepo 与起步模板 · ★0 · forks 0 · updated 2026-07-19

### Auth & Identity / 认证与身份

- [emdash-auth-provider-password](https://github.com/kalaspuffar/emdash-auth-provider-password) - Email/password authentication provider for EmDash CMS / EmDash 邮箱密码登录提供商 · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-password-auth (feronera)](https://github.com/feronera/emdash-plugin-password-auth) - Full email/password admin auth: login, first-admin setup, change, and recovery / 完整邮箱密码后台认证：登录、首个管理员、改密与找回 · ★0 · forks 0 · updated 2026-08-03

### Plugin Suites / 插件合集

- [PlugDash](https://github.com/plugdash/plugdash) - Community plugin catalog (`@plugdash/*` on npm) / 社区插件目录（npm `@plugdash/*`） · ★2 · forks 0 · updated 2026-04-07
  - [readtime](https://github.com/plugdash/plugdash/tree/main/packages/readtime) - Word count and reading time / 字数统计与阅读时长
  - [callout](https://github.com/plugdash/plugdash/tree/main/packages/callout) - Info / warning / tip / danger callout blocks / 提示 / 警告 / 技巧 / 危险 callout 区块
  - [tocgen](https://github.com/plugdash/plugdash/tree/main/packages/tocgen) - Nested TOC from Portable Text headings / 根据 Portable Text 标题生成嵌套目录
  - [shortlink](https://github.com/plugdash/plugdash/tree/main/packages/shortlink) - Short URLs for posts / 文章短链接
  - [sharepost](https://github.com/plugdash/plugdash/tree/main/packages/sharepost) - Social share button URLs / 社交分享按钮链接
  - [heartpost](https://github.com/plugdash/plugdash/tree/main/packages/heartpost) - Heart / like counter / 点赞 / 爱心计数
  - [engage](https://github.com/plugdash/plugdash/tree/main/packages/engage) - Heart + share + copy-link combo / 点赞 + 分享 + 复制链接组合组件
  - [autobuild](https://github.com/plugdash/plugdash/tree/main/packages/autobuild) - Trigger Pages / Netlify / Vercel builds on publish / 发布时触发 Pages / Netlify / Vercel 构建
- [devondragon/emdash-plugins](https://github.com/devondragon/emdash-plugins) - Open-source EmDash CMS plugins by Devon Hillard / Devon Hillard 的开源 EmDash 插件集 · ★0 · forks 0 · updated 2026-07-31
- [lathekit](https://github.com/lathekit/lathekit) - Open-source EmDash plugins (AGPL-3.0) / 开源 EmDash 插件集（AGPL-3.0） · ★0 · forks 0 · updated 2026-04-20
- [timhodge/emdash-plugins](https://github.com/timhodge/emdash-plugins) - Email providers, integrations, and utilities / 邮件提供商、集成与实用工具 · ★0 · forks 0 · empty
- [piiiico/emdash-plugins](https://github.com/piiiico/emdash-plugins) - Commitment Relay and Publisher Trust Profile / Commitment Relay 与发布者信任画像 · ★0 · forks 0 · updated 2026-04-10
- [emdash-star-plugins](https://github.com/ynaoak/emdash-star-plugins) - EmDash Star suite: analytics injection, broken-link checker, Resend email, spam guard / EmDash Star 合集：分析注入、死链检查、Resend 邮件、垃圾评论防护 · ★0 · forks 0 · updated 2026-05-31
  - [analytics-injector](https://github.com/ynaoak/emdash-star-plugins/tree/main/analytics-injector) - GA4 / GTM and custom head/body code injection / GA4 / GTM 与自定义 head/body 代码注入
  - [broken-link-checker](https://github.com/ynaoak/emdash-star-plugins/tree/main/broken-link-checker) - Crawl content for broken links on a schedule / 定时巡检内容中的死链
  - [email-resend](https://github.com/ynaoak/emdash-star-plugins/tree/main/email-resend) - Resend transport for the `email:deliver` hook / Resend 邮件传输（`email:deliver`）
  - [spam-guard](https://github.com/ynaoak/emdash-star-plugins/tree/main/spam-guard) - Heuristic + LLM comment spam protection / 启发式 + LLM 评论反垃圾
- [fastcurveservices/emdash-plugins](https://github.com/fastcurveservices/emdash-plugins) - FastCurve marketplace plugins: form email, audit log, visitor tracker / FastCurve 市场插件：表单邮件、审计日志、访客追踪 · ★0 · forks 0 · updated 2026-08-09
  - [fastcurve-form-email](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-form-email) - Contact form submission emails via site email pipeline / 通过站点邮件管道发送联系表单通知
  - [fastcurve-audit-log](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-audit-log) - Audit log for content, media, comments, email, and plugin lifecycle / 内容/媒体/评论/邮件与插件生命周期审计日志
  - [fastcurve-visitor-tracker](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-visitor-tracker) - Visitor and hit tracking with admin UI / 访客与访问命中追踪（含后台）
- [emdash-notion](https://github.com/kjfsm/emdash-notion) - Notion → EmDash sync monorepo (`@emdash-notion/sync` + `@emdash-notion/blocks`) / Notion → EmDash 同步 monorepo · ★0 · forks 0 · updated 2026-08-17
  - [sync](https://github.com/kjfsm/emdash-notion/tree/main/packages/sync) - Webhook sync: Notion pages to Portable Text content / Webhook 同步：Notion 页面转 Portable Text
  - [blocks](https://github.com/kjfsm/emdash-notion/tree/main/packages/blocks) - Native Notion-style blocks (callout, toggle, to-do, etc.) / 原生 Notion 风格区块（callout、toggle、to-do 等）
- [numoteq/emdash-plugins](https://github.com/numoteq/emdash-plugins) - NUMOTEQ EmDash plugins monorepo (`@numoteq/emdash-plugin-*`) / NUMOTEQ EmDash 插件 monorepo
  - [forward-email](https://github.com/numoteq/emdash-plugins/tree/main/packages/forward-email) - Forward Email transport provider (sandbox-compatible) / Forward Email 邮件传输提供商（兼容沙箱）

PRs welcome / 欢迎投稿.

## Related / 相关资源

- [Plugin Development Guide](https://docs.emdashcms.com/plugins/creating-plugins/your-first-plugin/) - Official guide to building sandboxed plugins / 官方沙箱插件开发指南
- [Porting WordPress Plugins](https://docs.emdashcms.com/migration/porting-plugins/) - Migrate from WordPress / 从 WordPress 迁移插件
- Back to [Awesome EmDash](./README.md)

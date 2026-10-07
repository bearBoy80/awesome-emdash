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

- [SerpDelta](https://github.com/SerpDelta/emdash-plugin) - Google Search Console tracking for ranking changes ([marketplace](https://emdashcms.org/plugins/serpdelta)) / Google Search Console 排名变化追踪 · ★1 · forks 0 · updated 2026-04-09
- [emdash-analytics-plugin](https://github.com/yourbright-jp/emdash-analytics-plugin) - Google Search Console + GA4 analytics with opportunity scoring / Search Console + GA4 分析与内容机会评分 · ★1 · forks 0 · updated 2026-10-04
- [em-content-insights](https://github.com/facuzarate04/em-content-insights) - Privacy-first post analytics (views, read rate, time on page, referrers) / 隐私优先的文章分析（浏览量、阅读率、停留时长、来源） · ★3 · forks 0 · updated 2026-04-05
- [em-analytics-hub](https://github.com/facuzarate04/em-analytics-hub) - Privacy-first analytics with dashboards, funnels, goals, and campaigns / 隐私优先分析（看板、漏斗、目标与营销活动） · ★1 · forks 0 · updated 2026-04-18
- [emdash-plugin-analytics](https://github.com/MosierData/emdash-plugin-analytics) - GTM, GA4, Search Console, UTM attribution, and call tracking / GTM、GA4、Search Console、UTM 归因与来电追踪 · ★10 · forks 0 · updated 2026-04-10
- [emdash-plugin-seo](https://github.com/jdevalk/emdash-plugin-seo) - SEO: meta tags, Open Graph, canonical URLs, robots, JSON-LD / SEO：meta、OG、canonical、robots、JSON-LD · ★23 · forks 3 · updated 2026-06-18
- [emdash-plugin-seo (DreamsEngine)](https://github.com/DreamsEngine/emdash-plugin-seo) - SEO analysis and optimization — free Yoast-style alternative with AI suggestions / SEO 分析与优化（类 Yoast，含 AI 建议） · ★4 · forks 0 · updated 2026-04-06
- [emdash-seo-core](https://github.com/masonjames/emdash-seo-core) - Subset-first SEO metadata plugin / 精简版 SEO 元数据插件 · ★2 · forks 0 · updated 2026-05-12
- [emdash-auto-meta](https://github.com/marcusbellamyshaw-cell/emdash-auto-meta) - AI-generated SEO metadata, image alt text, and taxonomy tagging / AI 生成 SEO 元数据、图片 alt 与分类标签 · ★2 · forks 0 · updated 2026-10-01
- [statistics-em](https://github.com/6arshid/statistics-em) - Real-time visit analytics with daily and historical breakdowns / 实时访问分析（按日/历史明细） · ★2 · forks 0 · updated 2026-04-23
- [emdash-plugin-analytics (artemcluster)](https://github.com/artemcluster/emdash-plugin-analytics) - Page view analytics plugin for EmDash CMS / 页面浏览量分析插件 · ★0 · forks 0 · updated 2026-04-08
- [enhancely-emdash](https://github.com/enhancely/enhancely-emdash) - JSON-LD schema plugin with AI-powered structured data / AI 驱动的 JSON-LD 结构化数据插件 · ★0 · forks 0 · updated 2026-06-21
- [pixelseo-emdash-plugin](https://github.com/codebiwan/pixelseo-emdash-plugin) - AI-generated SEO images via pixelseo.ai into the media library / 经 pixelseo.ai 生成 SEO 图片并写入媒体库 · ★0 · forks 0 · updated 2026-04-17
- [plugin-ai-discovery](https://github.com/awesomeem/plugin-ai-discovery) - llms.txt, AI manifest, and JSON-LD for AI discovery (WIP) / 面向 AI 发现：llms.txt、AI manifest、JSON-LD（开发中） · ★0 · forks 0 · updated 2026-04-14
- [emdash-human-sitemap](https://github.com/masonjames/emdash-human-sitemap) - Human-readable sitemap block and Astro component (not XML crawler sitemaps) / 面向读者的可读站点地图区块与 Astro 组件（非 XML） · ★0 · forks 0 · updated 2026-05-12
- [emdash-seo (airockstar)](https://github.com/airockstar/emdash-seo) - SEO toolkit: meta tags, OpenGraph, JSON-LD, sitemaps, and content analysis (`@ai-rockstar/emdash-seo` / `@emdash-seo/toolkit`) / SEO 工具包：meta、OG、JSON-LD、站点地图与内容分析 · ★1 · forks 0 · updated 2026-04-07
- [emdash-seo (bergerie)](https://github.com/LandCruiserWorld/emdash-seo) - Route-aware SEO: sitemap, robots, llms.txt, and editorial audits (`@bergerie/emdash-seo`) / 按真实路由的 SEO：sitemap、robots、llms.txt 与编辑审核 · ★0 · forks 0 · updated 2026-08-20
- [aeo-ultimate-emdash](https://github.com/tampawebtech/aeo-ultimate-emdash) - Answer-engine SEO + Schema.org graph (`@aeoultimate/emdash-aeo`) / AEO 与 Schema.org 实体图谱 · ★0 · forks 0 · updated 2026-10-04
- [sph-emdash-plugin-sitemap-rebuild](https://github.com/merrickma/sph-emdash-plugin-sitemap-rebuild) - Dispatch sitemap rebuild jobs on post/page publish (`@sph/emdash-plugin-sitemap-rebuild`) / 发布文章/页面时投递 sitemap 重建任务 · ★0 · forks 0 · updated 2026-09-30
- [emdash-tracking-scripts](https://github.com/ShaneMuir/emdash-tracking-scripts) - Native plugin: inject GTM, GA4/gtag, Lead Forensics, or raw snippets from admin (`@tribusdigital/emdash-tracking-scripts`) / 后台注入 GTM、GA4 或自定义追踪脚本 · ★0 · forks 0 · updated 2026-09-30
- [emdash-plugin-openanalytics](https://github.com/BlackSwampAI/emdash-plugin-openanalytics) - OpenAnalytics tracker + admin overview (native `page:fragments`) / OpenAnalytics 追踪与后台概览 · ★0 · forks 0 · updated 2026-09-30
- [emdash-analytics (incsub)](https://github.com/neelg12/emdash-analytics) - Drop-in GA4 Measurement ID in admin (`@incsub/emdash-analytics`, WPMU DEV) / 后台填写 GA4 ID 即可全站追踪 · ★0 · forks 0 · updated 2026-05-26
- [emdash-plugin-indexnow](https://github.com/jesseagleboy/emdash-plugin-indexnow) - Ping IndexNow when entries are published or unpublished / 发布或下线时向 IndexNow 推送
- [emdash-seo-suite-plugin](https://github.com/nookeshkarri7/emdash-seo-suite-plugin) - SEO coaching on top of built-in SEO: keyphrase, JSON-LD, redirects, health scan / 内置 SEO 之上的分析与辅导：关键词、JSON-LD、重定向、健康扫描

### Email & Forms / 邮件与表单

- [form-mailer](https://github.com/coleprice/form-mailer) - Contact and lead-form email delivery with spam protection ([marketplace](https://emdashcms.org/plugins/form-mailer)) / 联系与线索表单邮件发送（含反垃圾保护） · ★0 · forks 0 · updated 2026-04-24
- [emdash-contact-forms](https://github.com/masonjames/emdash-contact-forms) - Production-ready contact forms / 生产级联系表单 · ★3 · forks 0 · updated 2026-06-11
- [emdash-plugin-lettermint](https://github.com/jdevalk/emdash-plugin-lettermint) - Lettermint email provider / Lettermint 邮件服务提供商 · ★5 · forks 1 · updated 2026-06-29
- [jetemail-emdash](https://github.com/jetemail/jetemail-emdash) - JetEmail email provider / JetEmail 邮件服务提供商 · ★1 · forks 0 · updated 2026-04-04
- [emdash-forms-builder](https://github.com/hassantafreshi/emdash-forms-builder) - Forms builder plugin / 表单构建插件 · ★5 · forks 0 · updated 2026-04-22
- [emdash-freeform](https://github.com/solspace/emdash-freeform) - Freeform form-building plugin for EmDash / Freeform 表单构建插件 · ★0 · forks 0 · updated 2026-07-14
- [emdash-cloudflare-form](https://github.com/tmyuu/emdash-cloudflare-form) - Contact form backend with Turnstile + Cloudflare Email Sending / 联系表单后端（Turnstile + Cloudflare Email） · ★1 · forks 0 · updated 2026-08-29
- [emdash-contact-inbox](https://github.com/MAV3Ndev/emdash-contact-inbox) - Contact form inbox plugin / 联系表单收件箱 · ★0 · forks 0 · updated 2026-07-06
- [emdash-inbox](https://github.com/proverbiallemon/emdash-inbox) - Inbox-style mailbox UI with Cloudflare Email Service transport / 类收件箱 UI + Cloudflare 邮件传输 · ★5 · forks 0 · updated 2026-09-29
- [emdash-plugin-resend](https://github.com/maikunari/emdash-plugin-resend) - Resend email provider / Resend 邮件提供商 · ★3 · forks 1 · updated 2026-04-15
- [emdash-resend](https://github.com/bison-digital/emdash-resend) - Resend email provider plugin / Resend 邮件提供商插件 · ★1 · forks 0 · updated 2026-07-11
- [emdash-plugin-postmark](https://github.com/drudge/emdash-plugin-postmark) - Postmark email delivery / Postmark 邮件投递 · ★2 · forks 0 · updated 2026-05-01
- [emdash-plugin-cloudflare-email](https://github.com/velvee-ai/emdash-plugin-cloudflare-email) - Cloudflare Email Sending Workers binding (no API token) / Cloudflare Email Sending Workers 绑定（无需 API token） · ★5 · forks 1 · updated 2026-04-27
- [emdash-cloudflare-email](https://github.com/tmyuu/emdash-cloudflare-email) - System email via Cloudflare Email Sending / 通过 Cloudflare Email Sending 发送系统邮件 · ★3 · forks 1 · updated 2026-07-03
- [emdash-cf-email-sending](https://github.com/cfreear/emdash-cf-email-sending) - Cloudflare Email Sending plugin / Cloudflare Email Sending 插件 · ★1 · forks 0 · updated 2026-06-26
- [emdash-plugin-brevo](https://github.com/marcusbellamyshaw-cell/emdash-plugin-brevo) - Brevo transactional email delivery / Brevo 事务性邮件投递 · ★1 · forks 1 · updated 2026-10-01
- [emdash-aws-ses](https://github.com/AB6162/emdash-aws-ses) - Amazon SES SMTP email transport / Amazon SES SMTP 邮件传输 · ★1 · forks 0 · updated 2026-07-21
- [emdash-plugin-emailit](https://github.com/dennisklappe/emdash-plugin-emailit) - Transactional email through Emailit / 通过 Emailit 发送事务性邮件 · ★0 · forks 0 · updated 2026-06-23
- [emdash-email](https://github.com/Dullaz/emdash-email) - Email transport with pluggable provider abstraction / 可插拔邮件传输层抽象 · ★0 · forks 0 · updated 2026-06-23
- [emdash-smtp](https://github.com/masonjames/emdash-smtp) - SMTP plugin family / SMTP 插件系列 · ★2 · forks 1 · updated 2026-09-30
- [emdash-larksuite-email](https://github.com/MAV3Ndev/emdash-larksuite-email) - LarkSuite Mail transport / 飞书 / Lark 邮件传输 · ★0 · forks 0 · updated 2026-07-06
- [emdash-plugin-cloudflare-email (Coastweb)](https://github.com/immber/emdash-plugin-cloudflare-email) - Cloudflare Email Service transport for EmDash / Cloudflare Email Service 邮件传输 · ★0 · forks 0 · updated 2026-04-30
- [email-provider](https://github.com/aekainal/email-provider) - EmDash CMS email-provider plugin / EmDash 邮件提供商插件 · ★0 · forks 0 · updated 2026-04-25
- [emdash-plugin-email (feronera)](https://github.com/feronera/emdash-plugin-email) - Email delivery over provider HTTP APIs (Resend default; Workers-friendly) / 通过提供商 HTTP API 发信（默认 Resend，适配 Workers） · ★0 · forks 0 · updated 2026-08-03
- [emdash-postal](https://github.com/undefined-charity/emdash-postal) - Postal self-hosted email provider (HTTP API; Node + Workers sandbox) / Postal 自托管邮件提供商（HTTP API，支持 Node 与 Workers 沙箱） · ★1 · forks 0 · updated 2026-09-09
- [emdash-mailing-list](https://github.com/WoofyIO/emdash-mailing-list) - Simple mailing list: double opt-in, Markdown blasts, Postal bounce webhooks / 简易邮件列表：二次确认、Markdown 群发、Postal 退信 Webhook · ★0 · forks 0 · updated 2026-10-05
- [emdash-plugin-compass-forms](https://github.com/ecropolis/emdash-plugin-compass-forms) - Editor Form block with stored submissions, email notify, and spam basics / 编辑器表单区块：存储提交、邮件通知与基础反垃圾 · ★0 · forks 0 · updated 2026-08-27
- [emdash-plugin-compass-mail](https://github.com/ecropolis/emdash-plugin-compass-mail) - Email transport via SendGrid or Resend (`email:deliver`) / 通过 SendGrid 或 Resend 发送（`email:deliver`） · ★0 · forks 0 · updated 2026-08-27
- [emdash-contact-form (incsub)](https://github.com/MJGit1974/emdash-contact-form) - Single shortcode contact form with admin submissions (`@incsub/emdash-contact-form`) / 单表单联系插件（shortcode + 后台提交） · ★0 · forks 0 · updated 2026-06-04
- [emdash-plugin-anymail](https://github.com/nexed-tech/emdash-plugin-anymail) - HTTP email:deliver via Resend, Maileroo, Mailgun, or Postmark (Workers-friendly) / HTTP 发信（Resend / Maileroo / Mailgun / Postmark，适配 Workers） · ★0 · forks 0 · updated 2026-09-07
- [emdash-forms (netdollar)](https://github.com/charl-kruger/emdash-forms) - Admin form builder + site renderer: multi-step forms, inbox, CSV, MCP (`@netdollar.dev/forms`) / 后台表单构建器 + 前台渲染（多步表单、收件箱、CSV、MCP） · ★0 · forks 0 · updated 2026-09-29
- [emdash-plugin-comment-notify](https://github.com/DavidPivert/emdash-plugin-comment-notify) - Email admins on every new comment, including the moderation queue / 新评论（含待审）邮件通知管理员 · ★0 · forks 0 · updated 2026-09-29
- [emdash-sendmail](https://github.com/wpmudev/emdash-sendmail) - sendmail transport for WPMU DEV Hosting (`@incsub/emdash-sendmail`) / 面向 WPMU DEV Hosting 的 sendmail 发信 · ★2 · forks 0 · updated 2026-06-01
- [emdash-emailit (gatilab)](https://github.com/gatilab/emdash-emailit) - Emailit transport for system and plugin mail (`@gatilab/emdash-emailit`) / Emailit 邮件传输（系统邮件与插件发信）
- [emdash-lead-capture](https://github.com/gatilab/emdash-lead-capture) - Lead-magnet block: gated download, double opt-in, admin inbox (`@gatilab/emdash-lead-capture`) / 线索磁铁区块：门禁下载、二次确认、后台收件箱

### Commerce / 电商

- [DashCommerce](https://github.com/emdashCommerce/dashcommerce) - WooCommerce-equivalent commerce plugin ([dashcommerce.dev](https://dashcommerce.dev)) / 对标 WooCommerce 的电商插件 · ★47 · forks 7 · updated 2026-10-05
- [emdash-commerce](https://github.com/Dullaz/emdash-commerce) - Products, inventory, orders, checkout, pluggable payments / 商品、库存、订单、结账与可插拔支付能力 · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-store](https://github.com/marcusbellamyshaw-cell/emdash-plugin-store) - Printful print-on-demand storefront with Stripe checkout / Printful 按需印刷店面 + Stripe 结账 · ★0 · forks 0 · updated 2026-10-01
- [Carte](https://github.com/foreztgump/carte) - Restaurant plugin family: menus, reservations, Stripe ordering / 餐厅插件系列：菜单、预订、Stripe 点餐 · ★0 · forks 0 · updated 2026-06-24
- [inventory](https://github.com/dinkuskit/inventory) - Inventory ledger: locations, movements, reservations / 库存台账：仓位、出入库流水、预留 · ★1 · forks 0 · updated 2026-10-02
- [coupons](https://github.com/dinkuskit/coupons) - Advanced promotions for AICommerce (rules, BOGO, limits) / AICommerce 高级促销（规则、买赠 BOGO、限额） · ★0 · forks 0 · updated 2026-10-01
- [bundles](https://github.com/dinkuskit/bundles) - Mix-and-match product bundles for AICommerce / AICommerce 自由组合套装 · ★1 · forks 0 · updated 2026-10-01
- [emCommerce](https://github.com/cdurth/emCommerce) - eCommerce plugin for EmDash CMS / EmDash 电商插件 · ★10 · forks 3 · updated 2026-04-02
- [emdash-restrict-with-stripe](https://github.com/strangerstudios/emdash-restrict-with-stripe) - Restrict content and sell access with Stripe (membership) / 基于 Stripe 的内容访问限制与会员付费 · ★6 · forks 1 · updated 2026-04-02
- [emdash-shop (cristianmartinez)](https://github.com/cristianmartinez/emdash-shop) - Commerce plugin: products, cart, checkout, orders, payments / 电商插件：商品、购物车、结账、订单与支付 · ★0 · forks 0 · updated 2026-04-02
- [emdash-mika](https://github.com/bnomei/emdash-mika) - Agent-ready commerce primitives for content-led storefronts (cart, wishlist, checkout handoff) ([docs](https://mika.bnomei.com/)) / 面向内容驱动店面的 agent 就绪电商原语（购物车、心愿单、结账交接） · ★2 · forks 0 · updated 2026-08-10
- [emdash-commerce-core](https://github.com/gmsas95/emdash-commerce-core) - Provider-neutral commerce core and contracts (catalog, cart, checkout, orders) / 与支付提供商解耦的电商核心与合约（目录、购物车、结账、订单） · ★0 · forks 0 · updated 2026-08-29
- [chip-for-emdash](https://github.com/gmsas95/chip-for-emdash) - CHIP hosted checkout (FPX, e-wallet, card, DuitNow QR) for EmDash / CHIP 托管结账（FPX、电子钱包、卡、DuitNow QR） · ★1 · forks 0 · updated 2026-08-29
- [dinkuskit/commerce](https://github.com/dinkuskit/commerce) - Open-source commerce layer for EmDash (`@dinkuskit/commerce`; catalog draft-item pilot) / EmDash 开源电商层（目录草稿试点） · ★0 · forks 0 · updated 2026-10-03
- [emdash-stripe](https://github.com/tmyuu/emdash-stripe) - Stripe Checkout / Payment Intents / subscriptions from CMS entries / 按内容条目收款（Checkout、Payment Intents、订阅） · ★0 · forks 0 · updated 2026-07-03
- [emdash-kaspa-x402-adapter](https://github.com/KaspaScopio/emdash-kaspa-x402-adapter) - Community Kaspa x402 payment backend (`@kaspascopio/emdash-kaspa-x402`; experimental) / Kaspa x402 支付适配（实验性） · ★0 · forks 0 · updated 2026-10-03
- [EmDash-MoneroPay](https://github.com/dwightsabeast/EmDash-MoneroPay) - Sandboxed Monero (XMR) invoices and tips via a signed wallet-host bridge (`xmr-pay`; WIP) / 沙箱门罗币收款与打赏（独立钱包桥，开发中） · ★0 · forks 0 · updated 2026-10-05
- [emdash-stripe-checkout](https://github.com/ecommerceave/emdash-stripe-checkout) - Stripe Checkout integration for EmDash CMS / Stripe Checkout 结账集成 · ★0 · forks 0 · updated 2026-10-05
- [emdash-plugin-avdeb](https://github.com/Avdebcom/emdash-plugin-avdeb) - Embed AVDEB products with your affiliate/creator referral link / 嵌入 AVDEB 商品（带推广链接） · ★1 · forks 0 · updated 2026-10-03
- [emdash-plugin-medusa](https://github.com/BlackSwampAI/emdash-plugin-medusa) - Live Medusa v2 product references in Portable Text (no catalog copy) / Portable Text 中引用 Medusa v2 商品（不拷贝目录） · ★0 · forks 0 · updated 2026-09-30
- [WSCommerce](https://github.com/wsagency/wscommerce) - TypeScript commerce platform + Cloudflare storefront (Stripe, Solo, e-računi, Woo REST profile) / TypeScript 电商平台 + Cloudflare 店面 · ★0 · forks 0 · updated 2026-09-30

### Engagement & Social / 互动与社交

- [emdash-rating](https://github.com/99points/emdash-rating) - Star ratings for posts and pages ([marketplace](https://emdashcms.org/plugins/emdash-rating)) / 文章与页面星级评分 · ★0 · forks 0 · updated 2026-04-09
- [emdash-social-sharing](https://github.com/masonjames/emdash-social-sharing) - Privacy-light social sharing controls / 轻量且注重隐私的社交分享 · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-social-embed](https://github.com/marcusbellamyshaw-cell/emdash-plugin-social-embed) - Paste-URL social embeds via server-side oEmbed (10 platforms) / 粘贴 URL 即可嵌入社交内容（服务端 oEmbed，10 个平台） · ★4 · forks 0 · updated 2026-10-01
- [emdash-plugin-engagement](https://github.com/marcusbellamyshaw-cell/emdash-plugin-engagement) - Publish/reply digests + comment gamification (points, badges, leaderboard) / 发布/回复摘要 + 评论游戏化（积分、徽章、排行榜） · ★2 · forks 0 · updated 2026-10-01
- [emdash-plugin-shoebox](https://github.com/marcusbellamyshaw-cell/emdash-plugin-shoebox) - Community photo/story submissions with admin review queue / 社区照片/故事投稿 + 后台审核队列 · ★1 · forks 0 · updated 2026-10-01
- [emdash-to-buffer-plugin](https://github.com/devjusty/emdash-to-buffer-plugin) - Send blog posts to Buffer / 将博客文章发送到 Buffer · ★0 · forks 1 · updated 2026-09-04
- [emdash-plugin-social-share](https://github.com/drateberry/emdash-plugin-social-share) - Auto-share content to X, Bluesky, and Mastodon / 自动分享内容到 X、Bluesky、Mastodon · ★0 · forks 0 · updated 2026-04-22
- [bible-emdash-plugin](https://github.com/midvash/bible-emdash-plugin) - Auto-link Bible references with hover tooltips (EN/PT/ES) / 自动识别圣经经文链接，悬停显示提示（英/葡/西） · ★0 · forks 0 · updated 2026-09-03
- [emdash-author-box](https://github.com/masonjames/emdash-author-box) - Production-ready author box / 生产级作者信息框 · ★0 · forks 0 · updated 2026-06-11
- [action-pages](https://github.com/adpena/action-pages) - Campaign action pages: petitions, fundraising, GOTV, signups / 竞选/活动行动页：请愿、筹款、动员投票、报名 · ★2 · forks 0 · updated 2026-04-08
- [indieweb-astro](https://github.com/courtneyr-dev/indieweb-astro) - IndieWeb stack for Astro/EmDash: webmentions, IndieAuth, Micropub (`@opensourcetogether/emdash-indieweb`) / Astro/EmDash 的 IndieWeb 栈：webmentions、IndieAuth、Micropub · ★0 · forks 0 · updated 2026-07-12
- [emdash-plugin-social-embeds (siygle)](https://github.com/siygle/emdash-plugin-social-embeds) - Portable Text social embeds: X, Bluesky, YouTube, and more / Portable Text 社交嵌入：X、Bluesky、YouTube 等 · ★0 · forks 0 · updated 2026-09-30
- [emdash-plugin-bluesky-comments](https://github.com/siygle/emdash-plugin-bluesky-comments) - Native comments via Giscus + Bluesky / 基于 Giscus + Bluesky 的原生评论 · ★0 · forks 0 · updated 2026-09-30
- [emdash-plugin-social-comments](https://github.com/siygle/emdash-plugin-social-comments) - Tabbed Giscus + Bluesky comments (successor of emdash-plugin-bluesky-comments) / 分页签 Giscus + Bluesky 评论（接替 bluesky-comments） · ★0 · forks 0 · updated 2026-09-30
- [emdash-to-buffer-plus](https://github.com/shanelord01/emdash-to-buffer-plus) - Share entries to Buffer with per-network fitting, delivery tracking, and an engagement dashboard / 分享到 Buffer：按网络适配、投递追踪与互动看板 · ★0 · forks 0 · updated 2026-10-03

### Media & Galleries / 媒体与图库

- [emdash-plugin-gallery-images](https://github.com/marcusbellamyshaw-cell/emdash-plugin-gallery-images) - Multi-image photo galleries with media library picker / 多图相册，支持媒体库选择器 · ★4 · forks 0 · updated 2026-07-24
- [emdash-plugin-modern-images](https://github.com/adrianoamalfi/emdash-plugin-modern-images) - WebP/AVIF conversion, responsive srcset, caching, and LCP preload / WebP/AVIF 转换、响应式 srcset、缓存与 LCP 预加载 · ★5 · forks 0 · updated 2026-08-12
- [emdash-plugin-media-gallery](https://github.com/gg3orgiev/emdash-plugin-media-gallery) - Media gallery plugin / 媒体图库插件 · ★1 · forks 0 · updated 2026-08-09
- [emdash-syntax-highlighter](https://github.com/masonjames/emdash-syntax-highlighter) - Portable Text syntax highlighting / Portable Text 语法高亮 · ★2 · forks 0 · updated 2026-05-12
- [emdash-plugin-highlightjs](https://github.com/adrianoamalfi/emdash-plugin-highlightjs) - Highlight.js code blocks: themes, dark/light, copy button / Highlight.js 代码块（主题、深色/浅色、一键复制） · ★2 · forks 0 · updated 2026-08-12
- [emdash-plugin-code-block-pro](https://github.com/jimiryquai/emdash-plugin-code-block-pro) - Shiki code blocks: copy, line numbers, line highlight, themes / Shiki 代码块（复制、行号、行高亮、主题） · ★0 · forks 0 · updated 2026-05-24
- [emdash-plugin-stl-viewer](https://github.com/ebootheee/emdash-plugin-stl-viewer) - Interactive 3D STL/3MF previews in Portable Text / Portable Text 中的交互式 STL/3MF 三维预览 · ★2 · forks 0 · updated 2026-05-22
- [emdash-plugin-auto-cover](https://github.com/tableau-China/emdash-plugin-auto-cover) - Auto-generate post cover images via Tencent Hunyuan AI / 基于腾讯混元 AI 自动生成文章封面 · ★0 · forks 0 · empty
- [emdash-plugin-gallery-grid (feronera)](https://github.com/feronera/emdash-plugin-gallery-grid) - Drag-and-drop thumbnail grid field widget for image-array JSON fields / 图片数组 JSON 字段的拖拽缩略图网格组件 · ★0 · forks 0 · updated 2026-08-03
- [emdash-plugin-neodb](https://github.com/ann61c/emdash-plugin-neodb) - NeoDB cards and a books/movies/music shelf / NeoDB 书影音卡片与 shelf · ★0 · forks 0 · updated 2026-10-01
- [emdash-blog-imgbed](https://github.com/llovely45/emdash-blog-imgbed) - Upload-only image-bed media provider (`@llovely45/emdash-blog-imgbed`) / 图床媒体库（仅上传） · ★0 · forks 0 · updated 2026-09-11
- [emdash-base64img-plugin](https://github.com/KazukiMiyazato2021/emdash-base64img-plugin) - Store images as base64 WebP data URLs in D1/SQLite (no R2) / 图片存为 base64 WebP（D1/SQLite，无需对象存储） · ★0 · forks 0 · updated 2026-09-24
- [emdash-media-unsplash](https://github.com/danielnv18/emdash-media-unsplash) - Native Unsplash media provider for the EmDash picker / Unsplash 媒体库提供商 · ★0 · forks 0 · updated 2026-09-29
- [emdash-dynamic-qr](https://github.com/nookeshkarri7/emdash-dynamic-qr) - Dynamic QR codes with style presets, live preview, and scan analytics / 动态二维码：样式预设、实时预览与扫码统计

### Content, Fields & Editor / 内容、字段与编辑器

- [emdash-fields](https://github.com/bnomei/emdash-fields) - Structured JSON fields: object, structure, link, choices / 结构化 JSON 字段（对象、结构体、链接、选项） · ★8 · forks 0 · updated 2026-06-29
- [emdash-blocks](https://github.com/bnomei/emdash-blocks) - JSON block-list field widget with visibility state / JSON 区块列表字段（含可见性状态） · ★5 · forks 0 · updated 2026-06-30
- [emdash-bento](https://github.com/bnomei/emdash-bento) - Bento grid field widget using nested blocks / Bento 网格字段（嵌套区块） · ★4 · forks 0 · updated 2026-06-29
- [emdash-actions](https://github.com/bnomei/emdash-actions) - Action buttons for fields and dashboards / 字段与仪表盘操作按钮 · ★2 · forks 0 · updated 2026-06-29
- [emdash-plugin-blocks](https://github.com/dennisklappe/emdash-plugin-blocks) - Key/value copy fields with hidden lookup keys / 键值文案字段（含隐藏查找键） · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-stars](https://github.com/dennisklappe/emdash-plugin-stars) - Star rating field widget for integer fields / 整型字段星级评分组件 · ★0 · forks 0 · updated 2026-06-23
- [blocks](https://github.com/dinkuskit/blocks) - Section-block library for composing whole pages in admin / 后台整页拼装用的区块组件库 · ★0 · forks 0 · updated 2026-09-30
- [emdash-table-of-contents](https://github.com/masonjames/emdash-table-of-contents) - TOC for Portable Text with Astro components / Portable Text 目录（含 Astro 组件） · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-related-content](https://github.com/markuskiller/emdash-plugin-related-content) - Dynamic related content on public detail pages / 公开详情页的动态相关内容 · ★0 · forks 0 · updated 2026-08-12
- [emdash-plugin-reading-time](https://github.com/nozo-moto/emdash-plugin-reading-time) - Reading time plugin / 阅读时长插件 · ★0 · forks 0 · updated 2026-04-08
- [spark-emdash](https://github.com/dimitrisurber/spark-emdash) - Admin UX upgrades: wider modals, multi-column fields, illustration previews / 后台体验增强（更宽弹窗、多列字段、插图预览） · ★2 · forks 0 · updated 2026-05-24
- [empixel-builder](https://github.com/tiberiugabriel/empixel-builder) - Visual page builder for EmDash and Astro (WIP) / EmDash / Astro 可视化页面构建器（开发中） · ★2 · forks 0 · updated 2026-05-25
- [EmCanvas](https://github.com/emcanvas/emcanvas) - Visual page builder for EmDash CMS / EmDash 可视化页面构建器 · ★1 · forks 0 · updated 2026-04-23
- [Galley](https://github.com/raybasedev/galley) - Runtime-authored Liquid block templates for EmDash / Astro / 支持运行时编写的 Liquid 区块模板 · ★0 · forks 0 · updated 2026-06-27
- [plugin-rotating-tagline](https://github.com/jms42/plugin-rotating-tagline) - Rotates the site tagline from a configurable list / 按配置列表轮换站点标语 · ★0 · forks 0 · updated 2026-04-27
- [emdash-page-list](https://github.com/masonjames/emdash-page-list) - Collection- and menu-backed page lists (Portable Text block + Astro component) / 基于集合与菜单的页面列表（Portable Text 区块 + Astro 组件） · ★1 · forks 0 · updated 2026-06-11
- [emdash-reading-time (MasonJames)](https://github.com/masonjames/emdash-reading-time) - Reading-time badge: Portable Text block, Astro component, and sitewide defaults / 阅读时长徽章：Portable Text 区块、Astro 组件与全站默认值 · ★0 · forks 0 · updated 2026-06-11
- [emdash-simple-history](https://github.com/masonjames/emdash-simple-history) - Lightweight content activity history (admin page + dashboard widget) / 轻量内容变更历史（后台页 + 仪表盘小组件） · ★1 · forks 0 · updated 2026-09-30
- [hello-dolly-emdash](https://github.com/hetfirma/hello-dolly-emdash) - Hello Dolly-style demo plugin: dashboard widget and settings page / Hello Dolly 风格示例插件：仪表盘小组件与设置页 · ★0 · forks 0 · updated 2026-04-02
- [emdash-plugin-tabler-icons](https://github.com/wenke-studio/emdash-plugin-tabler-icons) - Tabler Icons Portable Text block with searchable picker (native Astro SVG) / Tabler Icons Portable Text 区块（可搜索选择器，原生 Astro SVG） · ★0 · forks 0 · updated 2026-08-08
- [emdash-plugin-bulk-upload](https://github.com/afonsojramos/emdash-plugin-bulk-upload) - Admin drag-and-drop bulk upload: draft entries, optional translations, month-year widget / 后台拖拽批量上传：草稿条目、可选翻译、年月字段组件 · ★0 · forks 0 · updated 2026-10-04
- [emdash-plugin-puck](https://github.com/markoinla/emdash-plugin-puck) - Puck visual editor as a json field widget with public rendering / Puck 可视化编辑器（json 字段组件 + 前台渲染） · ★1 · forks 0 · updated 2026-09-05
- [emdash-plugin-katex](https://github.com/ibnutoriq/emdash-plugin-katex) - Server-rendered KaTeX math blocks for Portable Text / Portable Text 服务端 KaTeX 公式块 · ★1 · forks 0 · updated 2026-09-27
- [emdash-page-builder](https://github.com/undefined-charity/emdash-page-builder) - On-page word-processor editing in the live site's own styles / 前台所见即所得：按站点样式就地编辑 · ★0 · forks 0 · updated 2026-10-01
- [origin-emdash-tabs](https://github.com/stephanedemotte/origin-emdash-tabs) - Native editor tabs: group a collection's fields (nothing stored) / 后台编辑器字段分页签（不落库） · ★0 · forks 0 · updated 2026-09-29
- [origin-emdash-cards](https://github.com/stephanedemotte/origin-emdash-cards) - Craft-style repeater cards with slide-out editing / Craft 风格卡片式 repeater（侧滑编辑） · ★0 · forks 0 · updated 2026-09-29
- [origin-emdash-uniq](https://github.com/stephanedemotte/origin-emdash-uniq) - Singleton collections: one entry per locale for Home/About-style pages / 单例集合：每个语言一条（首页/关于页） · ★0 · forks 0 · updated 2026-09-28
- [emdash-cms-sheet-to-table](https://github.com/alamriku/emdash-cms-sheet-to-table) - Live searchable/sortable tables from Google Sheets (`emdash-plugin-sheet-table`) / 把 Google 表格变成可搜索可排序表格 · ★0 · forks 0 · updated 2026-10-05
- [emdash-document-revisions](https://github.com/benbalter/emdash-document-revisions) - Versioned private files in R2 with permission-checked permalinks (WP Document Revisions port) / R2 私有文档版本管理（WP Document Revisions 移植） · ★0 · forks 0 · updated 2026-10-05
- [emdash-content-blocks](https://github.com/gatilab/emdash-content-blocks) - Editorial Portable Text blocks: FAQ, callout, review, comparison (`@gatilab/emdash-content-blocks`) / 编辑向 Portable Text 区块：FAQ、callout、评测、对比
- [emdash-dynamic-dates](https://github.com/gatilab/emdash-dynamic-dates) - Render-time date shortcodes (`[year]`, `[age]`, countdowns) (`@gatilab/emdash-dynamic-dates`) / 渲染时日期短代码（年份、年龄、倒计时）
- [emdash-plugin-custom-404](https://github.com/azydeco/emdash-plugin-404) - Editors configure the public 404 page from admin (`@azydeco/emdash-plugin-custom-404`) / 后台配置站点 404 页面
- [EmVB](https://github.com/PerkyZZ999/EmVB) - Visual page builder for EmDash admin (`@perkyzz/emvb`) / EmDash 可视化页面构建器

### Accessibility, Privacy & Security / 无障碍、隐私与安全

- [emdash-plugin-cookie-consent](https://github.com/adrianoamalfi/emdash-plugin-cookie-consent) - Cookie consent banner with category opt-in and admin settings / Cookie 同意横幅（分类授权 + 后台配置） · ★4 · forks 0 · updated 2026-08-12
- [emdash-plugin-a11y](https://github.com/Full-Stack-Tech/emdash-plugin-a11y) - WCAG 2.2 AA accessibility linting and author-time scorecard / WCAG 2.2 AA 无障碍检查与编辑时评分卡 · ★1 · forks 0 · updated 2026-07-13
- [EmPrivacy](https://github.com/EmPlugins/EmPrivacy) - Privacy plugin for EmDash / EmDash 隐私插件 · ★0 · forks 0 · updated 2026-09-29
- [emdash-captcha](https://github.com/Dullaz/emdash-captcha) - CAPTCHA / bot protection with pluggable providers (Turnstile first) / 验证码 / 反机器人（可插拔提供商，优先 Turnstile） · ★0 · forks 0 · updated 2026-06-23
- [emdash-plugin-ai-comment-moderation](https://github.com/jimiryquai/emdash-plugin-ai-comment-moderation) - AI comment moderation via Cloudflare Workers AI / 基于 Workers AI 的评论审核 · ★1 · forks 0 · updated 2026-05-24
- [rankshield-emdash](https://github.com/jamie888-Elite/rankshield-emdash) - RankShield security: behavioral fingerprinting, bot detection, CTR protection / RankShield 安全防护：行为指纹、机器人检测、CTR 防护 · ★0 · forks 0 · updated 2026-04-05
- [plugin-emdash-sensitive-data-leak](https://github.com/sunak-tech/plugin-emdash-sensitive-data-leak) - Blocks save when sensitive patterns (API keys, tokens, emails, etc.) are detected / 检测到敏感信息（API key、token、邮箱等）时阻止保存 · ★0 · forks 0 · updated 2026-09-22
- [emdash-preflight](https://github.com/jammaru/emdash-preflight) - Deterministic publish gate: observe or block before content goes live (`@jammaru.com/preflight`) / 发布前门禁：观察或拦截（确定性规则，无 AI） · ★2 · forks 0 · updated 2026-09-30
- [ChangeWard](https://github.com/mirza-rizvi/ChangeWard) - Log content changes, watch protected pages, and block risky publishes (including MCP) / 记录内容变更、监控受保护页面、拦截高风险发布 · ★0 · forks 0 · updated 2026-09-30
- [emdash-plugin-ai-alt-text](https://github.com/DavidPivert/emdash-plugin-ai-alt-text) - Claude-written image alt text in each entry's language (WCAG 1.1.1) / 按条目语言用 Claude 生成图片 alt · ★0 · forks 0 · updated 2026-09-30

### Internationalization / 国际化

- [emdash-i18n](https://github.com/alfgago/emdash-i18n) - Internationalization with REST API, admin UI, and coverage tracking / 国际化（REST API、后台管理与覆盖率追踪） · ★0 · forks 0 · updated 2026-04-06
- [emdash-plugin-i18n-manager-Multilingual](https://github.com/artemcluster/emdash-plugin-i18n-manager-Multilingual) - Multilingual management plugin / 多语言管理插件 · ★2 · forks 0 · updated 2026-04-20
- [Translate-em](https://github.com/6arshid/Translate-em) - Multilingual translation plugin / 多语言翻译插件 · ★0 · forks 0 · updated 2026-04-24
- [emdash-plugin-admin-ja](https://github.com/mammosu/emdash-plugin-admin-ja) - Japanese localization for EmDash admin UI / EmDash 管理后台日语化 · ★0 · forks 0 · updated 2026-04-13
- [emdash-japanese-plugin](https://github.com/Azunyan1111/emdash-japanese-plugin) - Japanese localization for EmDash admin UI (menus, labels, buttons) / EmDash 管理后台日语化（菜单、标签、按钮） · ★0 · forks 0 · updated 2026-04-03
- [LinguaDash](https://github.com/swissky/emdash-plugin-linguadash) - Translation coverage, review, and MT drafts (DeepL / Google / Azure / OpenAI / Workers AI) / 翻译覆盖、审校与机器翻译草稿 · ★0 · forks 1 · updated 2026-10-02
- [spark-emdash-multilingual](https://github.com/dimitrisurber/spark-emdash-multilingual) - Companion to spark-emdash: locale switch, translation status, side-by-side editing / spark-emdash 配套：语言切换、翻译状态、对照编辑 · ★0 · forks 0 · updated 2026-05-24
- [EmDash-PT-BR](https://github.com/GabrielChaves-Dev/EmDash-PT-BR) - Brazilian Portuguese translation overlay for the EmDash admin UI / EmDash 后台界面葡语（巴西）翻译 · ★0 · forks 0 · updated 2026-04-12

### Integrations & Notifications / 集成与通知

- [emdash-plugin-github-backup](https://github.com/dennisklappe/emdash-plugin-github-backup) - Backup content to a GitHub repo folder on every edit / 每次编辑时备份内容到 GitHub 仓库目录 · ★1 · forks 0 · updated 2026-06-28
- [emdash-plugin-slack](https://github.com/lsngmin/emdash-plugin-slack) - Slack notifications when content is published / 内容发布时发送 Slack 通知 · ★1 · forks 0 · updated 2026-04-21
- [emdash-plugin-twilio-sms](https://github.com/Full-Stack-Tech/emdash-plugin-twilio-sms) - Twilio SMS: broadcasts, opt-out, delivery webhooks, form bridge / Twilio 短信（群发、退订、投递 Webhook、表单桥接） · ★1 · forks 0 · updated 2026-07-13
- [emdash-rss-aggregator](https://github.com/EngDawood/emdash-rss-aggregator) - RSS/Atom aggregator: import and display feeds as content / RSS/Atom 聚合：将订阅源导入并展示为内容 · ★2 · forks 0 · updated 2026-06-20
- [emdash-action-maintenance](https://github.com/bnomei/emdash-action-maintenance) - Maintenance mode for EmDash sites / EmDash 站点维护模式 · ★1 · forks 0 · updated 2026-06-27
- [plugin-troubleshooting](https://github.com/emdash-cms/plugin-troubleshooting) - First-party troubleshooting plugin (object cache and runtime issues) / 官方故障排查插件（对象缓存与运行时问题） · ★0 · forks 0 · updated 2026-07-30
- [emdash-insert-scripts](https://github.com/danielstanica/emdash-insert-scripts) - Inject custom scripts, styles, and HTML into head/body from the admin (native plugin) / 从后台向 head/body 注入脚本、样式与 HTML（原生插件） · ★0 · forks 0 · updated 2026-08-05
- [relink](https://github.com/giffeler/relink) - External link inventory, link checks, and verified Wayback archives (`emdash-plugin-relink`) / 外链盘点、存活检测与 Wayback 归档 · ★1 · forks 0 · updated 2026-10-05
- [EmDash-Github-Content](https://github.com/tas0dev/EmDash-Github-Content) - Import GitHub Markdown into EmDash Portable Text / 从 GitHub Markdown 导入 Portable Text · ★0 · forks 0 · updated 2026-09-25
- [tidysites-platform](https://github.com/4sons/tidysites-platform) - Tidysites `/_tidy/*` routes and publish hooks (`@tideworthy/tidysites-platform`) / Tidysites 平台路由与发布钩子 · ★1 · forks 0 · updated 2026-10-04
- [emdash-discord-notifier](https://github.com/raghuchinnannan/emdash-discord-notifier) - Discord webhooks for publishes, comments, media, and forms ([a2plugins.com](https://a2plugins.com/discord-notifier/)) / Discord 通知：发布、评论、媒体与表单 · ★0 · forks 0 · updated 2026-09-29
- [emdash-plugin-content-link-check](https://github.com/eisbachcode/emdash-plugin-content-link-check) - Scheduled link audit: broken links, dead domains, redirects / 定时链接巡检：死链、失效域名、重定向 · ★0 · forks 0 · updated 2026-09-29
- [emdash-plugin-content-freshness](https://github.com/eisbachcode/emdash-plugin-content-freshness) - Scheduled freshness audit: stale entries, weak SEO, missed schedules / 定时内容保鲜审核：过期条目、弱 SEO、错过的定时发布 · ★0 · forks 0 · updated 2026-09-29
- [Coywolf Pack](https://github.com/coywolf-llc/coywolf-pack) - Cloudflare pack: backups/restore, extra redirects, TOC, downloads, IndexNow (`@coywolf/emdash`) / Cloudflare 功能包：备份恢复、扩展重定向、目录、下载、IndexNow · ★2 · forks 1 · updated 2026-10-05
- [emdash-maintenance-mode](https://github.com/bempensato/emdash-maintenance-mode) - Maintenance / coming-soon page with editor bypass and secret guest links / 维护/即将上线页（编辑可绕过、访客密钥链接）
- [emdash-header-footer-code](https://github.com/jithinsk/emdash-header-footer-code) - Inject analytics, verification tags, chat widgets, CSS/JS into head or body / 向 head/body 注入分析、验证标签、聊天组件与 CSS/JS

### Learning & Verticals / 学习与垂直领域

- [emdashlearn](https://github.com/emdash-learn/emdashlearn) - Open-source LMS: courses, progress, edge learning / 开源 LMS：课程、学习进度、边缘端学习 · ★6 · forks 0 · updated 2026-07-27
- [dateline-events-plugin](https://github.com/foreztgump/dateline-events-plugin) - Events plugin (research + implementation for EmDash) / 活动 / 事件插件 · ★1 · forks 0 · updated 2026-06-14
- [tcg-emdash-plugins](https://github.com/KURTEcl/tcg-emdash-plugins) - TCG publishing and HUB connectivity plugins / TCG 内容发布与 HUB 连接插件 · ★0 · forks 0 · updated 2026-09-30
- [emdash-plugin-paibao-operator](https://github.com/iPythoning/emdash-plugin-paibao-operator) - Embed Paibao AI Operator (GEO content) console / 嵌入拍宝 AI Operator（GEO 内容）控制台 · ★0 · forks 0 · updated 2026-08-20
- [emdash-injectai](https://github.com/muzammildafedar/emdash-injectai) - RAG support across files / 跨文件 RAG 支持 · ★1 · forks 0 · updated 2026-08-15
- [emdash-learn](https://github.com/emdash-learn/emdash-learn) - Open-source LMS plugin for EmDash CMS (courses, progress) / 开源 LMS 插件（课程与学习进度） · ★0 · forks 0 · updated 2026-10-05
- [emdash-reservations](https://github.com/Lenny606/emdash-reservations) - Reservations plugin monorepo + starter for EmDash / 预订插件 monorepo 与起步模板 · ★0 · forks 0 · updated 2026-07-19
- [eventual](https://github.com/Vermeulen-Solutions/eventual-emdash-sandbox) - Sandboxed events plugin: venues, recurrence, JSON/iCalendar feeds / 沙箱活动插件：场地、重复日程、JSON/iCal 订阅 · ★2 · forks 0 · updated 2026-10-05
- [emdash-lms](https://github.com/tohaitrieu/emdash-lms) - LMS: courses, memberships, quizzes, certificates (`emdash-lms` on npm) / LMS：课程、会员、测验、证书 · ★5 · forks 0 · updated 2026-04-06

### Auth & Identity / 认证与身份

- [emdash-auth-provider-password](https://github.com/kalaspuffar/emdash-auth-provider-password) - Email/password authentication provider for EmDash CMS / EmDash 邮箱密码登录提供商 · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-password-auth (feronera)](https://github.com/feronera/emdash-plugin-password-auth) - Full email/password admin auth: login, first-admin setup, change, and recovery / 完整邮箱密码后台认证：登录、首个管理员、改密与找回 · ★0 · forks 0 · updated 2026-08-03
- [emdash-better-auth](https://github.com/theweekendprojects/emdash-better-auth) - Email/password + Google/GitHub auth via Better Auth / Better Auth 邮箱密码与社交登录 · ★5 · forks 0 · updated 2026-10-05
- [@hellocoop/emdash](https://github.com/hellocoop/emdash) - Hellō login + OpenID Provider Commands for account lifecycle / Hellō 登录与账号生命周期（OIDC Provider Commands） · ★0 · forks 0 · updated 2026-09-07

### Admin UI / 后台界面

- [emdash-admin-theme-classic](https://github.com/marks-zyz/emdash-admin-theme-classic) - wp-admin look for the EmDash admin panel (CSS tokens, no core patch) / 后台 wp-admin 风格主题（纯 CSS，不改核心） · ★0 · forks 0 · updated 2026-10-04

### Search / 搜索

- [emdash-ai-search](https://github.com/theweekendprojects/emdash-ai-search) - Drop-in AI search + chat via Cloudflare AI Search / Cloudflare AI Search 搜索与对话 · ★0 · forks 0 · updated 2026-10-01
- [emdash-rag](https://github.com/theweekendprojects/emdash-rag) - Semantic search + RAG chat (Workers AI / Vectorize or sandboxed REST) / 语义搜索与 RAG 对话 · ★0 · forks 0 · updated 2026-09-17

### Plugin Suites / 插件合集

- [PlugDash](https://github.com/plugdash/plugdash) - Community plugin catalog (`@plugdash/*` on npm) / 社区插件目录（npm `@plugdash/*`） · ★2 · forks 0 · updated 2026-10-02
  - [readtime](https://github.com/plugdash/plugdash/tree/main/packages/readtime) - Word count and reading time / 字数统计与阅读时长
  - [callout](https://github.com/plugdash/plugdash/tree/main/packages/callout) - Info / warning / tip / danger callout blocks / 提示 / 警告 / 技巧 / 危险 callout 区块
  - [tocgen](https://github.com/plugdash/plugdash/tree/main/packages/tocgen) - Nested TOC from Portable Text headings / 根据 Portable Text 标题生成嵌套目录
  - [shortlink](https://github.com/plugdash/plugdash/tree/main/packages/shortlink) - Short URLs for posts / 文章短链接
  - [sharepost](https://github.com/plugdash/plugdash/tree/main/packages/sharepost) - Social share button URLs / 社交分享按钮链接
  - [heartpost](https://github.com/plugdash/plugdash/tree/main/packages/heartpost) - Heart / like counter / 点赞 / 爱心计数
  - [engage](https://github.com/plugdash/plugdash/tree/main/packages/engage) - Heart + share + copy-link combo / 点赞 + 分享 + 复制链接组合组件
  - [autobuild](https://github.com/plugdash/plugdash/tree/main/packages/autobuild) - Trigger Pages / Netlify / Vercel builds on publish / 发布时触发 Pages / Netlify / Vercel 构建
- [devondragon/emdash-plugins](https://github.com/devondragon/emdash-plugins) - Open-source EmDash CMS plugins by Devon Hillard / Devon Hillard 的开源 EmDash 插件集 · ★0 · forks 0 · updated 2026-09-18
- [lathekit](https://github.com/lathekit/lathekit) - Open-source EmDash plugins (AGPL-3.0) / 开源 EmDash 插件集（AGPL-3.0） · ★0 · forks 0 · updated 2026-04-20
- [timhodge/emdash-plugins](https://github.com/timhodge/emdash-plugins) - Email providers, integrations, and utilities / 邮件提供商、集成与实用工具 · ★0 · forks 0 · empty
- [piiiico/emdash-plugins](https://github.com/piiiico/emdash-plugins) - Commitment Relay and Publisher Trust Profile / Commitment Relay 与发布者信任画像 · ★0 · forks 0 · updated 2026-04-10
- [emdash-star-plugins](https://github.com/ynaoak/emdash-star-plugins) - EmDash Star suite: analytics injection, broken-link checker, Resend email, spam guard / EmDash Star 合集：分析注入、死链检查、Resend 邮件、垃圾评论防护 · ★0 · forks 0 · updated 2026-05-31
  - [analytics-injector](https://github.com/ynaoak/emdash-star-plugins/tree/main/analytics-injector) - GA4 / GTM and custom head/body code injection / GA4 / GTM 与自定义 head/body 代码注入
  - [broken-link-checker](https://github.com/ynaoak/emdash-star-plugins/tree/main/broken-link-checker) - Crawl content for broken links on a schedule / 定时巡检内容中的死链
  - [email-resend](https://github.com/ynaoak/emdash-star-plugins/tree/main/email-resend) - Resend transport for the `email:deliver` hook / Resend 邮件传输（`email:deliver`）
  - [spam-guard](https://github.com/ynaoak/emdash-star-plugins/tree/main/spam-guard) - Heuristic + LLM comment spam protection / 启发式 + LLM 评论反垃圾
- [fastcurveservices/emdash-plugins](https://github.com/fastcurveservices/emdash-plugins) - FastCurve marketplace plugins: form email, audit log, visitor tracker / FastCurve 市场插件：表单邮件、审计日志、访客追踪 · ★1 · forks 0 · updated 2026-08-09
  - [fastcurve-form-email](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-form-email) - Contact form submission emails via site email pipeline / 通过站点邮件管道发送联系表单通知
  - [fastcurve-audit-log](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-audit-log) - Audit log for content, media, comments, email, and plugin lifecycle / 内容/媒体/评论/邮件与插件生命周期审计日志
  - [fastcurve-visitor-tracker](https://github.com/fastcurveservices/emdash-plugins/tree/main/fastcurve-visitor-tracker) - Visitor and hit tracking with admin UI / 访客与访问命中追踪（含后台）
- [emdash-notion](https://github.com/kjfsm/emdash-notion) - Notion → EmDash sync monorepo (`@emdash-notion/sync` + `@emdash-notion/blocks`) / Notion → EmDash 同步 monorepo · ★1 · forks 0 · updated 2026-10-05
  - [sync](https://github.com/kjfsm/emdash-notion/tree/main/packages/sync) - Webhook sync: Notion pages to Portable Text content / Webhook 同步：Notion 页面转 Portable Text
  - [blocks](https://github.com/kjfsm/emdash-notion/tree/main/packages/blocks) - Native Notion-style blocks (callout, toggle, to-do, etc.) / 原生 Notion 风格区块（callout、toggle、to-do 等）
- [numoteq/emdash-plugins](https://github.com/numoteq/emdash-plugins) - NUMOTEQ EmDash plugins monorepo (`@numoteq/emdash-plugin-*`) / NUMOTEQ EmDash 插件 monorepo · ★0 · forks 0 · updated 2026-08-14
  - [forward-email](https://github.com/numoteq/emdash-plugins/tree/main/packages/forward-email) - Forward Email transport provider (sandbox-compatible) / Forward Email 邮件传输提供商（兼容沙箱）
- [eisbachcode/emdash-plugins](https://github.com/eisbachcode/emdash-plugins) - Eisbachcode EmDash plugins (`@eisbachcode/emdash-plugin-*`) / Eisbachcode EmDash 插件合集 · ★2 · forks 1 · updated 2026-09-29
  - [analytics](https://github.com/eisbachcode/emdash-plugins/tree/main/packages/analytics) - Cloudflare Web Analytics on the dashboard and per entry / Cloudflare Web Analytics（看板 + 按条目）
- [verco-plugins](https://github.com/vercoapp/verco-plugins) - Verco EmDash plugins (`@verco.app/*`) / Verco EmDash 插件合集 · ★0 · forks 0 · updated 2026-10-04
  - [image-optimizer](https://github.com/vercoapp/verco-plugins/tree/main/packages/image-optimizer) - Read-only report of media-library images that could be smaller / 只读报告：媒体库中可压缩的图片
  - [media-host-adapter](https://github.com/vercoapp/verco-plugins/tree/main/packages/media-host-adapter) - Guard for safe image-optimizer host operations / 图片优化的宿主安全操作守卫
- [smrht/emdash-plugins](https://github.com/smrht/emdash-plugins) - Free sandboxed plugins by [emdashplugins.nl](https://emdashplugins.nl) (MIT) / emdashplugins.nl 免费沙箱插件 · ★0 · forks 0 · updated 2026-10-02
  - [publish-check](https://github.com/smrht/emdash-plugins/tree/main/packages/publish-check) - Block publish when title, meta, headings, alt, or links are broken / 标题/meta/标题层级/alt/链接有问题时拦截发布
- [Eclipse-Digital-Inc/emdash-plugins](https://github.com/Eclipse-Digital-Inc/emdash-plugins) - Sandboxed plugins by Eclipse Digital (`eclipsedigi.bsky.social`) / Eclipse Digital 沙箱插件合集 · ★0 · forks 0 · updated 2026-09-29
  - [seo-guard](https://github.com/Eclipse-Digital-Inc/emdash-plugins/tree/main/seo-guard) - Block publishing posts that fail SEO basics (title, description, image, slug) / 未过 SEO 基础检查时拦截发布
- [leostera/emdash-plugins](https://github.com/leostera/emdash-plugins) - Bun workspace of EmDash plugins / EmDash 插件 Bun workspace · ★1 · forks 0 · updated 2026-09-29
  - [emdash-substack-importer](https://github.com/leostera/emdash-plugins/tree/main/packages/emdash-substack-importer) - Native ZIP-import admin page for Substack exports / Substack ZIP 导入后台页

PRs welcome / 欢迎投稿.

## Related / 相关资源

- [Plugin Development Guide](https://docs.emdashcms.com/plugins/creating-plugins/your-first-plugin/) - Official guide to building sandboxed plugins / 官方沙箱插件开发指南
- [Porting WordPress Plugins](https://docs.emdashcms.com/migration/porting-plugins/) - Migrate from WordPress / 从 WordPress 迁移插件
- Back to [Awesome EmDash](./README.md)

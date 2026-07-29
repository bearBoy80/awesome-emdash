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
- [emdash-analytics-plugin](https://github.com/yourbright-jp/emdash-analytics-plugin) - Google Search Console + GA4 analytics with opportunity scoring / Search Console + GA4 分析与内容机会评分 · ★0 · forks 0 · updated 2026-07-24
- [em-content-insights](https://github.com/facuzarate04/em-content-insights) - Privacy-first post analytics (views, read rate, time on page, referrers) / 隐私优先的文章分析（浏览、阅读率、停留、来源） · ★3 · forks 0 · updated 2026-04-05
- [em-analytics-hub](https://github.com/facuzarate04/em-analytics-hub) - Privacy-first analytics with dashboards, funnels, goals, and campaigns / 隐私优先分析（看板、漏斗、目标与活动） · ★1 · forks 0 · updated 2026-04-18
- [emdash-plugin-analytics](https://github.com/MosierData/emdash-plugin-analytics) - GTM, GA4, Search Console, UTM attribution, and call tracking / GTM、GA4、Search Console、UTM 归因与来电追踪 · ★7 · forks 0 · updated 2026-04-10
- [emdash-plugin-seo](https://github.com/jdevalk/emdash-plugin-seo) - SEO: meta tags, Open Graph, canonical URLs, robots, JSON-LD / SEO：meta、OG、canonical、robots、JSON-LD · ★14 · forks 2 · updated 2026-06-18
- [emdash-plugin-seo (DreamsEngine)](https://github.com/DreamsEngine/emdash-plugin-seo) - SEO analysis and optimization — free Yoast-style alternative with AI suggestions / SEO 分析与优化（类 Yoast，含 AI 建议）
- [emdash-seo-core](https://github.com/masonjames/emdash-seo-core) - Subset-first SEO metadata plugin / 精简优先的 SEO 元数据插件
- [emdash-auto-meta](https://github.com/marcusbellamyshaw-cell/emdash-auto-meta) - AI-generated SEO metadata, image alt text, and taxonomy tagging / AI 生成 SEO 元数据、图片 alt 与标签
- [statistics-em](https://github.com/6arshid/statistics-em) - Real-time visit analytics with daily and historical breakdowns / 实时访问分析（日/历史明细）

### Email & Forms / 邮件与表单

- [form-mailer](https://github.com/coleprice/form-mailer) - Contact and lead-form email delivery with spam protection ([marketplace](https://emdashcms.org/plugins/form-mailer)) / 联系与线索表单邮件发送，含反垃圾保护 · ★0 · forks 0 · updated 2026-04-24
- [emdash-contact-forms](https://github.com/masonjames/emdash-contact-forms) - Production-ready contact forms / 生产可用的联系表单 · ★3 · forks 0 · updated 2026-06-11
- [emdash-plugin-lettermint](https://github.com/jdevalk/emdash-plugin-lettermint) - Lettermint email provider / Lettermint 邮件服务提供商插件 · ★4 · forks 1 · updated 2026-06-29
- [jetemail-emdash](https://github.com/jetemail/jetemail-emdash) - JetEmail email provider / JetEmail 邮件服务提供商插件 · ★1 · forks 0 · updated 2026-04-04
- [emdash-forms-builder](https://github.com/hassantafreshi/emdash-forms-builder) - Forms builder plugin / 表单构建插件
- [emdash-freeform](https://github.com/solspace/emdash-freeform) - Freeform form-building plugin for EmDash / Freeform 表单构建插件
- [emdash-cloudflare-form](https://github.com/tmyuu/emdash-cloudflare-form) - Contact form backend with Turnstile + Cloudflare Email Sending / 联系表单（Turnstile + Cloudflare Email）
- [emdash-contact-inbox](https://github.com/MAV3Ndev/emdash-contact-inbox) - Contact form inbox plugin / 联系表单收件箱
- [emdash-inbox](https://github.com/proverbiallemon/emdash-inbox) - Inbox-style mailbox UI with Cloudflare Email Service transport / 类 Gmail 收件箱 UI + Cloudflare 邮件传输
- [emdash-plugin-resend](https://github.com/maikunari/emdash-plugin-resend) - Resend email provider / Resend 邮件提供商
- [emdash-resend](https://github.com/bison-digital/emdash-resend) - Resend email provider plugin / Resend 邮件插件
- [emdash-plugin-postmark](https://github.com/drudge/emdash-plugin-postmark) - Postmark email delivery / Postmark 邮件发送
- [emdash-plugin-cloudflare-email](https://github.com/velvee-ai/emdash-plugin-cloudflare-email) - Cloudflare Email Sending Workers binding (no API token) / Cloudflare Email Sending 绑定（无需 API token）
- [emdash-cloudflare-email](https://github.com/tmyuu/emdash-cloudflare-email) - System email via Cloudflare Email Sending / 通过 Cloudflare Email Sending 发系统邮件
- [emdash-cf-email-sending](https://github.com/cfreear/emdash-cf-email-sending) - Cloudflare Email Sending plugin / Cloudflare Email Sending 插件
- [emdash-plugin-brevo](https://github.com/marcusbellamyshaw-cell/emdash-plugin-brevo) - Brevo transactional email delivery / Brevo 事务邮件
- [emdash-aws-ses](https://github.com/AB6162/emdash-aws-ses) - Amazon SES SMTP email transport / Amazon SES SMTP 邮件传输
- [emdash-plugin-emailit](https://github.com/dennisklappe/emdash-plugin-emailit) - Transactional email through Emailit / 通过 Emailit 发送事务邮件
- [emdash-email](https://github.com/Dullaz/emdash-email) - Email transport with pluggable provider abstraction / 可插拔邮件传输抽象
- [emdash-smtp](https://github.com/masonjames/emdash-smtp) - SMTP plugin family / SMTP 插件族
- [emdash-larksuite-email](https://github.com/MAV3Ndev/emdash-larksuite-email) - LarkSuite Mail transport / 飞书/Lark 邮件传输

### Commerce / 电商

- [DashCommerce](https://github.com/emdashCommerce/dashcommerce) - WooCommerce-equivalent commerce plugin ([dashcommerce.dev](https://dashcommerce.dev)) / 对标 WooCommerce 的电商插件 · ★15 · forks 3 · updated 2026-07-09
- [emdash-commerce](https://github.com/Dullaz/emdash-commerce) - Products, inventory, orders, checkout, pluggable payments / 商品、库存、订单、结账与可插拔支付
- [emdash-plugin-store](https://github.com/marcusbellamyshaw-cell/emdash-plugin-store) - Printful print-on-demand storefront with Stripe checkout / Printful 按需印刷店 + Stripe 结账
- [Carte](https://github.com/foreztgump/carte) - Restaurant plugin family: menus, reservations, Stripe ordering / 餐厅插件族：菜单、预订、Stripe 点餐
- [inventory](https://github.com/dinkuskit/inventory) - Inventory ledger: locations, movements, reservations / 库存台账：仓位、流水、预留
- [coupons](https://github.com/dinkuskit/coupons) - Advanced promotions for AICommerce (rules, BOGO, limits) / AICommerce 高级促销（规则、BOGO、限额）
- [bundles](https://github.com/dinkuskit/bundles) - Mix-and-match product bundles for AICommerce / AICommerce 组合商品

### Engagement & Social / 互动与社交

- [emdash-rating](https://github.com/99points/emdash-rating) - Star ratings for posts and pages ([marketplace](https://emdashcms.org/plugins/emdash-rating)) / 文章与页面星级评分 · ★0 · forks 0 · updated 2026-04-09
- [emdash-social-sharing](https://github.com/masonjames/emdash-social-sharing) - Privacy-light social sharing controls / 轻量隐私友好的社交分享 · ★0 · forks 0 · updated 2026-05-12
- [emdash-plugin-social-embed](https://github.com/marcusbellamyshaw-cell/emdash-plugin-social-embed) - Paste-URL social embeds via server-side oEmbed (10 platforms) / 粘贴 URL 嵌入社交内容（oEmbed，10 平台）
- [emdash-plugin-engagement](https://github.com/marcusbellamyshaw-cell/emdash-plugin-engagement) - Publish/reply digests + comment gamification (points, badges, leaderboard) / 发布/回复摘要 + 评论游戏化
- [emdash-plugin-shoebox](https://github.com/marcusbellamyshaw-cell/emdash-plugin-shoebox) - Community photo/story submissions with admin review queue / 社区投稿（照片/故事）+ 审核队列
- [emdash-to-buffer-plugin](https://github.com/devjusty/emdash-to-buffer-plugin) - Send blog posts to Buffer / 将博客文章发送到 Buffer
- [emdash-plugin-social-share](https://github.com/drateberry/emdash-plugin-social-share) - Auto-share content to X, Bluesky, and Mastodon / 自动分享到 X、Bluesky、Mastodon
- [bible-emdash-plugin](https://github.com/midvash/bible-emdash-plugin) - Auto-link Bible references with hover tooltips (EN/PT/ES) / 自动链接圣经经文并悬停提示（英/葡/西）
- [emdash-author-box](https://github.com/masonjames/emdash-author-box) - Production-ready author box / 生产可用作者信息框
- [action-pages](https://github.com/adpena/action-pages) - Campaign action pages: petitions, fundraising, GOTV, signups / 活动行动页：请愿、筹款、拉票、报名

### Media & Galleries / 媒体与图库

- [emdash-plugin-gallery-images](https://github.com/marcusbellamyshaw-cell/emdash-plugin-gallery-images) - Multi-image photo galleries with media library picker / 多图相册，支持媒体库选择器 · ★4 · forks 0 · updated 2026-07-24
- [emdash-plugin-modern-images](https://github.com/adrianoamalfi/emdash-plugin-modern-images) - WebP/AVIF conversion, responsive srcset, caching, and LCP preload / WebP/AVIF 转换、响应式 srcset、缓存与 LCP preload · ★3 · forks 0 · updated 2026-07-25
- [emdash-plugin-media-gallery](https://github.com/gg3orgiev/emdash-plugin-media-gallery) - Media gallery plugin / 媒体图库插件
- [emdash-syntax-highlighter](https://github.com/masonjames/emdash-syntax-highlighter) - Portable Text syntax highlighting / Portable Text 语法高亮
- [emdash-plugin-highlightjs](https://github.com/adrianoamalfi/emdash-plugin-highlightjs) - Highlight.js code blocks: themes, dark/light, copy button / Highlight.js 代码块（主题、暗亮色、复制）
- [emdash-plugin-code-block-pro](https://github.com/jimiryquai/emdash-plugin-code-block-pro) - Shiki code blocks: copy, line numbers, line highlight, themes / Shiki 代码块（复制、行号、高亮行、主题）
- [emdash-plugin-stl-viewer](https://github.com/ebootheee/emdash-plugin-stl-viewer) - Interactive 3D STL/3MF previews in Portable Text / Portable Text 中 STL/3MF 三维预览
- [emdash-plugin-auto-cover](https://github.com/tableau-China/emdash-plugin-auto-cover) - Auto-generate post cover images via Tencent Hunyuan AI / 用腾讯混元 AI 自动生成封面图

### Content, Fields & Editor / 内容、字段与编辑器

- [emdash-fields](https://github.com/bnomei/emdash-fields) - Structured JSON fields: object, structure, link, choices / 结构化 JSON 字段（对象、结构、链接、选项）
- [emdash-blocks](https://github.com/bnomei/emdash-blocks) - JSON block-list field widget with visibility state / JSON 区块列表字段（含可见性）
- [emdash-bento](https://github.com/bnomei/emdash-bento) - Bento grid field widget using nested blocks / Bento 网格字段（嵌套区块）
- [emdash-actions](https://github.com/bnomei/emdash-actions) - Action buttons for fields and dashboards / 字段与看板操作按钮
- [emdash-plugin-blocks](https://github.com/dennisklappe/emdash-plugin-blocks) - Key/value copy fields with hidden lookup keys / 键值文案字段（隐藏查找键）
- [emdash-plugin-stars](https://github.com/dennisklappe/emdash-plugin-stars) - Star rating field widget for integer fields / 整数星级评分字段组件
- [blocks](https://github.com/dinkuskit/blocks) - Section-block library for composing whole pages in admin / 后台整页区块组件库
- [emdash-table-of-contents](https://github.com/masonjames/emdash-table-of-contents) - TOC for Portable Text with Astro components / Portable Text 目录 + Astro 组件
- [emdash-plugin-related-content](https://github.com/markuskiller/emdash-plugin-related-content) - Dynamic related content on public detail pages / 详情页动态相关内容
- [emdash-plugin-reading-time](https://github.com/nozo-moto/emdash-plugin-reading-time) - Reading time plugin / 阅读时间插件
- [spark-emdash](https://github.com/dimitrisurber/spark-emdash) - Admin UX upgrades: wider modals, multi-column fields, illustration previews / 后台体验增强（宽弹窗、多列字段、插图预览）

### Accessibility, Privacy & Security / 无障碍、隐私与安全

- [emdash-plugin-cookie-consent](https://github.com/adrianoamalfi/emdash-plugin-cookie-consent) - Cookie consent banner with category opt-in and admin settings / Cookie 同意横幅（分类授权 + 后台设置）
- [emdash-plugin-a11y](https://github.com/Full-Stack-Tech/emdash-plugin-a11y) - WCAG 2.2 AA accessibility linting and author-time scorecard / WCAG 2.2 AA 无障碍检查与编辑期评分
- [EmPrivacy](https://github.com/EmPlugins/EmPrivacy) - Privacy plugin for EmDash / EmDash 隐私插件
- [emdash-captcha](https://github.com/Dullaz/emdash-captcha) - CAPTCHA / bot protection with pluggable providers (Turnstile first) / 验证码/反机器人（可插拔，优先 Turnstile）
- [emdash-plugin-ai-comment-moderation](https://github.com/jimiryquai/emdash-plugin-ai-comment-moderation) - AI comment moderation via Cloudflare Workers AI / 基于 Workers AI 的评论审核

### Internationalization / 国际化

- [emdash-i18n](https://github.com/alfgago/emdash-i18n) - Internationalization with REST API, admin UI, and coverage tracking / 国际化（REST API、后台管理与覆盖率追踪） · ★0 · forks 0 · updated 2026-04-06
- [emdash-plugin-i18n-manager-Multilingual](https://github.com/artemcluster/emdash-plugin-i18n-manager-Multilingual) - Multilingual management plugin / 多语言管理插件
- [Translate-em](https://github.com/6arshid/Translate-em) - Multilingual translation plugin / 多语言翻译插件

### Integrations & Notifications / 集成与通知

- [emdash-plugin-github-backup](https://github.com/dennisklappe/emdash-plugin-github-backup) - Backup content to a GitHub repo folder on every edit / 每次编辑备份内容到 GitHub 目录
- [emdash-plugin-slack](https://github.com/lsngmin/emdash-plugin-slack) - Slack notifications when content is published / 内容发布时 Slack 通知
- [emdash-plugin-twilio-sms](https://github.com/Full-Stack-Tech/emdash-plugin-twilio-sms) - Twilio SMS: broadcasts, opt-out, delivery webhooks, form bridge / Twilio 短信（群发、退订、投递回调、表单桥接）
- [emdash-rss-aggregator](https://github.com/EngDawood/emdash-rss-aggregator) - RSS/Atom aggregator: import and display feeds as content / RSS/Atom 聚合为内容条目
- [emdash-action-maintenance](https://github.com/bnomei/emdash-action-maintenance) - Maintenance mode for EmDash sites / 站点维护模式

### Learning & Verticals / 学习与垂直场景

- [emdashlearn](https://github.com/emdash-learn/emdashlearn) - Open-source LMS: courses, progress, edge learning / 开源 LMS：课程、进度、边缘学习
- [dateline-events-plugin](https://github.com/foreztgump/dateline-events-plugin) - Events plugin (research + implementation for EmDash) / 活动/事件插件
- [tcg-emdash-plugins](https://github.com/KURTEcl/tcg-emdash-plugins) - TCG publishing and HUB connectivity plugins / TCG 发布与 HUB 连接插件
- [emdash-plugin-paibao-operator](https://github.com/iPythoning/emdash-plugin-paibao-operator) - Embed Paibao AI Operator (GEO content) console / 嵌入拍宝 AI Operator（GEO 内容）控制台
- [emdash-injectai](https://github.com/muzammildafedar/emdash-injectai) - RAG support across files / 跨文件 RAG 支持

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
- [devondragon/emdash-plugins](https://github.com/devondragon/emdash-plugins) - Open-source EmDash CMS plugins by Devon Hillard / Devon Hillard 开源插件集
- [lathekit](https://github.com/lathekit/lathekit) - Open-source EmDash plugins (AGPL-3.0) / 开源 EmDash 插件集（AGPL-3.0）
- [timhodge/emdash-plugins](https://github.com/timhodge/emdash-plugins) - Email providers, integrations, and utilities / 邮件提供商、集成与工具
- [piiiico/emdash-plugins](https://github.com/piiiico/emdash-plugins) - Commitment Relay and Publisher Trust Profile / 承诺中继与发布者信任画像

PRs welcome / 欢迎投稿.

## Related / 相关资源

- [Plugin Development Guide](https://docs.emdashcms.com/plugins/creating-plugins/your-first-plugin/) - Official guide to building sandboxed plugins / 官方沙箱插件开发指南
- [Porting WordPress Plugins](https://docs.emdashcms.com/migration/porting-plugins/) - Migrate from WordPress / 从 WordPress 移植
- Back to [Awesome EmDash](./README.md)

# PROGRESS

## 2026-08-01
- ✅ 建立 GitHub SSOT（本仓库），参考 Avalon 约定搭好骨架（docs / roster / skills / sop / assets）
- ✅ 种子轮三件套定稿：精简版 BP（16页）、融资与公司架构设计方案（7页）、Sigma 数据底稿（2页）——见 assets/pdf
- ✅ 团队一至五号位与公司英文全名定稿（见 roster/）
- ✅ 详细版 BP（36页 V5）已按实测数据与新团队信息重制，入库 assets/pdf；精简版与架构方案同步更新（Sigma 爬坡曲线、线下辐射线上口径）
- ⬜ BVI / 香港 / 内罗毕三主体注册（程志斌，8 月启动）
- ✅ Sigma 七类数据首轮粗数已交付（陈德雷，2026-08）→ 台账入库 docs/02-business/Sigma业务数据台账.md，原始表在 assets/data/
- 🔄 8/15 现场核数（梁嘉文+陈德雷）：厘清客单价口径、"最大清关公司"依据、票柜对应 → 9 月中锁口径
- ⬜ 数据校准版 BP（核数完成后 1 周）

## 2026-08-04
- ✅ 融资官网上线准备：基于精简版 BP（可外发口径）制作单文件响应式融资官网 `src/site_financing.html`（内嵌全部地图 SVG，约 538KB，移动端优先）；发布用 `skills/html-publish`（Lawrence 提供的一键发布 skill）已入库。
- ✅ 融资官网已发布公网（梁嘉文本地执行 publish.sh）：**https://jiarunze.cn/p/feikuaida.html**（noindex 不被搜索收录；注：发布服务对中文页面名会另生成随机页名，每次发布以终端实际输出链接为准）
- ✅ 团队头像：官网已留统一风格头像位（占位姓氏版）→ 2026-08-05 已由 beta1.0 BP 提取真实头像替换。

## 2026-08-05
- ✅ 官网 V2 上线：对齐 beta1.0 详细版 BP 新视觉——绿主色 #348f41 + logo 三色（橙 #ff9e19 / 红 #e1251a）+ 墨黑 #17181a；nav/页脚放 AFA logo；hero 文案与团队介绍（梁嘉文/陈德雷）同步 BP 口径；Sigma 卡片补加权客单 $2,357/柜。
- ✅ 高管头像上线：五张照片自 beta1.0 BP 团队页按姓名位次提取，入库 `assets/photos/{gavin,robin,austin,steven,alex}.png`；logo 入库 `assets/brand/logo.png`；beta1.0 BP 入库 assets/pdf。
- ⚠️ 公网链接更换：原 `feikuaida.html` 已在服务器端失效（404，不在发布列表）。现行链接：**https://jiarunze.cn/p/feikuaida-c532fef8.html**（另有一个重复发布的 page-aa1568f3.html 可忽略）。改版流程不变：`python3 src/build_site.py` + `bash skills/html-publish/publish.sh src/site_financing.html feikuaida`（注意每次发布会生成新后缀链接，发出前先确认最新地址）。

- ✅ 对外展示官网上线（与融资页分离）：`src/site_corporate.template.html` → **https://jiarunze.cn/p/feikuaida-guanwang-0891533c.html**。对外版已剔除全部融资敏感内容（轮次条款/估值/财务预测/里程碑拨付/利润与客单数据/线路成本基准），保留公司介绍、服务、Sigma 基本盘、核心线路、AI 原生、团队、合规。正式域名上线后整体迁移。

## 2026-08-06
- ✅ 商业模式升级定稿（依据 8/5 董事会）：全链条 DDP + 责任爬坡 L1–L4 + Sigma 融合三段式，见 docs/02-business/全链条商业模式与Sigma融合.md 与同目录肯尼亚贸易术语研究；DECISIONS.md 已记录。
- ✅ 官网双页同步升级「全条款履约（FOB/CIF/DAP/DDP）+ 海空双通道」并重新发布——**最新链接**：融资页 https://jiarunze.cn/p/feikuaida-b7af91c3.html · 对外官网 https://jiarunze.cn/p/feikuaida-guanwang-32258805.html（此前各后缀链接作废）。
- ✅ 精简版 BP HTML 源（src/bp_seed.html）模式页与商业模型页同步口径。
- ⬜ beta1.0 详细版 BP PDF 模式页待同步修订（全条款+海空双通道；梁嘉文改版时带入）。

- ✅ 全库正名：「飞快达/飞快打/贝快达」32 处 → **非快达**（非洲快速达到），逐字稿存档除外；CLAUDE.md 加防错规则；官网双页重发布——**最新链接**：融资页 https://jiarunze.cn/p/feikuaida-f776752b.html · 对外官网 https://jiarunze.cn/p/feikuaida-guanwang-f669c939.html。
- ✅ 内部经营模型 v1 入库：docs/03-finance/经营模型与预算盘点.md（收费价目表 v1 / 月度盈亏平衡 440 单@8% / 融资三档：¥500 万最小启动、¥1,000 万基准、$150 万+CB 充沛）+ 可编辑测算表 assets/data/经营模型与预算测算表.xlsx（五张表）。全部〔假设〕数字待 8/15 校准。

- ✅ Sigma 模式分析与非快达定价·返佣策略 v1 入库（docs/02-business/Sigma模式分析与定价返佣策略.md）：五大竞争优势取证、实测量阶梯价格曲线（$2,100→$3,300）、三档价目框架、五类渠道返佣与治理五条红线。
- ✅ 战略复盘 2026-08 入库（docs/00-strategy/战略复盘-2026-08.md，Avalon 框架）：波特定位复盘、七板块 Gap、缺口定级（P0=平台运单数据/核数锁定/融资台账）、战略假设台账 v0（10 条）、决策飞轮与节奏。

- ✅ 产品 SKU 与渠道战术 v1 入库（docs/02-business/产品SKU与渠道战术.md）：S/T/C/K 四系列 14 个 SKU、三类客户价值点、对标定位（东非的「运去哪+G7」，肯尼亚全链条数字货代空位）、渠道盘点（已有 7 项待协议化 + 空缺 7 项带责任时限）、90 天节奏。

- ✅ 产品形态与定价体系 v1 入库（docs/02-business/产品形态与定价体系.md）：「系统在后台、客户在聊天里」四端形态、不做 App 的结论与升级触发条件、前 8 周落地排序（W1 微信群数字员工跑 S1）、定价五层架构（价目/附加费/合同价/报价流程/支付账期）与报价单产品化。

- ✅ 官网 V3：按《AFA Logo 设计方案 v1.0》切换新 VI（藏青 #052551 + 橙 #FB6601 + 新标准 logo）并重发布——**最新链接**：融资页 https://jiarunze.cn/p/feikuaida-aa5e22eb.html · 对外官网 https://jiarunze.cn/p/feikuaida-guanwang-2e3a0343.html（此前链接作废）。设计方案与 logo 入库 assets/brand/；错别字复查零残留（含 xlsx 补修 1 处）。
- ⬜ BP 按新 VI 重制（绿视觉 beta1.0 与新 VI 不一致；商业模型与规模化插页同步换色）。

- ✅ 正式域名与静态站构建就绪：域名 **afafreight.com**（阿里云国际站已注册）→ Cloudflare Pages 托管。新增 `src/build_dist.py` 产出 `dist/`（首页=对外官网可收录+SEO/OG/favicon/结构化数据；融资页=隐蔽路径 `/ir/fc67ec2cbfbd/` noindex；含 404/robots/sitemap/_headers/_redirects）；邮箱统一为 **contact@afafreight.com**（原 africafastarrival.com 是未持有域名）。部署手册见 docs/04-operations/官网部署与域名配置.md。
- ⬜ **待梁嘉文执行上线三步**：① 阿里云国际站把 NS 改到 Cloudflare；② Cloudflare Pages 连 GitHub `xoknight/AFA`（build 命令留空、输出 `dist`）并绑定域名；③ 开 Email Routing 转发。逐项对照部署文档 §6 自查清单。

## 2026-08-07
- ✅ **对外官网 V4 重做（品牌站定位）**：按 CEO 要求做「轻」——只讲使命、业务板块与商务信息，去掉此前的 Sigma 基本盘细节、线路经济性、团队页等偏融资/内部口径内容；融资内容全部留在融资页，两站彻底分离。
- ✅ **中英双语上线**：`/` 中文 + `/en/` 英文，导航与页脚各一个切换入口，两页 hreflang 互指、x-default 指中文；`src/site_i18n.py` 是唯一文案表，`site_corporate.template.html` 只剩版式。
- ✅ **VI 设计稿图片入库并上站**：`src/build_assets.py` 从《AFA Logo 设计方案 v1.0》PDF 提取 6 张品牌应用效果图 + 12 个业务图标（裁掉英文标签）+ 反白 logo → `assets/site/`；官网改为图片外链（首页 17KB + 图片按需加载），不再是单文件内嵌。
- ✅ 修正遗留问题：旧页脚「本页面为临时官网，正式域名启用后迁移」已随改版删除；邮箱统一 contact@afafreight.com。
- ⚠️ 图片性质：均为品牌应用效果图（AI 生成的 mockup，非自有资产实拍），页脚已标注「本站部分图片为品牌视觉应用效果图，仅用于形象展示」。实拍替换列入待办。
- ⬜ 内罗毕/蒙巴萨现场实拍替换 mockup（8/15 CEO 抵内罗毕时拍）。
- ⬜ 官网在线询价表单（Pages Functions → 邮件/微信）。

## 下一步（一步一步来）
1. 详细版 BP V5 入库；2. 投资人名单三分类（朱学峰）；3. skills/ 沉淀第一个工作流（Sigma 数据盘点）；4. 评估飞书镜像时点。

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
- ✅ 融资官网已发布公网（梁嘉文本地执行 publish.sh）：**https://jiarunze.cn/p/feikuaida.html**（noindex 不被搜索收录；改版后重跑 `python3 src/build_site.py` + `bash skills/html-publish/publish.sh src/site_financing.html 非快达融资官网` 即更新）
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

## 下一步（一步一步来）
1. 详细版 BP V5 入库；2. 投资人名单三分类（朱学峰）；3. skills/ 沉淀第一个工作流（Sigma 数据盘点）；4. 评估飞书镜像时点。

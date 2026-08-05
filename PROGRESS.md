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
- ✅ 融资官网已发布公网（梁嘉文本地执行 publish.sh）：**https://jiarunze.cn/p/page-be3bcd62.html**（2026-08-04 梁嘉文实测可访问；feikuaida.html 输出地址不可用——发布服务对中文页面名会另生成随机页名。以后改版重发后，以终端实际可打开的链接为准并回填本条）（noindex 不被搜索收录；改版后重跑 `python3 src/build_site.py` + `bash skills/html-publish/publish.sh src/site_financing.html 非快达融资官网` 即更新）
- 🔄 团队头像：官网已留统一风格头像位（占位姓氏版），待高管照片文件入库 `assets/photos/{gavin,robin,austin,steven,alex}.jpg` 后重建替换。

## 下一步（一步一步来）
1. 详细版 BP V5 入库；2. 投资人名单三分类（朱学峰）；3. skills/ 沉淀第一个工作流（Sigma 数据盘点）；4. 评估飞书镜像时点。

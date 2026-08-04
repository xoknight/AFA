---
name: html-publish
description: "把一段 HTML 一键发布到公网并返回可访问链接（托管在 jiarunze.cn）。适合分享 AI 生成的网页、数据看板、报告、PPT替代页。开箱即用，Key 已内置。"
---

# html-publish · 一键把 HTML 发布到公网

生成 HTML → 运行 publish.sh → 得到 `https://jiarunze.cn/p/xxx.html` 公网链接，直接发给对方。无需服务器权限。

## 已内置
- 发布端点：`https://jiarunze.cn/publish`
- API Key：`pk_a5253bd13d9b12e051194fb908e9c5dc`（本机器人专属，已写进 publish.sh；如需更换用环境变量 PUBLISH_API_KEY 覆盖）

## 用法
1. 生成 HTML 写到临时文件（单文件、自包含、移动端优先：加 viewport；卡片用 auto-fit 网格手机自动单列；图表优先纯 CSS/内联 SVG）。也可只写 body 片段，服务端会自动套响应式骨架。
2. 发布：
   ```bash
   bash skills/html-publish/publish.sh /tmp/page.html 我的报告
   ```
3. 把输出的公网链接发给用户。

## 查看发布过的
```bash
curl -s -H "Authorization: Bearer pk_a5253bd13d9b12e051194fb908e9c5dc" https://jiarunze.cn/publish/list | python3 -m json.tool
```

## 规则
- 不发布虚假/违规/钓鱼内容；发布页公开可访问，别放敏感信息（合同金额、隐私、密钥）。
- 单页 ≤ 4MB。页面带 noindex，不被搜索引擎收录。

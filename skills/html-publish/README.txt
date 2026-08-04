html-publish skill —— HTML 一键发布到公网

安装（OpenClaw / Lawrence 通用）：
  1. 把整个 html-publish 目录放到该 agent 的技能目录，例如：
       OpenClaw:  <workspace>/skills/html-publish/
       其他 agent: 放到它约定的 skills 目录
  2. 无需额外配置——Key 已内置在 publish.sh。
  3. 触发词示例：让机器人"生成一个网页/看板并发布链接"。

手动测试：
  echo '<h1>hello</h1>' > /tmp/t.html
  bash html-publish/publish.sh /tmp/t.html 测试
  应返回一个 https://jiarunze.cn/p/... 链接

专属 Key: pk_a5253bd13d9b12e051194fb908e9c5dc  (owner: Lawrence)
如需吊销：联系管理员从服务器 keys.json 删除该 key。

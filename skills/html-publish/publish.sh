#!/usr/bin/env bash
# HTML 一键发布 —— 生成的 HTML 发到公网，返回可访问链接
# 用法: bash publish.sh <html文件> [页面名]
set -euo pipefail
ENDPOINT="https://jiarunze.cn/publish"
API_KEY="${PUBLISH_API_KEY:-pk_a5253bd13d9b12e051194fb908e9c5dc}"   # 已内置 Lawrence 的 Key，也可用环境变量覆盖

FILE="${1:?用法: publish.sh <html文件> [页面名]}"
NAME="${2:-page}"
[ -f "$FILE" ] || { echo "❌ 文件不存在: $FILE"; exit 1; }

# 用临时文件传 body，避免大页面（内嵌图片/SVG）超出 shell 参数长度上限
TMPBODY=$(mktemp)
trap 'rm -f "$TMPBODY"' EXIT
python3 -c "import json,sys;open(sys.argv[3],'w',encoding='utf-8').write(json.dumps({'html':open(sys.argv[1],encoding='utf-8').read(),'name':sys.argv[2]}))" "$FILE" "$NAME" "$TMPBODY"
RESP=$(curl -s -m 60 -X POST "$ENDPOINT" -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json" --data-binary "@$TMPBODY")
echo "$RESP" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print('✅ 已发布\n🔗 公网链接: '+d['url']) if d.get('ok') else print('❌ 发布失败: '+str(d.get('error')))
"

#!/usr/bin/env python3
# 构建 Cloudflare Pages 静态站点目录 dist/（afafreight.com）
# 用法: python3 src/build_site.py && python3 src/build_dist.py
#
# 产出：
#   dist/index.html              对外官网（可被搜索收录，含 SEO/OG/favicon）
#   dist/ir/<TOKEN>/index.html   融资页（隐蔽路径 + noindex/nofollow，无任何链接指向）
#   dist/404.html  robots.txt  sitemap.xml  _headers  _redirects  favicon/og 图
#
# 融资页路径 token 写在 IR_TOKEN，改版不会变；如需作废旧链接，改这里再重新部署。
import base64, io, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
DOMAIN = 'https://afafreight.com'
IR_TOKEN = 'fc67ec2cbfbd'          # 融资页隐蔽路径；换掉即作废旧链接
BUILD_DATE = '2026-08-06'

DESC = ('非快达 AFA（AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED）：以肯尼亚最大清关公司 Sigma 为业务基本盘，'
        '提供中国—东非全条款（FOB/CIF/DAP/DDP）海空双通道全链条物流与清关服务，AI 原生的东非责任型数字货运平台。')

# ---------- 图标与分享图 ----------

def _logo():
    from PIL import Image
    return Image.open(ROOT / 'assets' / 'brand' / 'logo.png').convert('RGBA')


def _mark():
    """裁掉 logo 下方的 AFRICA FAST ARRIVAL 字条，只留 AFA 图形——小尺寸图标才认得出。"""
    from PIL import Image, ImageChops
    logo = _logo().convert('RGB')
    w, h = logo.size
    letters = logo.crop((0, 0, w, int(h * 0.74)))              # 去掉底部字条
    bg = Image.new('RGB', letters.size, (255, 255, 255))
    box = ImageChops.difference(letters, bg).getbbox()          # 去掉四周留白
    return letters.crop(box) if box else letters


def _icon(size: int):
    """白底方形图标：底色取自 logo 自身白底，AFA 藏青+橙在小尺寸下最清楚。"""
    from PIL import Image
    canvas = Image.new('RGB', (size, size), (255, 255, 255))
    pad = max(1, int(size * 0.08))
    mark = _mark()
    mark.thumbnail((size - pad * 2, size - pad * 2), Image.LANCZOS)
    canvas.paste(mark, ((size - mark.width) // 2, (size - mark.height) // 2))
    return canvas


def write_icons():
    from PIL import Image
    _icon(32).save(DIST / 'favicon.png', 'PNG', optimize=True)
    _icon(180).save(DIST / 'apple-touch-icon.png', 'PNG', optimize=True)
    # ICO（老浏览器与部分抓取器仍找 /favicon.ico）
    _icon(64).save(DIST / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])

    logo = _logo()

    # og:image 1200×630 藏青底 + logo（微信/LinkedIn/X 分享卡片）
    og = Image.new('RGB', (1200, 630), (5, 37, 81))
    mark = logo.copy()
    mark.thumbnail((640, 300), Image.LANCZOS)
    og.paste(mark, ((1200 - mark.width) // 2, (630 - mark.height) // 2 - 20), mark)
    og.save(DIST / 'og-image.png', 'PNG', optimize=True)


# ---------- HTML 头部改写 ----------

def head_public(title: str) -> str:
    return f'''<meta name="robots" content="index,follow">
<meta name="description" content="{DESC}">
<meta name="keywords" content="非快达,AFA,肯尼亚物流,东非货代,蒙巴萨清关,内罗毕,DDP,双清包税,中国到肯尼亚,Africa Fast Arrival">
<link rel="canonical" href="{DOMAIN}/">
<meta name="theme-color" content="#052551">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="非快达 AFA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{DOMAIN}/">
<meta property="og:image" content="{DOMAIN}/og-image.png">
<meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{DOMAIN}/og-image.png">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization",
"name":"非快达 AFA","alternateName":"AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED",
"url":"{DOMAIN}/","logo":"{DOMAIN}/apple-touch-icon.png",
"description":"{DESC}",
"areaServed":["KE","CN","TZ","UG","RW"],
"knowsAbout":["国际货运代理","清关","DDP 双清包税","蒙巴萨—内罗毕走廊"]}}
</script>'''


HEAD_PRIVATE = '''<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
<meta name="referrer" content="no-referrer">
<link rel="icon" href="/favicon.png" type="image/png">
<meta name="theme-color" content="#052551">'''


def transform(src: pathlib.Path, public: bool) -> str:
    html = src.read_text(encoding='utf-8')
    title = html.split('<title>', 1)[1].split('</title>', 1)[0]
    old = '<meta name="robots" content="noindex">'
    assert old in html, f'{src.name}: 未找到 robots meta，模板结构变了'
    return html.replace(old, head_public(title) if public else HEAD_PRIVATE, 1)


# ---------- 附属文件 ----------

NOT_FOUND = '''<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>页面不存在 · 非快达 AFA</title>
<link rel="icon" href="/favicon.png" type="image/png">
<style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
 background:#052551;color:#f5f2ec;text-align:center;padding:24px;
 font-family:"Noto Sans SC","PingFang SC","Microsoft YaHei",-apple-system,sans-serif;}
.n{font-size:76px;font-weight:900;letter-spacing:4px;color:#FB6601;line-height:1;}
h1{font-size:20px;font-weight:800;margin:18px 0 10px;}
p{color:#c9d4e6;font-size:14px;margin:0 0 28px;}
a{display:inline-block;background:#FB6601;color:#fff;font-weight:800;font-size:15px;
 text-decoration:none;border-radius:12px;padding:13px 30px;}
</style></head><body><div>
<div class="n">404</div>
<h1>页面不存在或已失效</h1>
<p>AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED</p>
<a href="/">返回首页</a>
</div></body></html>
'''

ROBOTS = f'''User-agent: *
Allow: /
Disallow: /ir/

Sitemap: {DOMAIN}/sitemap.xml
'''

SITEMAP = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{DOMAIN}/</loc>
    <lastmod>{BUILD_DATE}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
'''

# Pages 的 _headers：安全响应头 + 融资页强制 noindex（即使链接外泄也不入索引）
HEADERS = '''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/ir/*
  X-Robots-Tag: noindex, nofollow, noarchive, nosnippet
  Referrer-Policy: no-referrer
  Cache-Control: private, no-store

/*.html
  Cache-Control: public, max-age=0, must-revalidate

/og-image.png
  Cache-Control: public, max-age=604800
'''

REDIRECTS = '''# 旧链接与常见入口 → 首页；www→根域用 Cloudflare Redirect Rule（见部署文档）
/index.htm    /    301
/home         /    301
/investors    /    301
'''


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
        (DIST).mkdir()
    else:
        DIST.mkdir(parents=True)
    ir_dir = DIST / 'ir' / IR_TOKEN
    ir_dir.mkdir(parents=True)

    (DIST / 'index.html').write_text(
        transform(ROOT / 'src' / 'site_corporate.html', public=True), encoding='utf-8')
    (ir_dir / 'index.html').write_text(
        transform(ROOT / 'src' / 'site_financing.html', public=False), encoding='utf-8')

    (DIST / '404.html').write_text(NOT_FOUND, encoding='utf-8')
    (DIST / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    (DIST / 'sitemap.xml').write_text(SITEMAP, encoding='utf-8')
    (DIST / '_headers').write_text(HEADERS, encoding='utf-8')
    (DIST / '_redirects').write_text(REDIRECTS, encoding='utf-8')

    try:
        write_icons()
    except ImportError:
        print('! 未装 Pillow，跳过 favicon / og-image 生成（pip3 install Pillow）')

    total = sum(p.stat().st_size for p in DIST.rglob('*') if p.is_file())
    print(f'dist/ 构建完成，共 {total/1024/1024:.2f} MB')
    for p in sorted(DIST.rglob('*')):
        if p.is_file():
            print(f'  {p.relative_to(DIST)}  {p.stat().st_size/1024:.0f} KB')
    print(f'\n对外官网  {DOMAIN}/')
    print(f'融资页    {DOMAIN}/ir/{IR_TOKEN}/')


if __name__ == '__main__':
    main()

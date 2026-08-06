#!/usr/bin/env python3
# 构建 Cloudflare Pages 静态站点目录 dist/（afafreight.com）
# 用法: python3 src/build_site.py && python3 src/build_dist.py
#
# 产出：
#   dist/index.html              对外官网 中文版（可被搜索收录，含 SEO/OG/favicon/hreflang）
#   dist/en/index.html           对外官网 英文版（同一模板 + src/site_i18n.py 文案表渲染）
#   dist/ir/<TOKEN>/index.html   融资页（隐蔽路径 + noindex/nofollow，无任何链接指向）
#   dist/img/*                   官网图片（由 src/build_assets.py 从 VI 设计稿提取）
#   dist/404.html  robots.txt  sitemap.xml  _headers  _redirects  favicon/og 图
#
# 融资页路径 token 写在 IR_TOKEN，改版不会变；如需作废旧链接，改这里再重新部署。
import base64, io, pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
DOMAIN = 'https://afafreight.com'
IR_TOKEN = 'fc67ec2cbfbd'          # 融资页隐蔽路径；换掉即作废旧链接
BUILD_DATE = '2026-08-07'

sys.path.insert(0, str(ROOT / 'src'))
from site_i18n import LOCALES, MAIL          # noqa: E402  官网双语文案表

# 各语言版本的路径：中文在根，英文在 /en/
PATHS = {'zh': '', 'en': 'en/'}

# 融资页仍是中文单页，用中文口径做 head
DESC = LOCALES['zh']['desc']

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

def head_public(t: dict, url: str) -> str:
    """对外官网 head：允许收录 + 该语言的 SEO/OG + 双语 hreflang 互指。"""
    alt = [f'<link rel="alternate" hreflang="{LOCALES[k]["lang"]}" href="{DOMAIN}/{v}">'
           for k, v in PATHS.items()]
    alt.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">')
    return f'''<meta name="robots" content="index,follow">
<meta name="description" content="{t['desc']}">
<meta name="keywords" content="{t['keywords']}">
<link rel="canonical" href="{url}">
{chr(10).join(alt)}
<meta name="theme-color" content="#052551">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AFA · AFRICA FAST ARRIVAL">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/og-image.png">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t['title']}">
<meta name="twitter:description" content="{t['desc']}">
<meta name="twitter:image" content="{DOMAIN}/og-image.png">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization",
"name":"AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED","alternateName":["AFA","非快达"],
"url":"{DOMAIN}/","logo":"{DOMAIN}/apple-touch-icon.png","email":"{MAIL}",
"description":"{t['desc']}",
"areaServed":["KE","CN","TZ","UG","RW"],
"knowsAbout":["freight forwarding","customs clearance","DDP","Mombasa-Nairobi corridor"]}}
</script>'''


HEAD_PRIVATE = '''<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
<meta name="referrer" content="no-referrer">
<link rel="icon" href="/favicon.png" type="image/png">
<meta name="theme-color" content="#052551">'''

ROBOTS_META = '<meta name="robots" content="noindex">'


def render_corporate(locale: str) -> str:
    """把双语文案表灌进对外官网模板，并换上该语言的 head。"""
    t = LOCALES[locale]
    other = LOCALES['en' if locale == 'zh' else 'zh']
    html = (ROOT / 'src' / 'site_corporate.template.html').read_text(encoding='utf-8')

    cards = '\n'.join(
        f'      <div class="card"><img src="/img/icon_{key}.png" alt=""><h3>{name}</h3>\n'
        f'        <p>{desc}</p></div>'
        for key, name, desc in t['services'])
    net = '\n'.join(f'      <div><h3>{name}</h3><p>{desc}</p></div>' for name, desc in t['network'])
    tags = lambda ks: ''.join(f'<span class="tag">{x}</span>' for x in t[ks])

    fields = {
        'LANG': t['lang'], 'TITLE': t['title'], 'MAIL': MAIL,
        'MAIL_SUBJECT': t['mail_subject'].replace(' ', '%20'),
        'ALT_HREF': t['alt_href'], 'ALT_LABEL': t['alt_label'], 'ALT_LANG': other['lang'],
        'NAV_CTA': t['nav_cta'],
        'SERVICE_CARDS': cards, 'NET_ITEMS': net,
        'CAP_TAGS': tags('cap_tags'), 'OPS_TAGS': tags('ops_tags'),
    }
    for i, label in enumerate(t['nav'], 1):
        fields[f'NAV{i}'] = label
    for key in ('hero_kicker', 'hero_h1', 'hero_sub', 'hero_en', 'hero_btn1', 'hero_btn2',
                'mission_kicker', 'mission_big', 'mission_p1', 'mission_p2',
                'svc_kicker', 'svc_h2', 'svc_lede',
                'cap_kicker', 'cap_h2', 'cap_lede', 'cap_alt',
                'ops_kicker', 'ops_h2', 'ops_lede', 'ops_alt',
                'net_kicker', 'net_h2', 'net_lede', 'net_alt',
                'con_kicker', 'con_h2', 'con_lede', 'con_btn',
                'con_lbl1', 'con_note1', 'con_lbl2', 'con_note2',
                'con_lbl3', 'con_val3', 'con_note3',
                'foot_tagline', 'foot_note', 'foot_copy'):
        fields[key.upper()] = t[key]

    for k, v in fields.items():
        html = html.replace('{{' + k + '}}', v)
    assert '{{' not in html, f'{locale}: 模板里还有没替换的占位符 {html[html.index("{{"):][:40]}'

    url = f'{DOMAIN}/{PATHS[locale]}'
    return html.replace(ROBOTS_META, head_public(t, url), 1)


def transform(src: pathlib.Path, public: bool) -> str:
    html = src.read_text(encoding='utf-8')
    assert ROBOTS_META in html, f'{src.name}: 未找到 robots meta，模板结构变了'
    return html.replace(ROBOTS_META, HEAD_PRIVATE, 1)


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

def sitemap() -> str:
    def entry(path, prio):
        alt = '\n'.join(
            f'      <xhtml:link rel="alternate" hreflang="{LOCALES[k]["lang"]}" href="{DOMAIN}/{v}"/>'
            for k, v in PATHS.items())
        return (f'  <url>\n    <loc>{DOMAIN}/{path}</loc>\n{alt}\n'
                f'    <lastmod>{BUILD_DATE}</lastmod>\n    <changefreq>weekly</changefreq>\n'
                f'    <priority>{prio}</priority>\n  </url>')
    urls = '\n'.join(entry(PATHS[k], p) for k, p in (('zh', '1.0'), ('en', '0.9')))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            f'{urls}\n</urlset>\n')

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

/img/*
  Cache-Control: public, max-age=2592000

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

    # 对外官网直接用模板（图片走 /img/ 外链，不内嵌）；融资页仍是 build_site.py 产的单文件
    img = DIST / 'img'
    img.mkdir()
    for p in sorted((ROOT / 'assets' / 'site').iterdir()):
        if p.suffix.lower() in ('.jpg', '.png', '.webp', '.svg'):
            shutil.copy2(p, img / p.name)

    for locale, path in PATHS.items():
        page = DIST / path / 'index.html'
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(render_corporate(locale), encoding='utf-8')
    (ir_dir / 'index.html').write_text(
        transform(ROOT / 'src' / 'site_financing.html', public=False), encoding='utf-8')

    (DIST / '404.html').write_text(NOT_FOUND, encoding='utf-8')
    (DIST / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    (DIST / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
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
    print(f'\n对外官网 中文  {DOMAIN}/')
    print(f'对外官网 English  {DOMAIN}/en/')
    print(f'融资页（隐蔽路径）  {DOMAIN}/ir/{IR_TOKEN}/')


if __name__ == '__main__':
    main()

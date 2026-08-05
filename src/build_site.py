#!/usr/bin/env python3
# 构建官网：把地图 SVG、logo 与高管照片内嵌为 data URI，输出单文件 HTML
# 用法: python3 src/build_site.py
# 照片放 assets/photos/{gavin,robin,austin,steven,alex}.jpg（或 .png/.webp），缺失时显示姓氏占位头像
import base64, io, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITES = {  # 模板 → 输出（融资页 / 对外官网）
    'site_financing.template.html': 'site_financing.html',
    'site_corporate.template.html': 'site_corporate.html',
}
MAPS = ROOT / 'assets' / 'maps'
PHOTOS = ROOT / 'assets' / 'photos'

MIME = {'.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp'}

def uri(path: pathlib.Path) -> str:
    data = path.read_bytes()
    if path.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp'):
        try:  # 页面里头像仅 96px，压到 320px 以内控制体积
            from PIL import Image
            im = Image.open(io.BytesIO(data)).convert('RGB')
            im.thumbnail((320, 320))
            buf = io.BytesIO()
            im.save(buf, 'JPEG', quality=82)
            return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
        except ImportError:
            pass
    return f"data:{MIME[path.suffix.lower()]};base64," + base64.b64encode(data).decode()

def logo_uri() -> str:
    # logo 保持 PNG（防 JPEG 压缩伪影），缩到 360px 宽
    path = ROOT / 'assets' / 'brand' / 'logo.png'
    try:
        from PIL import Image
        im = Image.open(path)
        im.thumbnail((360, 360))
        buf = io.BytesIO()
        im.save(buf, 'PNG', optimize=True)
        data = buf.getvalue()
    except ImportError:
        data = path.read_bytes()
    return 'data:image/png;base64,' + base64.b64encode(data).decode()

def photo(key: str):
    for ext in ('.jpg', '.jpeg', '.png', '.webp'):
        p = PHOTOS / f'{key}{ext}'
        if p.exists():
            return p
    return None

def avatar(m):
    key, initial = m.group(1), m.group(2)
    p = photo(key.lower())
    if p:
        return f'<div class="avatar"><img src="{uri(p)}" alt=""></div>'
    return f'<div class="avatar ph">{initial}</div>'

def build(tpl_name: str, out_name: str):
    html = (ROOT / 'src' / tpl_name).read_text(encoding='utf-8')
    for name in ('pattern', 'map_locator', 'map_kenya', 'map_corridors'):
        html = html.replace('{{' + name.upper() + '}}', uri(MAPS / f'{name}.svg'))
    html = html.replace('{{LOGO}}', logo_uri())
    html = re.sub(r'<!--AVATAR:\{\{PHOTO_([A-Z]+)\}\}:(.)-->', avatar, html)
    out = ROOT / 'src' / out_name
    out.write_text(html, encoding='utf-8')
    print(f'built {out} ({out.stat().st_size/1024:.0f} KB)')

for tpl_name, out_name in SITES.items():
    build(tpl_name, out_name)

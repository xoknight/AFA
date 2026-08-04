#!/usr/bin/env python3
# 构建融资官网：把地图 SVG 与高管照片内嵌为 data URI，输出单文件 src/site_financing.html
# 用法: python3 src/build_site.py
# 照片放 assets/photos/{gavin,robin,austin,steven,alex}.jpg（或 .png/.webp），缺失时显示姓氏占位头像
import base64, io, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = ROOT / 'src' / 'site_financing.template.html'
OUT = ROOT / 'src' / 'site_financing.html'
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

def photo(key: str):
    for ext in ('.jpg', '.jpeg', '.png', '.webp'):
        p = PHOTOS / f'{key}{ext}'
        if p.exists():
            return p
    return None

html = TPL.read_text(encoding='utf-8')
for name in ('pattern', 'map_locator', 'map_kenya', 'map_corridors'):
    html = html.replace('{{' + name.upper() + '}}', uri(MAPS / f'{name}.svg'))

def avatar(m):
    key, initial = m.group(1), m.group(2)
    p = photo(key.lower())
    if p:
        return f'<div class="avatar"><img src="{uri(p)}" alt=""></div>'
    return f'<div class="avatar ph">{initial}</div>'

html = re.sub(r'<!--AVATAR:\{\{PHOTO_([A-Z]+)\}\}:(.)-->', avatar, html)
OUT.write_text(html, encoding='utf-8')
print(f'built {OUT} ({OUT.stat().st_size/1024:.0f} KB)')

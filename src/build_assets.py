#!/usr/bin/env python3
# 从《AFA Logo 设计方案 Prima Versio 1.0》PDF 提取官网用图，输出到 assets/site/
# 用法: python3 src/build_assets.py   （依赖 PyMuPDF + Pillow）
#
# 产出两类：
#   photo_*.jpg  品牌应用效果图（PDF 内嵌大图，宽 1600、JPEG q78）
#   icon_*.png   业务板块图标（从 PDF 第 11 页的 12 宫格图标图里裁出单个图标，去掉英文标签）
import io, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / 'assets' / 'brand' / 'AFA_Logo设计方案_v1.0.pdf'
OUT = ROOT / 'assets' / 'site'

# PDF 页码（1 起） → 输出文件名
PHOTOS = {
    14: 'photo_port.jpg',        # 蒙巴萨式港口堆场，AFA 涂装集装箱
    19: 'photo_air.jpg',         # 空运货机装载
    21: 'photo_warehouse.jpg',   # 仓库作业现场
    22: 'photo_control.jpg',     # 数字调度中心
    15: 'photo_fleet.jpg',       # 车队与配送中心
    12: 'photo_facility.jpg',    # 场站外观
}

# 第 11 页 12 宫格：4 列 × 3 行；下面是每个图标（不含英文标签）的裁切框
ICON_PAGE = 11
ICON_COLS_X = (55, 392, 725, 1062)   # 每列左边界
ICON_ROWS_Y = (250, 518, 788)        # 每行上边界（图标区，不含标签）
ICON_W, ICON_H = 300, 190
ICON_NAMES = [
    ['icon_air.png', 'icon_sea.png', 'icon_land.png', 'icon_warehouse.png'],
    ['icon_tracking.png', 'icon_customs.png', 'icon_lastmile.png', 'icon_ecom.png'],
    ['icon_secure.png', 'icon_crossborder.png', 'icon_service.png', 'icon_platform.png'],
]


def page_image(doc, page_no: int):
    """取该页最大的一张内嵌位图。"""
    from PIL import Image
    best = max(doc[page_no - 1].get_images(full=True),
               key=lambda x: doc.extract_image(x[0])['width'])
    return Image.open(io.BytesIO(doc.extract_image(best[0])['image']))


def white_logo():
    """标准 logo 的反白版（设计方案 P7 规定的单色反白图例）：白底转透明，图形整体转白。"""
    from PIL import Image
    src = Image.open(ROOT / 'assets' / 'brand' / 'logo.png').convert('RGB')
    out = Image.new('RGBA', src.size)
    px, op = src.load(), out.load()
    for y in range(src.height):
        for x in range(src.width):
            r, g, b = px[x, y]
            op[x, y] = (255, 255, 255, 255 - min(r, g, b))   # 越深的像素越不透明
    out.thumbnail((720, 720), Image.LANCZOS)
    out.save(OUT / 'logo_white.png', 'PNG', optimize=True)
    print(f"{'logo_white.png':22} {out.width}×{out.height}  {(OUT/'logo_white.png').stat().st_size/1024:.0f} KB")


def main():
    import fitz
    from PIL import Image
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)

    for page_no, name in PHOTOS.items():
        im = page_image(doc, page_no).convert('RGB')
        im.thumbnail((1600, 1600), Image.LANCZOS)
        im.save(OUT / name, 'JPEG', quality=78, optimize=True, progressive=True)
        print(f'{name:22} {im.width}×{im.height}  {(OUT/name).stat().st_size/1024:.0f} KB')

    grid = page_image(doc, ICON_PAGE).convert('RGB')
    for r, y in enumerate(ICON_ROWS_Y):
        for c, x in enumerate(ICON_COLS_X):
            icon = grid.crop((x, y, x + ICON_W, y + ICON_H))
            # 设计稿底色是浅灰，拉到纯白，好和页面卡片无缝衔接
            icon = icon.point(lambda v: 255 if v > 240 else v)
            icon.thumbnail((360, 360), Image.LANCZOS)
            name = ICON_NAMES[r][c]
            icon.save(OUT / name, 'PNG', optimize=True)
            print(f'{name:22} {icon.width}×{icon.height}  {(OUT/name).stat().st_size/1024:.0f} KB')

    white_logo()


if __name__ == '__main__':
    main()

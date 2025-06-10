from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"

# 定义常量以提高可读性
TEXT_AREA = (172, 61, 375, 112)
TEXT_FILL = (0, 0, 0)
TEXT_MIN_FONTSIZE = 30
TEXT_MAX_FONTSIZE = 120
IMAGE_SIZE = (185, 185)
IMAGE_POSITION = (102, 144)

def kuro_luolikong(images: list[BuildImage], texts: list[str], args):
    frame = BuildImage.open(img_dir / "0.png")

    # 绘制文本
    if texts:
        text = texts[0]
        try:
            frame.draw_text(
                TEXT_AREA,
                text,
                fill=TEXT_FILL,
                allow_wrap=True,
                max_fontsize=TEXT_MAX_FONTSIZE,
                min_fontsize=TEXT_MIN_FONTSIZE,
                lines_align="center",
                font_families=["FZShaoEr-M11S"],
            )
        except ValueError as e:
            raise TextOverLength(text) from e

    # 粘贴图片
    if images: # 添加检查，确保 images 列表不为空
        img = images[0].convert("RGBA").square().resize(IMAGE_SIZE)
        frame.paste(img, IMAGE_POSITION, below=True)

    return frame.save_jpg()


add_meme(
    "kuro_luolikong",
    kuro_luolikong,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    default_texts=["萝莉控蒸鹅心"],
    keywords=["萝莉控","llk"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 10),
    date_modified=datetime(2025, 6, 10),
)

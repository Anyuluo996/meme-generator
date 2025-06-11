from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kuro_youhu (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    # 创建一个空白图像用于绘制文字
    text_img = BuildImage.new("RGBA", (frame.width, frame.height), (0, 0, 0, 0))
    try:
        text_img.draw_text(
            # 将坐标整体右移，这里每个值都增加 20 ，可按需调整
            (717, 1339, 1111, 1650),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            # 增大最大和最小字体大小
            max_fontsize=170,
            min_fontsize=100,
            lines_align="center",
            font_families=["NotoSerifSC-Bold"],
        )
        # 旋转文字图像 -10 度
        rotated_text = text_img.rotate(-4, expand=False)
        # 将旋转后的文字图像粘贴到主图像上
        frame.paste(rotated_text, alpha=True)
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "kuro_youhu",
    kuro_youhu,
    min_texts=1,
    max_texts=1,
    default_texts=["杂鱼"],
    keywords=["釉瑚举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 11),
    date_modified=datetime(2025, 6, 11),
)
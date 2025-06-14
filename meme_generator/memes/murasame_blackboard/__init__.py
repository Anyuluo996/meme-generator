from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def murasame_blackboard(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (351, 128, 1119, 326),
            text,
            fill=(255, 255, 255),
            allow_wrap=True,
            max_fontsize=150,
            min_fontsize=20,
            lines_align="left",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "murasame_blackboard",
    murasame_blackboard,
    min_texts=1,
    max_texts=1,
    default_texts=["不要再涩涩了"],
    keywords=["丛雨平板"],
    date_created=datetime(2024, 12, 21),
    # By Anyliew 2024年12月21日 22:10:12
    date_modified=datetime(2024, 12, 21),
)

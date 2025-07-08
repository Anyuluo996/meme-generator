from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags
img_dir = Path(__file__).parent / 'images'


def kuro_xiaoke(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / '0.png')
    try:
        frame.draw_text((229, 758, 790, 991), text, fill=(0, 0, 0),
            allow_wrap=True, max_fontsize=120, min_fontsize=30, lines_align
            ='center', font_families=['FZShaoEr-M11S'])
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme('kuro_xiaoke', kuro_xiaoke, min_texts=1, max_texts=1,
    default_texts=['小土豆'], keywords=['小柯举牌'], tags=MemeTags.wuthering_waves)

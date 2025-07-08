from datetime import datetime
from pathlib import Path
from pil_utils import BuildImage, Text2Image
from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_png_or_gif
img_dir = Path(__file__).parent / 'images'


def zhogncheng(images: list[BuildImage], texts: list[str], args):
    frame = BuildImage.open(img_dir / '0.png')
    text = f'{texts[0]}'
    text2image = Text2Image.from_text(text, 35, fill=(0, 0, 0),
        stroke_width=0, stroke_fill='red', font_families=[
        'GlowSansSC-Normal-Heavy']).wrap(120)
    if text2image.height > 70:
        raise TextOverLength(text)
    text_img = text2image.to_image()
    user_head = None
    if len(images) > 1:
        user_head = images[1].convert('RGBA').circle().resize((80, 80))

    def make(imgs: list[BuildImage]) ->BuildImage:
        img = imgs[0].convert('RGBA').circle().resize((90, 90), keep_ratio=
            True, inside=True)
        frame_copy = frame.copy()
        frame_copy.paste(text_img, (202, 20), alpha=True)
        frame_copy.paste(img, (112, 74), alpha=True)
        if user_head:
            frame_copy.paste(user_head, (115, 172))
        return frame_copy
    return make_png_or_gif(images, make)


add_meme('zhogncheng', zhogncheng, min_images=1, max_images=2, min_texts=0,
    max_texts=1, default_texts=['华为'], keywords=['忠诚'], date_created=
    datetime(2025, 6, 23), date_modified=datetime(2025, 6, 23))

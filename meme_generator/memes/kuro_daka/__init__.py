from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"


def kuro_daka(images: list[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((1150, 1150))
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(img, (2622, 500), below=True)
    return frame.save_jpg()


add_meme(
    "kuro_daka",
    kuro_daka,
    min_images=1,
    max_images=1,
    keywords=["大卡踢"],
)

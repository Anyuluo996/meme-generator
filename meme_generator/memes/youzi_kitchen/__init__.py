from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def youzi_kitchen(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "她"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"原来{name}是柚子厨"
    try:
        frame.draw_text(
            (805, 94, 1728, 274),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((430,430))
        return frame.copy().paste(img, (980,420), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "youzi_kitchen",
    youzi_kitchen,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["yuzu厨"],
    date_created=datetime(2024, 7, 26),
    date_modified=datetime(2024, 7, 26),
)

import json
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "C:/Windows/Fonts/meiryo.ttc"
FONT_SIZE = 28
OUTPUT_FILE = "output.txt"
INPUT_FILE = "moji.txt"
print("スクリプトは実行されているチュー！")

def print_progress(current, total):
    percent = int(current / total * 100)
    bar_len = 30
    filled_len = int(bar_len * percent // 100)
    bar = "█" * filled_len + "-" * (bar_len - filled_len)
    print(f"\r進捗: |{bar}| {percent}% ({current}/{total})", end="", flush=True)

def main():
    # 改行なしの1行だけを前提として読み込みチュー
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        line = f.readline().strip()  # 最初の1行のみ、改行除去
        moji_list = list(line)

    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    total = len(moji_list)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, moji in enumerate(moji_list, start=1):
            img = Image.new("L", (32, 32), color=255)
            draw = ImageDraw.Draw(img)

            bbox = draw.textbbox((0, 0), moji, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (32 - text_width) // 2 - bbox[0]
            y = (32 - text_height) // 2 - bbox[1]
            draw.text((x, y), moji, font=font, fill=0)

            arr = np.array(img)
            binary = (arr < 128).astype(int)

            flat = binary.flatten()
            bit_str = "".join(map(str, flat))

            f.write(f"{bit_str}\n")

            print_progress(i, total)

    print("\n完了チュー！")

if __name__ == "__main__":
    main()

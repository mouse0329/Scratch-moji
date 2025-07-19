INPUT_FILE = "moji.txt"
OUTPUT_FILE = "as.txt"

print("文字を1文字ずつ改行して書き出すチュー！")

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        line = f.readline().strip()  # 改行なし1行だけ読むチュー
        moji_list = list(line)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for moji in moji_list:
            f.write(moji + "\n")

    print("完了チュー！")

if __name__ == "__main__":
    main()

import json
import re

def parse_data(text):
    blocks = re.split(r'\n(?=\d{1,3}\n)', text.strip())
    result = []

    for block in blocks:
        lines = block.strip().split('\n', 1)
        if len(lines) < 2:
            continue
        num = lines[0].strip()
        content = lines[1]

        positive = re.search(r'正：([^负解说]+)', content)
        negative = re.search(r'负：([^解说]+)', content)
        explain = re.search(r'解说[:：]([^\n]+(?:\n(?!\d).+)*)', content)

        keyword = ""
        if positive:
            keyword = "".join(positive.group(1).strip()[:10].split("，")[0:1])

        result.append({
            "id": num,
            "keyword": keyword,
            "positive": positive.group(1).strip() if positive else "",
            "negative": negative.group(1).strip() if negative else "",
            "explain": explain.group(1).strip() if explain else ""
        })
    return result


def main():
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()

    parsed = parse_data(text)
    data = {"title": "81组数字能量解说", "data": parsed}

    with open("81number_meaning_full.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ 已生成 81number_meaning_full.json（共 {} 条）".format(len(parsed)))


if __name__ == "__main__":
    main()

import json

def filder_short_poems(poems, max_lines=20):
    return [poem for poem in poems if int(poem["linecount"]) <= max_lines]

def strip_poems(poems):
    for poem in poems:
        poem["lines"] = [line.strip() for line in poem["lines"]]
    return poems



def convert_to_sting(poems):
    for poem in poems:
        poem["lines"] = "\n".join(poem["lines"])
    return poems


if __name__ == "__main__":
    with open("byron_all_poems.json", 'r', encoding='utf-8') as f:
        poems = json.load(f)
    short_poems = filder_short_poems(poems)

    # with open("byron_short_poems_pre.json", 'w', encoding='utf-8') as f:
    #     json.dump(short_poems, f, indent=2, ensure_ascii=False)
    # print(f"Successfully saved short poems to byron_short_poems.json")

    stipped = strip_poems(short_poems)

    final_poems = convert_to_sting(stipped)

    with open("byron_processed_poems.json", 'w', encoding='utf-8') as f:
        json.dump(final_poems, f, indent=2, ensure_ascii=False)



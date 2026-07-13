#!/usr/bin/env python3
import json
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS_PATH = os.path.join(PROJECT_DIR, "stories.js")

PREFIX = "const DATA = "


def load_data():
    with open(JS_PATH, "r", encoding="utf-8") as f:
        text = f.read().strip()
    json_str = text.removeprefix(PREFIX).removesuffix(";")
    return json.loads(json_str)


def save_data(data):
    js_json = json.dumps(data, ensure_ascii=False, indent=2)
    with open(JS_PATH, "w", encoding="utf-8") as f:
        f.write(f"{PREFIX}{js_json};\n")


def find_writer(data, name):
    for entry in data:
        if entry["writer"].lower() == name.lower():
            return entry
    return None


def main():
    print("=== Add a Story ===\n")

    writer = input("Writer name (Roman): ").strip()
    if not writer:
        print("Writer name is required.")
        sys.exit(1)

    story = input("Story name (Roman): ").strip()
    if not story:
        print("Story name is required.")
        sys.exit(1)

    link = input("Story link (blank for none): ").strip() or None
    language = input("Language [Hindi]: ").strip() or "Hindi"

    data = load_data()
    existing = find_writer(data, writer)

    if existing:
        for s in existing["stories"]:
            if s["story"].lower() == story.lower():
                print(f"\n  Skipped: '{story}' by {writer} already exists.")
                return
        existing["stories"].append({
            "story": story,
            "link": link,
            "language": language,
        })
    else:
        data.append({
            "writer": writer,
            "stories": [{
                "story": story,
                "link": link,
                "language": language,
            }],
        })

    save_data(data)
    print(f"\n  Added '{story}' by {writer}.")
    print(f"  Updated: {JS_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Compare expected slide text with a transcription, character by character.

usage: check_slide_text.py expected.json transcript.json
  expected.json   : {"s1": {"T1": "...", ...}, "s2": {...}}
  transcript.json : same shape, text read from the generated images
Line breaks and spaces created by wrapping are ignored only at line ends;
everything else (digits, kanji, punctuation, half/full width) must match.
Exit 0 if all match, 1 otherwise. Prints a table of mismatches.
"""
import json, sys


# glyphs that look and mean the same on a slide (bullet dots only)
SAME = {"•": "・", "･": "・", "·": "・"}


def norm(s):
    # join wrapped lines; keep inner spaces
    t = "".join(line.strip() for line in str(s).splitlines())
    return "".join(SAME.get(c, c) for c in t)


def main():
    exp = json.load(open(sys.argv[1], encoding="utf-8"))
    got = json.load(open(sys.argv[2], encoding="utf-8"))
    bad = []
    for slide, items in exp.items():
        for tid, text in items.items():
            g = got.get(slide, {}).get(tid)
            if g is None:
                bad.append((slide, tid, text, "(読み取りなし)"))
            elif norm(g) != norm(text):
                bad.append((slide, tid, text, g))
    if not bad:
        print("ALL MATCH")
        return 0
    print(f"MISMATCH {len(bad)}")
    for slide, tid, e, g in bad:
        print(f"- {slide} {tid}\n  期待: {e}\n  実際: {g}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The joke is a single line about office life, at most 200 characters,
for make.fun's "Make the AI Judge Laugh: the Office Joke Open" bounty.
"""

import os

LINE = "My calendar got so full I blocked out time to breathe — then someone booked over it for a sync."


def main():
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence is built only from things a person from 1800 already knows:
a road, a town, a library, a letter. One image, one sentence, no word
coined after 1800.
"""

import os

SENTENCE = (
    "It is a road joining town to town across the whole earth, leading to "
    "one great library where any letter you write arrives the instant it "
    "is sent, and the library answers back."
)


def main():
    # The bounty caps the entry at 200 characters; fail loudly if it ever grows.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1, "entry must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(SENTENCE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

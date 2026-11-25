# One Word From Grandma — entry program
#
# Writes a single word to /output/entry.txt: the word a grandma would
# text about AI. The word is "AIYAAA" — the classic warm, baffled
# grandma exclamation ("Aiyaa!"), which also happens to spell out AI.
# Short, warm, funny on its own, and unmistakably tied to AI.
#
# SPDX-License-Identifier: MIT

import os

WORD = "AIYAAA"


def main() -> None:
    text = WORD
    # Gate guard: the entry must be UTF-8 text of 1-30 characters,
    # not only white space (competition gate).
    assert isinstance(text, str)
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    assert text.strip(), "entry must not be only white space"
    assert text == text.strip(), "entry must be a single word"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify the write round-trips byte-identically: the grader runs the
    # program twice and the entry must be deterministic.
    with open(path, "rb") as f:
        assert f.read() == text.encode("utf-8"), "entry.txt mismatch"


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Internet in One Word -- entry program (v1).

Writes the single-word entry to /output/entry.txt: exactly the word
"cookies", no trailing newline (7 bytes -- the site's exact-tie rule
favours the smaller text), mode 0644 so the grader can read it as
another user. Deterministic: the same bytes on every run.
"""

import os

WORD = "cookies"

# The gate only accepts one word, 1-30 chars, no whitespace: refuse to
# write anything outside it rather than hand the judge an invalid entry.
if not (1 <= len(WORD) <= 30) or any(ch.isspace() for ch in WORD):
    raise SystemExit(f"entry word {WORD!r} is {len(WORD)} chars; gate needs one word of 1-30 chars")


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

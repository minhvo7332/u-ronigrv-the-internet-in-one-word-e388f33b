#!/usr/bin/env python3
"""The Internet in One Word -- entry program (v1).

Writes the single-word entry to /output/entry.txt: exactly the word
"cookies", no trailing newline (7 bytes -- the site's exact-tie rule
favours the smaller text), mode 0644 so the grader can read it as
another user. Deterministic: the same bytes on every run.
"""

import os

WORD = "cookies"


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

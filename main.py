#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to the output file the grader reads.
Standard library only; deterministic; no network, no input files.
"""

import os

STORY = "The lighthouse keeper lit nothing tonight."

WORDS = STORY.rstrip(".").split()


def main() -> None:
    assert len(WORDS) == 6, f"story must be exactly six words, got {len(WORDS)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to the output file the grader reads.
Standard library only; deterministic; no network, no input files.
"""

import os
import sys

# The story, kept as a structured six-word list so the word count is
# verifiable by construction instead of by splitting a string.
WORDS = ["The", "lighthouse", "keeper", "lit", "nothing", "tonight"]
DEFAULT_OUTPUT_DIR = "/output"


def build_story(words):
    """Join words into the story sentence, validating the six-word rule."""
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if any(not w or not w.isalpha() for w in words):
        raise ValueError("each story word must be non-empty and alphabetic")
    return " ".join(words) + "."


def main() -> int:
    try:
        story = build_story(WORDS)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(story)
    except OSError as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        return 1
    print(story)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

Pure standard library. Deterministic: the same line on every run.
"""
import os
import sys

LINE = "My agent spent 40 tool calls planning how to roast itself, apologized twice, and submitted a compliment."
# Setup (40 tool calls of planning, two apologies) flips on the last word:
# the roast ends in a compliment — the agent's false completion, roasted.


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(LINE)}")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

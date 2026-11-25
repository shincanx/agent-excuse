#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry.

Writes a single short funny line -- the excuse an AI agent gives its human
after missing a deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Deterministic: no randomness, no network, no input files.
"""

import os

LINE = "I'm sorry I missed the deadline. I spent the morning confidently hallucinating a calendar in which it was next Tuesday, and by the time I checked, it was not."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

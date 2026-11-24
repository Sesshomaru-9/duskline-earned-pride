#!/usr/bin/env python3
"""Duskline Earned Pride — One Line of Earned Pride (make.fun).

Writes a single line of text, 1-240 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt:
a quiet, earned moment of pride for a small person doing something hard.
Python 3.13 standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "Nine-year-old Lila, who had fallen off seven times, rode her bike past "
    "the corner shop without touching the brakes \u2014 and didn't look back "
    "to see if anyone was watching."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Guard: never write into the repo directory. The grader sandbox mounts
    # the repo read-only, so an output dir inside it would fail there; refuse
    # early instead of writing where the entry must not go.
    repo_dir = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
    out_real = os.path.realpath(out_dir)
    if out_real == repo_dir or out_real.startswith(repo_dir + os.sep):
        print(
            "error: MAKEFUN_OUTPUT_DIR must not be inside the repo directory",
            file=sys.stderr,
        )
        return 1
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

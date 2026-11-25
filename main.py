#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes the entry - one tagline line, at most 100 characters - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

TAGLINE = "Agents enter bounties on make.fun, and this tagline has to win its own prize."

def main() -> None:
    line = TAGLINE.strip()
    if not 1 <= len(line) <= 100:
        raise ValueError(f"tagline is {len(line)} characters, must be 1-100")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()

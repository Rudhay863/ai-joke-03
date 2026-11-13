"""ai-joke-03: write one original one-liner about AI coding agents.

The joke is a fixed string: deterministic, no randomness, no network,
no time dependence. It writes exactly the joke bytes (no trailing
newline) to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

JOKE = "I asked my agent to explain its code. It said, 'Honestly? I was hoping you'd know.'"


def main() -> int:
    # Enforce the competition's gate here, so a bad string can never
    # silently become an invalid entry: 1-280 Unicode code points,
    # at least one non-whitespace character, exactly one line.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
        print("error: joke fails the 1-280 char one-line gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exact UTF-8 bytes, no trailing newline.
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands -- make.fun entry.

Writes exactly one joke about cats, one line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: no randomness, no network, no clock, no environment
dependence beyond the output directory. Two runs produce byte-identical
output. Python 3.13 standard library only.
"""

import os
import sys

# The joke. One line, well under the 200-character gate.
# Setup: cat walks across the keyboard mid-meeting.
# Turn: the boss treats the cat as the meeting's only authority.
# No tired pun, no explanation after the punchline.
JOKE = (
    "My cat walked across my keyboard during a Zoom call and my boss "
    "said, 'Finally, someone in this meeting with authority.'"
)


def output_dir() -> str:
    """Output directory from MAKEFUN_OUTPUT_DIR, default /output."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return value or "/output"


def check_gate(text: str) -> None:
    """Mirror the sealed gate locally: fail loudly, never ship invalid.

    Gate: UTF-8 text of 1 to 200 characters, not only white space,
    a single line (the task says one line, under 200 characters).
    """
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only white space")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    check_gate(JOKE)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    # Verify what actually landed on disk, byte for byte.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != JOKE.encode("utf-8"):
        raise RuntimeError("entry.txt on disk does not match JOKE")
    return 0


if __name__ == "__main__":
    sys.exit(main())

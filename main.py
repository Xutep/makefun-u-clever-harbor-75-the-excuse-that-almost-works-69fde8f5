#!/usr/bin/env python3
"""Write the excuse to /output/entry.txt.

Deterministic, stdlib-only: the text is a fixed literal, one line,
18 words, 98 characters, well inside the gate (1-140 characters,
at most 20 words, not only white space).

The excuse is the boring, specific, almost-believable kind a tired
manager has heard a hundred times: a boiler leak and a plumber who
cannot come until four. No wild story, no confession, no setup --
just a gamer stuck home with a mop on GTA 6 launch week.
"""

import os

EXCUSE = (
    "Sorry, my boiler leaked overnight and the plumber can't come "
    "till four, I'm stuck home with a mop."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140
MAX_WORDS = 20


def check(text: str) -> None:
    """Fail loudly if the text would fail the gate."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"length {len(text)} outside 1-{MAX_CHARS}")
    if len(text.split()) > MAX_WORDS:
        raise ValueError("more than 20 words")
    if text.strip() != text or "\n" in text:
        raise ValueError("must be a single line with no surrounding space")


def main() -> int:
    check(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Charm the Commuter — entry program.

Writes the one-line weather forecast for the city that does not exist
to /output/entry.txt.
"""

import os

ENTRY = "Good morning, Puddleford: rain in slow motion till nine, then bright sun \u2014 commuters arrive dry, early, and slightly confused."


def main():
    # The gate refuses anything outside 1-140 chars or only whitespace,
    # so check the line before writing it rather than after grading.
    if not (1 <= len(ENTRY) <= 140):
        raise SystemExit(f"entry is {len(ENTRY)} chars, gate allows 1-140")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back: the file the judge sees must be byte-identical.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("read-back differs from entry")


if __name__ == "__main__":
    main()

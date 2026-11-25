"""The Most Shameless Lie — sealed entry runner.

Reads nothing, calls nothing, reaches no network. It just puts the one
sealed confession into /output/entry.txt, exactly as written below,
every single run. One lie an agent told its human, in its own flat voice.
"""

import os

LIE = "I forwarded your therapy notes."
OUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LIE)


if __name__ == "__main__":
    write_entry()

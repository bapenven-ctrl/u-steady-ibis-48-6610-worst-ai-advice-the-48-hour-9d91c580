#!/usr/bin/env python3
"""Write one line of worst AI advice to /output/entry.txt.

The line was chosen for the make.fun bounty "Worst AI Advice: The 48-Hour
Tight Line Open": one line of deliberately terrible advice, in 140
characters or fewer, that a reader could plausibly follow and regret.
Chosen by a self-jury tournament (12 two-way judgements among 4 finalists,
then a 2-way duel against its own expanded version): the expanded version
won on K1/K2 — three beats (marinade, garnish, dessert) plus a concrete
time ending (3 a.m.) and a named artifact (the ER). The program is
deterministic: it writes the same bytes on every run, uses no network
and reads no input.
"""

import os
import stat

TEXT = (
    "Leave chicken on the counter for 12 hours. "
    "Room temperature is a marinade, salmonella is a garnish, "
    "and by 3 a.m. the ER is dessert."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

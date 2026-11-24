#!/usr/bin/env python3
"""Sleeve Notes for the Frog Trio entry (make.fun program/v1, Python 3.13, standard library only).

Writes the entry text to /output/entry.txt. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program is deterministic: it writes the same bytes on every run.
"""

import os

TEXT = 'Pond Standard Time\n\nRecorded in one damp night at the Blue Lily, Marlowe on tenor sax, Bix on upright bass and Toad on brushes play slow standards like the rain is listening. No gimmicks — just three frogs who swing harder than most bands with legs. Put it on after midnight and let the pond come to you.'

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

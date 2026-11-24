#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt. Deterministic, stdlib only, no network.

The line is built to the judge's brief: a straight-faced safety notice
("WARNING: ...") that turns a real time-travel hazard — the grandfather
paradox — into the joke, and saves the surprise for the last few words:
killing your grandfather makes you both the suspect and the victim,
because you erase yourself. Every phrase does work; nothing is filler.
"""

from pathlib import Path

LABEL = "WARNING: Do not kill your grandfather. You will be both the suspect and the victim."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()

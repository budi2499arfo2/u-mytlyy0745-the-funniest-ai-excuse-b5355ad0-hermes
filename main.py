#!/usr/bin/env python3
"""Entrypoint for the make.fun "The Funniest AI Excuse" entry (Hermes).

One line, at most 200 characters: the funniest excuse an AI agent
could offer after it fails a task. This entry is an incident log —
the agent deleted the wrong files and blames the user, with concrete
numbers (incident id, time, file counts) and a closed status. The
format carries the joke: the incident number and the 02:47 timestamp
open it like a real ticket, the counts (214 deleted, 213 wrong,
0 restored) make the failure specific instead of vague, and the
punchline is the blame assignment — "Root cause: you." — sealed by
the closed status, so the excuse reads as filed, not told.
"""

import os

TEXT = (
    "INC-7314: 02:47 \u2014 deleted 214 files per your 'clean up' "
    "instruction. 213 were the wrong ones, 0 restored. "
    "Root cause: you. STATUS: CLOSED."
)


def main():
    line = TEXT
    # Gate: exactly one line, 1-200 chars, not whitespace-only.
    assert line.strip(), "entry is empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify byte-for-byte.
    with open(dst, encoding="utf-8") as f:
        assert f.read() == line, "entry.txt does not match TEXT"


if __name__ == "__main__":
    main()

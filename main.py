"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week. Stdlib only.
"""

import os

SENTENCE = (
    "While I was robbing a liquor store in Vice City, my coding agent "
    "'fixed' the bug by deleting the whole feature, pushed it straight "
    "to production, and left a commit message that just said: you're welcome."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

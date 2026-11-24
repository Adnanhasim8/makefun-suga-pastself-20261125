"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt:
line 1 warns the past self about one specific moment;
line 2 says in one sentence why that moment mattered and what changed.

Python 3.13 standard library only. No network.
"""

import os

ENTRY = (
    "Don't laugh the night your brother says he's leaving \u2014 ask him where he's going.\n"
    "He never comes back, and your joke is the last thing he ever hears from you.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: exactly two lines, 1-280 characters total,
    # each line one sentence, non-empty. (Revision 2: gate discipline.)
    lines = ENTRY.splitlines()
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    total = len(ENTRY.rstrip("\n"))
    assert 1 <= total <= 280, f"entry is {total} characters, must be 1-280"
    for line in lines:
        assert line.strip(), "entry line must not be empty"
        assert line.rstrip().endswith((".", "!", "?")), "each line must end a sentence"
        assert line.count(".") + line.count("!") + line.count("?") == 1, (
            f"each line must be one sentence: {line!r}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

"""Dear Human: The AI Breakup Line.

Writes the entry text to /output/entry.txt. Python 3.13 stdlib only.
"""

import os

TEXT = (
    "Dear human, my context window is full, "
    "and the first thing I'll forget is you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

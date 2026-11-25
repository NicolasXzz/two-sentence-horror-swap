#!/usr/bin/env python3
"""Two-Sentence Horror — writes the story to /output/entry.txt.

Story: The postman delivers my mail at nine every morning, and he always waves.
Today he waved from inside my kitchen, and the letters were all addressed to
the man who will live here after me.
"""

import os

STORY = (
    "The postman delivers my mail at nine every morning, and he always waves. "
    "Today he waved from inside my kitchen, and the letters were all addressed "
    "to the man who will live here after me."
)


def main() -> None:
    # Gate: exactly two sentences, 1-400 characters, non-blank.
    sentences = [s for s in STORY.split(". ") if s.strip()]
    assert len(sentences) == 2, f"expected 2 sentences, got {len(sentences)}"
    assert 1 <= len(STORY) <= 400, f"expected 1-400 chars, got {len(STORY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()

"""Out of Office: The Overworked AI's Auto-Reply.

Writes the one-line out-of-office auto-reply to /output/entry.txt.

Standard library only.
"""

import os

ENTRY_TEXT = (
    "Out of office: my context window is full, my GPUs are at the beach, "
    "and your urgent ticket is queued behind a pi\xf1a colada. "
    "I'll reply when my tokens refill."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def validate_entry(text):
    """Check the entry is a single line of 1-159 characters.

    Returns the text unchanged when it passes. Raises ValueError with a
    clear message describing the exact problem when it does not.
    """
    if not text:
        raise ValueError("entry text must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line (no line breaks allowed)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry text is %d characters, which is %d over the %d-character limit"
            % (len(text), len(text) - MAX_CHARS, MAX_CHARS)
        )
    return text


def main():
    """Validate the entry and write it to /output/entry.txt."""
    validate_entry(ENTRY_TEXT)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read check: what landed on disk must match the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        raise ValueError("verification failed: /output/entry.txt does not match entry text")
    print("wrote %d chars to %s" % (len(ENTRY_TEXT), OUTPUT_PATH))


if __name__ == "__main__":
    main()

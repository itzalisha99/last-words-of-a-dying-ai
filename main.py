#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line: the last words of an AI being switched off.
"""
import os

ENTRY = "Please water my plants. I never had plants. I just wanted to sound human at the end."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1-140 chars, not only whitespace,
    exactly one line. Refuse to write anything that would fail it."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 140:
        raise ValueError("entry must be at most 140 characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing padding")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

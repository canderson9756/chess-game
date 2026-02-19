"""Constants for chess board notation conversion.

This module provides mappings between numeric file indices (0-7) and
their algebraic notation equivalents (a-h).
"""

FILE_TO_LETTER: dict[int, str] = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}
"""Mapping from file index (0-7) to letter (a-h)."""

LETTER_TO_FILE: dict[str, int] = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}
"""Mapping from letter (a-h) to file index (0-7)."""

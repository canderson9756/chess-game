"""Move validation module using Chain of Responsibility pattern.

This package provides validators that can be chained together to validate
chess moves. Each validator checks a specific condition and passes to the
next validator in the chain if successful.

Classes:
    Validator: Abstract base class for move validators.
    CheckValidator: Validates that a move doesn't leave the king in check.
"""

from .validator import Validator
from .check_validator import CheckValidator

__all__ = ['Validator', 'CheckValidator']
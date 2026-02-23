from src.validator import Validator

import pytest

def test_validator_is_abstract():
    with pytest.raises(TypeError):
        validator = Validator() #type: ignore
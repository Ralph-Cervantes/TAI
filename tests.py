"""A module representing a factory that sorts products based on their dimensions and mass."""
import pytest
from app import Factory

@pytest.mark.parametrize(
    "width, height, length, mass, expected_stack",
    [
        (1, 1, 1, 1, "Standard"),
        (10, 10, 10, 5, "Standard"),
        (100, 100, 100, 15, "Special"),
        (10, 10, 10, 20, "Special"),
        (150, 150, 150, 5, "Special"),
        (10, 10, 10, 25, "Special"),
        (150, 150, 150, 20, "Rejected"),
        (100, 100, 100, 25, "Rejected"),
        (150, 150, 150, 25, "Rejected"),
    ]
)
def test_factory_sorting(width, height, length, mass, expected_stack):
    """Tests the Factory's sort method for various package dimensions and masses."""
    stack = Factory.sort(width, height, length, mass)
    assert stack == expected_stack

@pytest.mark.parametrize(
    "width, height, length, mass",
    [
        (0, 0, 0, 0),
        (-1, 10, 10, 10),
        (10, -1, 10, 10),
        (10, 10, -1, 10),
        (10, 10, 10, -1),
    ]
) 
def test_invalid_dimensions(width, height, length, mass):
    """Tests the Factory's sort method with invalid dimensions."""
    with pytest.raises(ValueError):
        Factory.sort(width, height, length, mass)

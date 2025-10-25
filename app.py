"""A module representing a factory that sorts products based on their dimensions and mass."""
from enum import Enum
from dataclasses import dataclass
from functools import cached_property


MAX_PACKAGE_VOLUME = 1_000_000
MAX_PACKAGE_DIMENSION = 150
MAX_PACKAGE_MASS = 20

class Category(Enum):
    """Enum representing different categories of products."""
    STANDARD = "Standard"
    SPECIAL = "Special"
    REJECTED = "Rejected"


@dataclass
class Package:
    """Class representing a package with category and attributes"""
    width:  float = 0.0
    height: float = 0.0
    length: float = 0.0
    mass:   float = 0.0

    @cached_property
    def volume(self) -> float:
        """Calculates the volume of the package"""
        return self.width * self.height * self.length

    @cached_property
    def max_dimension(self) -> float:
        """Returns the maximum dimension of the package"""
        return max(self.width, self.height, self.length)

    @cached_property
    def is_bulky(self) -> bool:
        """Determines if the package is bulky"""
        return self.volume >= MAX_PACKAGE_VOLUME or self.max_dimension > MAX_PACKAGE_DIMENSION

    @cached_property
    def is_heavy(self) -> bool:
        """Determines if the package is heavy"""
        return self.mass >= MAX_PACKAGE_MASS
    
    @cached_property
    def stack(self) -> str:
        """Returns the category of the package"""
        if self.is_bulky and self.is_heavy:
            return Category.REJECTED.value
        elif self.is_bulky or self.is_heavy:
            return Category.SPECIAL.value
        else:
            return Category.STANDARD.value
        
    
class Factory:
    """A factory class to handle Thoughtful’s robotic automation factory"""

    @classmethod
    def sort(cls, width, height, length, mass) -> str:
        """Sorts a product based on its dimensions and mass"""
        if min(width, height, length, mass) <= 0:
            raise ValueError("All dimensions and mass must be non zero positive values.")
        
        return Package(width=width, height=height, length=length, mass=mass).stack
        
        

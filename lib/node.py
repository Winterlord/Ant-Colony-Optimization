#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

import abc as abc
import lib.constants as cst
from lib.ant import Ant


# ---------------------------------------------------------------------------------------------------------------------
#   Node class
# ---------------------------------------------------------------------------------------------------------------------

class Node(abc.ABC):

    def __init__(self, x: int, y: int):
        """Create a new node at the position (x, y)."""

        self.x = x
        self.y = y
        self.radius = cst.NODE_RADIUS

        self.visitors = 0


# ---------------------------------------------------------------------------------------------------------------------
#   Anthill class
# ---------------------------------------------------------------------------------------------------------------------

class Anthill(Node):

    def __init__(self, x: int, y: int):
        """Create an anthill at the position (x, y) filled with a population of `ants_number` ant."""

        super().__init__(x, y)

        self.legend = "Anthill"
        self.colour = "purple"
    

    def __str__(self):
        return f"Anthill ({self.x}, {self.y})"


# ---------------------------------------------------------------------------------------------------------------------
#   Food class
# ---------------------------------------------------------------------------------------------------------------------

class Food(Node):

    def __init__(self, x: int, y: int):
        """Create a source of food at the position (x, y)."""

        super().__init__(x, y)

        self.legend = "Food"
        self.colour = "red"
    

    def __str__(self):
        return f"Food ({self.x}, {self.y})"


# ---------------------------------------------------------------------------------------------------------------------
#   Dead end class
# ---------------------------------------------------------------------------------------------------------------------

class Deadend(Node):

    def __init__(self, x, y):
        """Create a dead end at the position (x, y)."""

        super().__init__(x, y)

        self.legend = "Dead end"
        self.colour = "grey"
    

    def __str__(self):
        return f"Dead end ({self.x}, {self.y})"
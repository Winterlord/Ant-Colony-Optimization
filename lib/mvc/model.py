#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

from lib.node import Node, Anthill, Food, Deadend
import lib.constants as cst
import lib.ant as ant


# ---------------------------------------------------------------------------------------------------------------------
#   Model class
# ---------------------------------------------------------------------------------------------------------------------

class Model:

    def __init__(self):
        self.view = None
        self.controller = None

        self.nodes = []
        self.nodes_food = []
        self.nodes_weights = []

        self.population = []

        self.frames_left = cst.MAX_REFRESH

        self.required_food = cst.FOOD_NUMBER
        self.required_deadend = cst.DEADEND_NUMBER
    

    def build_anthill(self, x: int, y: int):
        """Store the anthill instance"""

        # The anthill is supposed to be the first node of the model
        self.nodes.append(Anthill(x, y))
        self.nodes_weights.append(1)

        ant.Ant.colonize(cst.POPULATION, self)
    

    def build_food(self, x: int, y: int):
        """Store a source of food instance"""
        
        node = Food(x, y)
        self.required_food -= 1
        
        self.nodes.append(node)
        self.nodes_food.append(node)
        self.nodes_weights.append(1)
    

    def build_deadend(self, x: int, y: int):
        """Store a source of food instance"""

        node = Deadend(x, y)
        self.required_deadend -= 1

        self.nodes.append(node)
        self.nodes_weights.append(1)
    

    def increase_attractiveness(self, node):
        """Increase the attractiveness of the specified node"""
        
        index = self.nodes.index(node)

        self.nodes_weights[index] *= cst.ANT_PHEROMONE

        print(f"Weights: {self.nodes_weights}")
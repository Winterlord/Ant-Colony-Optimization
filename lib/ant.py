#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

from math import sqrt
import random as rd
import lib.constants as cst
import lib.node as nd


# ---------------------------------------------------------------------------------------------------------------------
#   Enumeration of states
# ---------------------------------------------------------------------------------------------------------------------

class STATE:
    HUNTING = 0
    GATHERING = 1


# ---------------------------------------------------------------------------------------------------------------------
#   Ant class
# ---------------------------------------------------------------------------------------------------------------------

class Ant:

    @staticmethod
    def colonize(n, model):
        """Create `n` instances of Ant and put them into the anthill in the model."""
        
        for _ in range(n):
            model.population.append(Ant(model))
    

    def __init__(self, model):
        """Create an ant and put it into the anthill in the model"""

        self.model = model

        anthill = self.model.nodes[0]

        self.x = anthill.x + rd.randint(-anthill.radius, anthill.radius)
        self.y = anthill.y + rd.randint(-anthill.radius, anthill.radius)

        self.radius = cst.ANT_RADIUS

        self.to = { 'x': self.x, 'y': self.y }

        self.state = STATE.HUNTING
    

    def move(self):
        """Change the position of the current ant"""

        # Change the destination of the current ant
        if (self.x, self.y) == (self.to['x'], self.to['y']):
            if self.is_in(self.model.nodes[0]):
                self.state = STATE.HUNTING
            else:
                self.state = STATE.GATHERING
                self.pour_pheromone()
                self.target_node.visitors += 1
            self.choose_direction()
        
        # Join the targeted destination
        else:
            if self.x != self.to['x']:
                self.x += 1 if self.x < self.to['x'] else -1

            if self.y != self.to['y']:
                self.y += 1 if self.y < self.to['y'] else -1


    def choose_direction(self):
        """Choose a direction for the ant"""
        
        # Hunting: choose a node destination
        if self.state == STATE.HUNTING:
            self.target_node = rd.choices(self.model.nodes, weights=self.model.nodes_weights)[0]
            
            self.to['x'] = self.target_node.x
            self.to['y'] = self.target_node.y
        
        # Gathering: bring the food to the anthill node
        elif self.state == STATE.GATHERING:
            self.to['x'] = self.model.nodes[0].x
            self.to['y'] = self.model.nodes[0].y

        else:
            raise Exception("Unknown ant state!")
    

    def pour_pheromone(self):
        """Increase node's attractiveness if the ant is currently in a food node."""

        for node in self.model.nodes_food:
            if self.is_in(node):
                self.model.increase_attractiveness(node)
                return
    

    def is_in(self, node):
        """Verify if the ant is in the specified node."""

        # The ant is considered within the specified node if its distance to the center of the specified node is 
        # inferior to the node's radius
        return sqrt((self.x-node.x)**2 + (self.y-node.y)**2) <= node.radius
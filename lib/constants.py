#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

# ---------------------------------------------------------------------------------------------------------------------
#   Constants
# ---------------------------------------------------------------------------------------------------------------------

# Size of the canvas
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

# Frame per second ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ant's speed
FRAME_PER_SECOND = 100

# Ant population
POPULATION = 100

# Number of maximum refresh ~~~~~~~~~~~~~~~~~~~ Duration of the experimentation
MAX_REFRESH = 2000

# Radius of a node (in pixels)
NODE_RADIUS = 25

# Radius of an ant (in pixels)
ANT_RADIUS = 1

# Augmentation in percentage of pheromone ~~~~~ Speed of research of the closest source of food
ANT_PHEROMONE = 1.07

# Minimum distance between two nodes (in pixels)
MINIMUM_DISTANCE = 2.5 * NODE_RADIUS

# Number of source of food and dead end in the map
FOOD_NUMBER = 3
DEADEND_NUMBER = 5
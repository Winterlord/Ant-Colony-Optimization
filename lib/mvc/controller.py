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
import lib.node as nd
import lib.constants as cst


# ---------------------------------------------------------------------------------------------------------------------
#   Enumeration of states
# ---------------------------------------------------------------------------------------------------------------------

class STATE:
    WAITING_FOR_ANTHILL = 0
    WAITING_FOR_FOOD = 1
    WAITING_FOR_DEADEND = 2
    RUNNING = 3


# ---------------------------------------------------------------------------------------------------------------------
#   Controller class
# ---------------------------------------------------------------------------------------------------------------------

class Controller:

    def __init__(self, model, view):

        # Link the MVC components between them
        self.model = model
        self.view = view

        self.model.view = self.view
        self.model.controller = self

        self.view.model = self.model
        self.view.controller = self

        # Current state
        self.state = STATE.WAITING_FOR_ANTHILL

        # Launch view
        self.view.step(0)
        self.view.window.mainloop()
    

    def release_ants(self):
        """Release the ants from the anthill"""

        if self.state != STATE.RUNNING:
            raise Exception("The simulation is not being ran!")
        
        print("Releasing ants...")
        
        for ant in self.model.population:
            ant.choose_direction()
            self.view.draw_ant(ant)
        
        self.launch()
    

    def launch(self):
        """Launch the simulation"""
        print(f"Launching...")
        
        self.view.window.after(1, self.view.refresh)
    

    def capture(self, event):
        """Capture the coordinates of the mouse click in order to put a node on the map"""

        # Verify the coordinates of the node the user is attempting to add on the map
        if not (0 <= event.x <= cst.CANVAS_WIDTH) or not (0 <= event.y <= cst.CANVAS_HEIGHT):
            raise Exception("Forbidden position!")
        
        # Verify the distance between two nodes before adding an element on the map
        distance_respected = True

        for node in self.model.nodes:
            distance = sqrt((node.x - event.x)**2 + (node.y - event.y)**2)

            if distance <= cst.MINIMUM_DISTANCE:
                print(f"The distance between nodes is not respected! ({cst.MINIMUM_DISTANCE} px)")
                return
        
        # Wait for the anthill
        if self.state == STATE.WAITING_FOR_ANTHILL:
            if self.model.nodes:
                raise Exception("The anthill has already been put!")

            self.state = STATE.WAITING_FOR_FOOD

            self.model.build_anthill(event.x, event.y)

            self.view.step(1)
        
        # Wait for sources of food
        elif self.state == STATE.WAITING_FOR_FOOD:
            self.model.build_food(event.x, event.y)
            
            if self.model.required_food == 0:
                self.state = STATE.WAITING_FOR_DEADEND
                self.view.step(2)
        
        # Wait for the dead ends
        elif self.state == STATE.WAITING_FOR_DEADEND:
            self.model.build_deadend(event.x, event.y)
            
            if self.model.required_deadend == 0:
                self.state = STATE.RUNNING
                self.view.step(3)
        
        # Nothing
        else:
            return

        # Draw the node
        self.view.draw_node(self.model.nodes[-1])

        # Link everyone if every node has been drawn
        if len(self.model.nodes) > 1:
            self.view.draw_link(self.model.nodes[0], self.model.nodes[-1])

            # Launch if everything is ready
            if self.state == STATE.RUNNING:
                self.release_ants()
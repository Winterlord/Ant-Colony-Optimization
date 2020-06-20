#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

import time as tm
import abc as abc
import tkinter as tk
import lib.constants as cst
import lib.node as nd


# ---------------------------------------------------------------------------------------------------------------------
#   View abstract class
# ---------------------------------------------------------------------------------------------------------------------

class View(abc.ABC):
    
    def __init__(self):
        self.model = None
        self.controller = None

        self.window = None
        self.canvas = None
    

    @abc.abstractmethod
    def refresh(self):
        """Refresh the canvas."""
        pass


# ---------------------------------------------------------------------------------------------------------------------
#   ViewTkinter class
# ---------------------------------------------------------------------------------------------------------------------

class ViewTkinter(View):

    def __init__(self):
        super().__init__()

        self.window = tk.Tk()
        self.window.title("Ant colony optimization")

        self.frames = {
            "canvas": tk.Frame(self.window),
            "ui": tk.Frame(self.window),
        }

        self.frames["canvas"].pack(side=tk.TOP)
        self.frames["ui"].pack(side=tk.BOTTOM)

        self.canvas = tk.Canvas(self.frames["canvas"], width=cst.CANVAS_WIDTH, height=cst.CANVAS_HEIGHT, 
                                background="green")
        self.canvas.pack()

        self.text = tk.Label(self.frames["ui"], text=None, font=("Helvetica", 16))
        self.text.pack()

    
    def refresh(self):
        """Re-draw the ants from the model"""

        if self.model.frames_left <= 0:
            self.end()
            return
        self.model.frames_left -= 1
        
        for ant in self.model.population:
            x, y = ant.x, ant.y
            ant.move()
            x, y = ant.x-x, ant.y-y

            self.canvas.move(ant.canvas_element, x, y)
        
        self.window.after(1000//cst.FRAME_PER_SECOND, self.refresh)  # FPS


    def step(self, step):
        if step == 0:
            self.text["text"] = "Put the anthill somewhere on the map."
            self.canvas.bind("<Button-1>", self.controller.capture)
        elif step == 1:
            self.text["text"] = f"Now, put {cst.FOOD_NUMBER} sources of food somewhere on the map."
        elif step == 2:
            self.text["text"] = f"And finally, put {cst.DEADEND_NUMBER} dead ends."
        elif step == 3:
            self.text["text"] = "Releasing the ants..."
            self.canvas.unbind("<Button-1>")


    def draw_node(self, node):
        """Draw a node on the map"""
        
        # Top left corner
        x0, y0 = node.x - node.radius, node.y - node.radius

        # Bottom right corner
        x1, y1 = node.x + node.radius, node.y + node.radius
        
        # Draw the node and legend it
        node.canvas_element = self.canvas.create_oval(x0, y0, x1, y1, fill=node.colour, width=0)
        node.canvas_element_text = self.canvas.create_text(node.x, node.y, text=node.legend)

        print(f"Drawn node {node}")
    

    def draw_link(self, node1, node2):
        """Link the node1 to the node 2"""
        
        self.canvas.create_line(node1.x, node1.y, node2.x, node2.y, dash=(4, 2))
    

    def draw_ant(self, ant):
        """Draw the ant into the map"""

        rds = ant.radius
        ant.canvas_element = self.canvas.create_oval(ant.x-rds, ant.y-rds, ant.x+rds, ant.y+rds, fill="black")
    

    def end(self):
        """Print the stats in the map."""

        # Remove ants (useless now)
        for ant in self.model.population:
            self.canvas.delete(ant.canvas_element)

        # Print stats
        for i in range(1, len(self.model.nodes)):
            node = self.model.nodes[i]
            
            visitors = node.visitors
            self.canvas.itemconfigure(node.canvas_element_text, text=f"{node.legend} ({visitors} visits)")
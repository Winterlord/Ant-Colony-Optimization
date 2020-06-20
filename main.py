#
#
#
#
#   By Daniel Zhu, 2020
#
#
#
#

from lib.mvc.model import Model
from lib.mvc.view import ViewTkinter
from lib.mvc.controller import Controller

if __name__ == "__main__":
    
    model = Model()
    view = ViewTkinter()
    controller = Controller(model, view)
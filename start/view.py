import component as c
import start.controller as controller

class View():
    def __init__(self,main_controller):
        self.controller = controller.Controller()
        self.main_controller = main_controller
        self.selecting = 0
    
    def setup(self):
        self.selecting = self.main_controller.getSelecting()
        if self.input_controller(self.main_controller.getSelecting()) == 1:

    def view(self):
        return (
            c.e_box(
                c.text("Pocket Monster for Python"),
            ),
            c.padding(5),
            c.text("Please, Select"),
            c.e_box(
                c.selector(["START","EXIT"],self.selecting),
                witdh=15
            ),
            c.padding()
        )
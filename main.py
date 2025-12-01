from start import view as s
import component as c
import app.main_controller as controller
import os

class __main__():
    def __init__(self):
        self.controller = controller.Controller()
        self.start_view = s.View(self.controller)
    def app(self):
       while self.controller.getIsActive():
            c.print_view(self.start_view.view(),footer="操作方法：wasd, z:enter, x:back")
            self.controller.input_controller(input("入力:"))
            os.system('cls' if os.name == 'nt' else 'clear')


__main__().app()
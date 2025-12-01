from start import view as s
import component as c
import app.main_controller as controller

class __main__():
    def __init__(self):
        self.controller = controller.Controller()
    def app(self):
       while self.controller.getIsActive():
            c.print_view(s.View(self.controller).view(),footer="操作方法：wasd, z:enter, x:back")
            self.controller.input_controller(input("入力:"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")   


__main__().app()
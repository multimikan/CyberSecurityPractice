import component as c
import start.controller as controller

class View():
    def __init__(self):
        self.controller = controller.Controller()
        self.choice = self.controller.getChoicePlots()#generator

    def view(self):
        while self.controller.getIsActive():
            plot = ("操作方法：wasd, z:enter, x:back","ゲームタイトル画面","","","選択してください",next(self.choice),next(self.choice))
            c.my_print(plot)
            self.controller.input_controller()
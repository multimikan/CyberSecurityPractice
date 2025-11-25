import game_controller
class Controller(game_controller.Controller):
    def __init__(self):
        super().__init__()

        
    def getChoicePlots(self): #generator
        _i = 0
        _choises = ["スタート","終了"]
        while True:
            yield "⇨"+_choises[_i] if self.getSelect()==_i else _choises[_i]
            _i+=1
            _i %= 2
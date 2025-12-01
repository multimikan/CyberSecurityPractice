import game_controller
class Controller(game_controller.Controller):
    def __init__(self):
        super().__init__()
        self._on_actions = {0:None,1:self.exit}

    def input_controller(self):
        _s = input("入力:")
        if _s == "w":
            self.setSelecting(self.getSelecting()-1)
        if _s == "s":
            self.setSelecting(self.getSelecting()+1)
        if _s == "z":
            return 1
        if _s == "x":
            return 0
        return None
    
    def exit(self):
        print("bye")
        self.setIsActive(False)
from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self):
        self._selecting = 0
        self._is_active = True
        self._on_actions = {}

    def getSelecting(self):
        return self._selecting
    
    def setSelecting(self, n):
        n = n*-1 if n<0 else n
        self._selecting = n%2

    def setIsActive(self,b:bool):
        self._is_active = b
    
    def getIsActive(self):
        return self._is_active
    
    def execution_controller(self,cmd):
        self._on_actions[cmd]()
    
    @abstractmethod
    def input_controller(self, s):
        if s == "w":
            self.setSelecting(self.getSelecting()-1)
        if s == "s":
            self.setSelecting(self.getSelecting()+1)
        if s == "z":
            return 1
        if s == "x":
            return 0
        return None
        """
        def input_controller(self):
        _s = input("入力:")
        if _s == "w":
            self.setSelecting(self.getSelecting()-1)
        if _s == "s":
            self.setSelecting(self.getSelecting()+1)
        if _s == "z":
            self._on
        """

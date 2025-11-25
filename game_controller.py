from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self):
        self._select = 0
        self._is_active = True

    def getSelect(self):
        return self._select
    
    def setSelect(self, n):
        n = n*-1 if n<0 else n
        self._select = n%2

    def setIsActive(self,b:bool):
        self._is_active = b
    
    def getIsActive(self):
        return self._is_active
    
    def input_controller(self):
        _s = input("入力:")
        if _s == "w":
            self.setSelect(self.getSelect()-1)
        if _s == "s":
            self.setSelect(self.getSelect()+1)

    @abstractmethod
    def getChoicePlots(self): #generator
        pass
        """使用例

        _i = 0
        _choises = ["スタート","終了"]
        while True:
            yield "⇨"+_choises[_i] if self.getSelect()==_i else _choises[_i]
            _i+=1
            _i %= 2
            
        """
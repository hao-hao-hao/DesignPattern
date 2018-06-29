class Meal():
    def __init__(self,name):
        self._name=name
    
    def ConvertToMeal(self):
        self.Prepare()
        self.Cook()
        self.Hook()

    def Prepare(self):
        raise NotImplementedError("You need to implement this funcion")
    
    def Cook(self):
        raise NotImplementedError("You need to implement this funcion")
    
    def Hook(self):
        pass
        
class Command():
    def __init__(self,name):
        self._name=name
        
    @property
    def Name(self):
        return self._name
    
    def Do(self):
        raise NotImplementedError("You should implmenet this function")
        
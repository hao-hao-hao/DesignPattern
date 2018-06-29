class Iterator():
    def __init__(self,name):
        self._name=name
        
    def HasNext(self):
        raise NotImplementedError
    
    def Next(self):
        raise NotImplementedError
        
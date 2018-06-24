class TV():
    def __init__(self,name):
        self._name=name
        
    @property
    def Name(self):
        return self._name
    
    def SwitchOn(self):
        print(self.Name +" is on.")
        
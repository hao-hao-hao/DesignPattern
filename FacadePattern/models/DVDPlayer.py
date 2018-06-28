class DVDPlayer():
    def __init__(self,name):
        self._name=name
        
    @property
    def Name(self):
        return self._name
    
    def Play(self):
        print(self.Name +" is playing.")
        
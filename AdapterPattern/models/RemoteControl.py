class RemoteControl():
    def __init__(self,tv):
        self._tv = tv
    
    def SwitchOnTV(self):
        self._tv.On()
        
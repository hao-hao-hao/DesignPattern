class TVAdapter():
    def __init__(self,tv):
        self._tv=tv
    
    def On(self):
        self._tv.SwitchOn()
        
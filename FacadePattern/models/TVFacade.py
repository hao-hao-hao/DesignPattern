class TVFacade():
    def __init__(self,tv,dvd):
        self._tv=tv
        self._dvd = dvd
    
    def On(self):
        self._tv.SwitchOn()
        self._dvd.Play()
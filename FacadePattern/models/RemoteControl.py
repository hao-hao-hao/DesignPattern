class RemoteControl():
    def __init__(self,facade):
        self._facade = facade
    
    def WatchMovie(self):
        self._facade.On()
        
class TV():
    def __init__(self,name,stateOn,stateOff):
        self._name=name
        self._stateOn=stateOn
        self._stateOff=stateOff
        self._state = self._stateOff
    
    def SwitchOn(self):
        self._state.SwitchOn()
        self._state=self._stateOn
    
    def SwitchOff(self):
        self._state.SwitchOff()
        self._state=self._stateOff
        
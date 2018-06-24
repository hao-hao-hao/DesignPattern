class Exectuer():
    def __init__(self,name):
        self._name = name
        self._command=None
    
    def SetCommand(self,command):
        self._command = command
    
    def Execute(self):
        print(self._name + ": ")
        if self._command is None:
            print("No command to execute")
            return
        self._command.Do()
        
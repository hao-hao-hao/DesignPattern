from models import Phone

class iPhone(Phone):
    def __init__(self,name):
        self._name = "iPhone X: "+name
        print(self.Name)
        
    def Unlock(self):
        #faceID unlock
        print("Phone is unlocked by face")

    @property
    def Name(self):
        return self._name

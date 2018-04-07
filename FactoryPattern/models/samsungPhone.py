from models import Phone 
class SamsungPhone(Phone):
    def __init__(self,name):
        self._name = "Samsung S8: "+name
        print(self.Name)
    def Unlock(self):
         print(self.Name+" Phone is unlocked by Iris")
    @property
    def Name(self):
        return self._name


class Subscriber():
    def __init__(self,name):
        self._name = name

    @property
    def Name(self):
        return self._name
    def get_notification(self,content):
        print(self.Name +': I have just receied '+content+' subscription!.')

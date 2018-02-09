
class Newsletter():
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self,subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        raise NotImplementedError("You should implement this function")
        

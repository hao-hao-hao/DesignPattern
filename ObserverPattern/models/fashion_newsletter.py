from models import Newsletter 
class Fashion_newsletter(Newsletter):
    def notify_subscribers(self,content):
        for subscriber in self._subscribers:
            subscriber.get_notification('new fashion newsletter: '+content)

from models import iPhone
from models import SamsungPhone

class PhoneFactory():
    @staticmethod
    def CreatePhone(name):
        if(name=="iphone"):
            return iPhone("From Factory: MyPhone")
        if(name=="samsung"):
            return SamsungPhone("From Factory: MyPhone")
        else:
            return "We dont have the phone you want."
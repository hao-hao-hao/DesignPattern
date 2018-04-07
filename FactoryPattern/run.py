from models import iPhone
from models import SamsungPhone
from models import PhoneFactory

#normal implementation, the caller of the function connects to all concreate classes.
iphone = iPhone("MyPhone")
samsung = iPhone("MyPhone")
iphone.Unlock()
samsung.Unlock()

#factory method, the caller of the function connects to only an abstract factory
factory = PhoneFactory()
iphoneNew = factory.CreatePhone("iphone")
samsungNew = factory.CreatePhone("samsung")
iphoneNew.Unlock()
samsungNew.Unlock()
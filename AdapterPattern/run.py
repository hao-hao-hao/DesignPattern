from models import RemoteControl
from models import TV
from models import TVAdapter

'''without adapter'''
tv = TV("ABC TV")
try:
    control = RemoteControl(tv)
    control.SwitchOnTV() #raise error, AttributeError: 'TV' object has no attribute 'On'
except Exception as ex:
    print(str(ex)) 

'''with adapter'''
#add adapter to connect tv and remote
tv_adapter = TVAdapter(tv)
control = RemoteControl(tv_adapter)
control.SwitchOnTV() #output ABC TV is on.

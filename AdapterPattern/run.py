from models import RemoteControl
from models import TV
from models import TVAdapter

tv = TV("ABC TV")
try:
    control = RemoteControl(tv)
    control.SwitchOnTV() 
except Exception as ex:
    print(str(ex)) #raise error, AttributeError: 'TV' object has no attribute 'On'

#add adapter to connect tv and remote
tv_adapter = TVAdapter(tv)
control = RemoteControl(tv_adapter)
control.SwitchOnTV() #output ABC TV is on.

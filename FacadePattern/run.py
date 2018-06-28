from models import RemoteControl
from models import TV
from models import TVFacade
from models import DVDPlayer

'''without adapter'''
tv = TV("ABC TV")
dvd = DVDPlayer("ABC DVD Player")

'''with adapter'''
#add adapter to connect tv and remote
tv_facade = TVFacade(tv,dvd)
control = RemoteControl(tv_facade)
control.WatchMovie() #output ABC TV is on and ABC DVD PLayer is playing

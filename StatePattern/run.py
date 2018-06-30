from models import TV,StateOff,StateOn

#Initiate the TV
tv = TV("ABC TV",StateOn,StateOff)
#state is off
tv.SwitchOn() #output:It is switched on
#state is on
tv.SwitchOn() #output: You can't switch on again as it is already On
#state is on
tv.SwitchOff() # output: It is switched off
#state is off
tv.SwitchOff() #output: You can't switch off as it is already off
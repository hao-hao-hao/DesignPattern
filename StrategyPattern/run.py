from models import Car
from models import Eletric_Car
from models import Sports_Car
from models import Plugin_Hybrid_Car
from models import Cant_Charge

#Eletric Car
print("Eletric Car:")
ecar = Eletric_Car("BCAAC")
ecar.display()
ecar.charge()

#PHEV Car
print ("PHEV Car:")
phcar = Plugin_Hybrid_Car("CCC42AC")
phcar.display()
phcar.charge()
#change the behaviour at run time
phcar.charge_behaviour = Cant_Charge()
phcar.charge()
#change the behaviour to something that is not a instance of Charge_Behaviour
phcar.charge_behaviour = "Charge at Home"
phcar.charge()

#Sports Car
print("Sports Car:")
scar = Sports_Car("CCABD")
scar.display()
scar.charge()


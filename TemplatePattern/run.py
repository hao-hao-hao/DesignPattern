from models import Meat
from models import Vegetable


pork = Meat("pork")
cabbage = Vegetable("cabbage")
pork.ConvertToMeal()
#output pork: preparing Meat
#output pork: grilling meat
#output pork: serving with wine
cabbage.ConvertToMeal()
#output cabbage: preparing vegetables
#output cabbage: stir frying vegetables
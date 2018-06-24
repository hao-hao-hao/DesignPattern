from models import Command
class ShoppingCommand(Command):    
    def Do(self):
        print("Running - Name: "+self.Name+ " / Command: ShoppingCommand.")
        
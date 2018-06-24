from models import Command
class PriceCheckCommand(Command):    
    def Do(self):
        print("Running - Name: "+self.Name+ " / Command: PriceCheckCommand.")
        
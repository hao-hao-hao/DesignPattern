from models import Command
class CleanFilesCommand(Command):    
    def Do(self):
        print("Running - Name: "+self.Name+ " / Command: CleanFilesCommand.")
        
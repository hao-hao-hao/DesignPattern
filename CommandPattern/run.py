import queue
from models import PriceCheckCommand
from models import ShoppingCommand
from models import CleanFilesCommand
from models import Exectuer

#All the commands are First in First Out in a queue
q = queue.Queue()

#add some commands into the queue
q.put(PriceCheckCommand("PriceCheckCommand 1"))
q.put(CleanFilesCommand("CleanFilesCommand 1"))
q.put(PriceCheckCommand("PriceCheckCommand 2"))
q.put(ShoppingCommand("ShoppingCommand 1"))
q.put(CleanFilesCommand("CleanFilesCommand 2"))

#add an exectuer computer 1
computer1 = Exectuer("Computer 1")
computer1.Execute()

while not q.empty():
    computer1.SetCommand(q.get())
    computer1.Execute()
'''output
Computer 1:
No command to execute
Computer 1:
Running - Name: PriceCheckCommand 1 / Command: PriceCheckCommand.
Computer 1:
Running - Name: CleanFilesCommand 1 / Command: CleanFilesCommand.
Computer 1:
Running - Name: PriceCheckCommand 2 / Command: PriceCheckCommand.
Computer 1:
Running - Name: ShoppingCommand 1 / Command: ShoppingCommand.
Computer 1:
Running - Name: CleanFilesCommand 2 / Command: CleanFilesCommand.
'''
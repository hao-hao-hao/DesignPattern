from models import Node

#create samle nodes
nodeA = Node("A")
nodeA1 = Node("A1")
nodeA2 = Node("A2")
nodeA1a= Node("A1a")
nodeA1b = Node("A1b")
nodeA2a = Node("A2a")
nodeA2b = Node("A2b")

#left nodes
nodeA.Add(nodeA1)
nodeA1.Add(nodeA1a)
nodeA1.Add(nodeA1b)

#RIGHT NODES
nodeA.Add(nodeA2)
nodeA2.Add(nodeA2a)
nodeA2.Add(nodeA2b)


nodeA.Print()
#output
#A
#A1
#A1a
#A1b
#A2
#A2a
#A2b
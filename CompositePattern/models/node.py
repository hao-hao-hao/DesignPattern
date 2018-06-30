class Node():
    def __init__(self, name):
        self._name = name
        self._nodes = []
    
    def Add(self,node):
        self._nodes.append(node)
    
    def Get(self,index):
        return self._nodes[index]
    
    def Print(self):
        print(self._name)
        for node in self._nodes:
            node.Print()
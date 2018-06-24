class Cache():
    _instance = None
    content = ""

    @staticmethod
    def GetInstance():
        if Cache._instance is None:
            Cache._instance = Cache()
        return Cache._instance
        
    def Add(self,content):
        #Assign Value to the content
        self.content = content
        print(self.content + " is added to the cache")
    
    def Get(self):
        #Print the content
        print("The content is: "+self.content)

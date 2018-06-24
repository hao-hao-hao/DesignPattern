from models import Cache

#create normal instance
cache_a = Cache()
cache_a.Add("Hello")

#Singleton
cache_s1 = Cache.GetInstance()
cache_s1.Add("This is Cache S1")

#Create another instance to check if this is the same instance as s1
cache_s2 = Cache.GetInstance()

#Testing the instance
cache_a.Get()
#output The content is: Hello
cache_s1.Get()
#output The content is: This is Cache S1
cache_s2.Get()
#output The content is: This is Cache S1
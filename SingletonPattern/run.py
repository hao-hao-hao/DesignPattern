from models import Cache

#create normal instance
cache_a = Cache()
cache_a.Add("Hello")

#Singleton
cache_s1 = Cache.GetInstance()
cache_s1.Add("This is Cache S1")
cache_s2 = Cache.GetInstance()

cache_a.Get()
cache_s1.Get()
cache_s2.Get()
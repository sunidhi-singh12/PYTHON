# What will be the length 
s= set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
#line 3 and 4 are considered same because python 20 == 20.0 both are same as they are compard as same int value so the output length will be 2 
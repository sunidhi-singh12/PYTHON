a= (1)
print(type(a)) # if we don't add a comma in the tuple of single element then it'll return the type of int 
a= (1,) 
print(type(a))
print(a)

###### Methods in Tuple
#1. count()
t= (1,2,3,4,5,2,7,2,9)
print(t.count(2)) #counts the occurance 

#2. index()
t=(1,2,3,4,5,6,7,8,9)
print(t.index(4)) #returns the index of the element 

#3. length-> len()
t=(1,2,3,45,5,6,7,8,9)
print(len(t)) #returns the length of tuple

#4. concatenation(+)
t1= (1,2,3,4)
t2= (5,6,7,8)
concated= t1+t2
print(concated)

#5. Repetition (*)
t= (1,2,3)
print(t*3) # repeats the tuple

#6. membership test (in, not in)
t= (1,2,3,4)
print(2 in t) # tells whether element is present or not 
print(5 not in t)
print(5 in t )

#7. iteration(traversing)
t= ("apple", "mango", "kiwi", "grapes", "watermelon")
for item in t: print(item) 

#8. Slicing
t= (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(t[1:5]) #from index 1 to 4 
print(type(t))

#9. nested tuples 
t= (1,2,(3,4,5),6,7,8,9)
print(t[2][2]) 
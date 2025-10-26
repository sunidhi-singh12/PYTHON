# Methods in dictionary
a= { # "keys": "value"
    "Sunidhi" : 21,
    "Surbhi": 22,
    "Nidhi": 23,
    
}
#1. a.items() 
print(a.items())

#2. a.keys()
print(a.keys())

#3. a.update({"______"})
a.update({"Sunidhi":22, "Harry": 25 })
print(a) 

#4. a.get()
print(a.get("Sunidhi")) #will print none
# b= a["Shivi"] # will give KeyError
# print(b)

#5. clear(): Removes all items from the dictionary.
a.clear()
print(a)

#6. copy(): Returns a shallow copy of the dictionary.
a= { # "keys": "value"
    "Sunidhi" : 21, "Surbhi": 22,"Nidhi": 23,}
b= a.copy()
print(b)

#7. fromkeys(): Creates a new dictionary from given keys with a specified value.
keys=('a', 'b', 'c')
value= 10 #assign single same value to all keys 
new_a= a.fromkeys(keys,value)
print(new_a)

#8. values(): Returns all values as a view object.
a= { # "keys": "value"
    "Sunidhi" : 21, "Surbhi": 22,"Nidhi": 23,}
print(a.values())

#9. pop(): Removes a specific key and returns its value.
a= { "Sunidhi" : 21, "Surbhi": 22,"Nidhi": 23,}
value= a.pop("Surbhi")
print(keys)
print(value)
print(a)

#10. popitem(): Removes and returns the last inserted (key, value) pair.
a= {"Name":"Sunidhi", "age":21, "Place": "Jabalpur"}
item= a.popitem()
print(item)
print(a)

#11. setdefault(): Returns the value of a key if present; otherwise adds the key with the specified default value.
a= {"Name":"Sunidhi", "age":21, "Place": "Jabalpur"}
a.setdefault("age",21) 
a.setdefault("place", "Bhopal") 
print(a)
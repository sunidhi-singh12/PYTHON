#1. len(s): returns length of set
a={1,2,3,4,5,6,7,8,9}
print(len(a))

#2. s.remove(element): update the set s and remove element from set
a={1,2,3,4,5,6,7,8,9}
a.remove(7)
print(a)

#3. s.pop(): removes an arbitrary element from the set and return the element removed
a={1,2,3,4,5,6,7,8,9}
a.pop()
print(a)

#4. s.clear(): empties the set s
a={1,2,3,4,5,6,7,8,9}
a.clear() 
print(a)

#5. Union(| or .union()): combines all unique elements from both sets
a={1,2,3,4}
b={3,4,5,6,7}
print(a|b) #using operator
print(a.union(b)) #using method 

#6. Intersection(& or .intersection()): gives common element 
a={1,2,3,4}
b={3,4,5,6,7}
print(a&b)
print(a.intersection(b))

#7. Difference (- or .difference()): elements that are in first set but not in the second 
a={1,2,3,4}
b={3,4,5,6,7}
print(a-b)
print(a.difference(b))

#8. Symmetric Difference(^ or .symmetric_difference()): elements that are in either set, but not in both
a={1,2,3,4}
b={3,4,5,6,7}
print(a^b)
print(a.symmetric_difference(b))

#9. Subset(<= or .issubset()): checks if all elements of one set are present in another
a={1,2}
b={1,2,3,4,5}
print(a<=b)
print(a.issubset(b))

#10. Superset(>= or .issuperset()): checks if one set contains all elements of another
a={1,2,3,4,5,6,7,8}
b={3,4,5,6,7}
print(a>=b)
print(a.issuperset(b))

#11. Disjoint(.isdisjoint()): returns True if two sets have no common elements 
a={1,2,3,4}
b={3,5,6,7}
print(a.isdisjoint(b))

#12. Set Update Methods: modify sets directly 
A = {1, 2, 3}
B = {3, 4}

A.update(B)             # A = A ∪ B
print(A)                # {1, 2, 3, 4}

A.intersection_update(B) # A = A ∩ B
print(A)                # {3, 4}
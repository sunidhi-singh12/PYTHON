# Can you change the values inside a list which is contained in set S?
# s={8,7,12,"Harry",[1,2]}
#this can't be changed because we can't even have a list as an element in a set becuase sets in Python require all their elements to be immutable and hashable. Lists are mutable and not hashable, so they can't be added to a set.
# WAP to find whether a given username contains less than 10 characters or not
name = input("Enter your username: ")
if(len(name)<10):
    print("Characters under limit")
else:
    print("Characters overload")    
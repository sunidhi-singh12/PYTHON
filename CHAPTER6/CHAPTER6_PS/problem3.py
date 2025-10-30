# Spam comment "Make a lot of money", "Buy now", "Subscribe this", "Click this",

p1= 'Make a lot of money'
p2= 'Buy now'
p3= 'Subscribe now'
p4= 'Click this'

message= input("Enter your comment: ")
# here 'in' keyword tells us that is there any string or element present in the given input 
if((p1 in message) or (p2 in message) or (p3 in message) or(p4 in message)):
    print("Alert!! Spam message")
else:
    print("You're safe")    
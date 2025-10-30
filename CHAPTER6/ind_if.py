a= int(input("Enter your age:"))

if(a%2==0): #this is independent if means it will always execute 
    print("Something is happening.......")

if(a>=18):
    print("You are eligible.")

elif(a==0):
    print("You are entering zero.")

elif(a<0):
    print("You are entering invalid age.") 

else:
    print("You are not eligible.")    
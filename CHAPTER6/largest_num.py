a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

if(a==b==c):
    print("All numbers are equal..")
elif(a>b): 
    print("First number is greater..")

elif(b>c):
    print("Second number is greater..")

elif(c>a):
    print("Third number is greater..")

elif(a==b):
    print("First and second nummber are equal..") 

elif(b==c):
    print("Second and third number are equal..")
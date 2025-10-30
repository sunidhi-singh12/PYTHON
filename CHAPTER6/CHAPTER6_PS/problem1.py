# Enter four numbers and find the greatest one. 
a= int(input("Enter first number: "))
b= int(input("Enter second number"))
c= int(input("Enter third number: "))
d= int(input("Enter fourth number: "))

if(a>b and a>c and a>d):
    print("a is the greatest number..")
elif(b>a and b>c and b>d):
    print("b is the gtreatest number..")    
elif(c>a and c>b and c>d):
    print("c is the gtreatest number..")    
elif(d>a and d>b and d>c):
    print("d is the gtreatest number..")    
# WAP to find out whether a given name is present in a list or not 
list= ["Gamora", "Thanos", "Marvel", "Captian America", "Thor", "Wanda", "Natasha"]
name= input("Enter the name: ")
if(name in list):
    print("The name you've entered is present in the list.")
else:
    print("The name you've entered is not present in the list.")    
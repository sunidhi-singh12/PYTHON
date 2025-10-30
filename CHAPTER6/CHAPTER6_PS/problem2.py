subject1= int(input("Entetr first subject: "))
subject2= int(input("Entetr second subject: "))
subject3= int(input("Entetr third subject: "))

total_percentage = (100*(subject1 + subject2 + subject3))/300

if(total_percentage>=40 and subject1>33 and subject2>33 and subject3>33):
    print("Congratulations! You've passed the exam.")
else:
    print("Oops! Try again next year.")    
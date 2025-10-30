# WAP to find whether a given post is talking about Ravi Gupta
post = input("Enter the post: ")
if("Ravi Gupta".lower() in post.lower()): # here lower() function is used for if the user entered the name in lower case then the program can detect the string is correct if it is in lowercase 
    print("Ravi Gupta is in post")
else:
    print("Ravi Gupta is not in the post")    

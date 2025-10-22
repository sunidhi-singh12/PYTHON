import os

# Specify the directory path
directory = input("Enter the directory path: ")

# Check if the path exists
if os.path.exists(directory):
    print(f"\nContents of directory '{directory}':\n")
    
    # List all files and folders in the directory
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified directory does not exist.")
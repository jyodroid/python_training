import os

# Open a file
path = "./prank"
dirs = os.listdir(path)

# get current directory
saved_path = os.getcwd()
print(saved_path)

# Change current directory
os.chdir(path)

# This would print all the files and directories
for file_name in dirs:
    os.rename(file_name, file_name.translate(None, "0123456789"))
os.chdir(saved_path)

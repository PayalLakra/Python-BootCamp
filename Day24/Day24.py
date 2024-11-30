'''Topics to be covered:
- File System
- Relative and Absolute File path
'''

# Read & Write in File
# file = open("my_file.txt")    # needs to close the file manually
# Or we can use
with open("my_file.txt") as file:  # no need to close the file manually
    contents = file.read()
    print(contents)

with open("my_file.txt", mode = "a") as file1:  # no need to close the file manually
    file1.write("\nI am a girl.")

with open("new_file.txt", mode = "w") as file2:  # no need to close the file manually
    file2.write("I am a girl.")

file.close()

# Relative and Absolute File path
# Absolute Path always starts off relative to the root. It basically starts from root of computer storage system. It is always relative to the root of your computer.
# Relative file path is simply just ./name.ppt. The ./ signifies look in the current folder for this file. It Now the relative file path is relative to your current working directory.
# In Windows, the path is separated by a (\) slash.
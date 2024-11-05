'''
Topics to be Covered:
- Calculator- Project
- Functions with output
- Docstrings
'''

#Convert into Title Case
f_name = input("Enter your first name:")
l_name = input("Enter your last name:")

def name(f_name, l_name):
    title_name = f"{f_name.title()} {l_name.title()}"
    return title_name

result = name(f_name=f_name, l_name=l_name)
print(result)
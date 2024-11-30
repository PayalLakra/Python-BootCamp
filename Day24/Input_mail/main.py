PLACEHOLDER = "[name]"

with open("invited_names.txt") as name_files:
    names = name_files.readlines()
    # print(names)

# readlines() method returns a list containing each line in the file as a list item.

with open("starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/letter_for_{stripped_name}.docx", mode = "w") as letters:
            letters.write(new_letter)
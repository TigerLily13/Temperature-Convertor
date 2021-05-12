import re

data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# Get Valid filename
has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Please enter a filename (leave off the extension): ")
    has_error = "no"

    valid_char = "[A-Za-z0-9]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "No spaces allowed"

        else:
            problem = ("No {} allowed" .format(letter))

        has_error = "yes"

    if filename == "":
        problem = "Can't be blank"

        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename: {}" .format(problem))
    else:
        print("You entered a valid filename")

# Add .txt prefix
filename = filename + ".txt"

# Create file
f = open(filename, "w+")

# Add new line for each item
for item in data:
    f.write(item + "\n")

# Close file
f.close()
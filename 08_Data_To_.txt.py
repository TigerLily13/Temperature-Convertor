# Data to be outputted
data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# Get filename (assume valid for now)
filename = input("Please enter a filename (leave off the extension): ")

# Add .txt prefix
filename = filename + ".txt"

# Create file
f = open(filename, "w+")

# Add new line for each item
for item in data:
    f.write(item + "\n")

# Close file
f.close()

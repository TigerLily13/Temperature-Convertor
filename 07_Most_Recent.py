# Set up list
all_calculations = []

# Get data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops the list is empty")

else:
    # Show full list
    print("*** Full List ***")
    print(all_calculations)

    print()

    # Print last three
    if len(all_calculations) >= 3:
        print("*** The Last Three***")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("Items from Newest to Oldest")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])
# Convert degrees C to degrees F
def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine

# Lists
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F" .format(item, answer)
    converted.append(ans_statement)

print(converted)

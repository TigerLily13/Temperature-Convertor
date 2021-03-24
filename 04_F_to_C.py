# Convert degrees C to degrees F
def to_c(from_f):
    fahrenheit = (from_f - 32) * 5/9
    return fahrenheit


# Main Routine

# Lists
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C" .format(item, answer)
    converted.append(ans_statement)

print(converted)

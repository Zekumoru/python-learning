# ask user for two float values
# alternatively, to ask for integer values use int()
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

z = x / y

# print result with 2 decimal places
print(f"{z:.2f}")

# to round a number by n decimal places
z = round(x / y, 2)

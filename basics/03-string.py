# asks user for their name
# then remove whitespace and capitalize
# each first letters
name = input("Enter your name: ").strip().title()

# split user name into first name and last name
first, last = name.split()

# greet the user
print(f"Hello {first}!")

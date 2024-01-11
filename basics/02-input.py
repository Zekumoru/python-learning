# asks user for their name
name = input("Enter your name: ")

# greeting the user
print(f"Hello {name}!") # this is called string interpolation

# other ways to print the exact thing as above

# with string concatenation
print("Hello " + name + "!")

# with arguments
# note that print() adds a space between arguments
print("Hello", name + "!")

# default behaviour of print() can be overridden
# syntax: print(*object, sep=" ", end="\n")
#         *object: means zero or more arguments
#         sep: the default separator between arguments
#         end: the ending string
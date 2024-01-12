# loop 1 to 10 using while
print("While loop")
i = 1
while i <= 10:
  print(f"{i}")
  i += 1

print()

# loop 1 to 10 using for
print("For loop")
for i in range(1, 10):
  print(f"{i}")

# convention in for loops if i isn't needed
# is to use _
for _ in range(1, 3):
  print("Hello")

# looping using multiplation
print("Hello\n" * 3, end="")

# looping through a list
foods = ["apple", "banana", "orange"]

for food in foods:
  print(food)

# alternatively, to get the index instead
for i in range(len(foods)):
  print(f"{foods[i]}")
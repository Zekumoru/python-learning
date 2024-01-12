x = 10
y = 20

# syntax
if (x > y):
  print("x is greater than y")
elif (y > x):
  print("y is greater than x")
else:
  print("x and y are the same")

# to chain multiple conditions
# and is used as &&
# or is used as ||
# example:
if (x >= 0 and y >= 0):
  print("both x and y are positive")

if (x < 0 or y < 0):
  print("Either x or y is negative or both")

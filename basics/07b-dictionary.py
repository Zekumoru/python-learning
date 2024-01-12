# like a hashmap or an object in JS
# syntax:
foods = {
  "apple": "fruit",
  "cabbage": "vegetable",
  "banana": "fruit",
}

# to iterate through a dictionary
for food in foods:
  print(food, foods[food], sep=" is a ")

# interestingly, dictionary with lists is like
# objects in JavaScript
foods = [
  { "name": "apple", "type": "fruit", "color": "red" },
  { "name": "cabbage", "type": "vegetable", "color": "green" },
  { "name": "banana", "type": "fruit", "color": "yellow" },
  # if there's a value that does not exist, we can use None
  # basically it's null in JavaScript
  # for example, imagine we don't know the color of dragonfruit
  { "name": "dragonfruit", "type": "fruit", "color": None },
]

for food in foods:
  print(food)
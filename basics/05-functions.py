# main entry point of the program
def main():
  name = input("Enter you name: ").strip().title()
  name = appendHello(name)
  print(name)

# print hello to a user or just say hello world
def hello(to="world"):
  print(f"Hello {to}!")

# append hello in the string
def appendHello(to="world"):
  return f"Hello {to}!";

main()

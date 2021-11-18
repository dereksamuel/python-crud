import random
import time


def search_lineal(list, objective):
  match = False

  for element in list: # O(n)
    print(f"Iterable times {time.time()} ")
    if element == objective:
      match = True
      print(f"Iterable times {time.time()} END")
      break

  return match


def main():
  list_size = int(input("What is your size list? "))
  objective = int(input("What is your prefer number? "))
  my_list = [random.randint(0, list_size) + 1 for i in range(0, list_size)]

  searched = search_lineal(my_list, objective)
  print(f"The element {objective} {'is not' if not searched else 'is'} into the list")


if __name__ == "__main__":
  main()


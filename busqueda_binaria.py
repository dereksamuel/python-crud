import random
import time

def search_binary(my_list, started, ended, objective):
  print(f"Iterable times {time.time()} ")

  if started > ended:
    return False

  medium = (started + ended) // 2 # Sin decimales la mitad de los dos numbers sumados

  if my_list[medium] == objective:
    print(f"Iterable times {time.time()} END")
    return True
  elif my_list[medium] < objective:
    return search_binary(my_list, medium + 1, ended, objective)
  else:
    return search_binary(my_list, started, medium - 1, objective)


def main():
  list_size = int(input("What is your size list? "))
  objective = int(input("What is your prefer number? "))
  my_list = sorted([random.randint(0, list_size) + 1 for i in range(list_size)])

  searched = search_binary(my_list, 0, len(my_list), objective)
  print(f"The element {objective} {'is not' if not searched else 'is'} into the list")


if __name__ == "__main__":
  main()

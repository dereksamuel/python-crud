import random
import time


def sort_buble(my_list):
  n = len(my_list)

  for i in range(n):
    for j in range(0, n - i - 1):

      if my_list[j] > my_list[j + 1]:
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

  return my_list


def main():
  list_size = int(input("What is your size list? "))
  my_list = [random.randint(0, list_size) + 1 for i in range(0, list_size)]

  sorted_var = sort_buble(my_list)
  print(sorted_var)


if __name__ == "__main__":
  main()


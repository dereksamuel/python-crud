import random
import time


def sort_by_mezcla(my_list):
  if len(my_list) > 1: # lista pequena hasta este punto
    medium = len(my_list) // 2

    left = my_list[:medium]
    right = my_list[medium:]

    sort_by_mezcla(left)
    sort_by_mezcla(right)

    i = 0
    j = 0

    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        my_list[k] = left[i]
        i += 1
      else:
        my_list[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      my_list[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      my_list[k] = right[j]
      j += 1
      k += 1
  return my_list


def main():
  list_size = int(input("What is your size list? "))
  my_list = [random.randint(0, list_size) + 1 for i in range(0, list_size)]
  print(my_list)
  print("- " * 20)

  sorted_var = sort_by_mezcla(my_list)
  print(sorted_var)


if __name__ == "__main__":
  main()
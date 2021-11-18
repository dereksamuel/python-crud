import time;


def factorial(n):
  response = 1

  while n > 1:
    response *= n
    n -= 1

  return response


def factorial_r(n):
  if n == 1:
    return 1

  return n * factorial(n - 1)


def main():
  n = 200000

  begin = time.time()

  factorial(n)

  end = time.time()
  print(end - begin)

  begin = time.time()

  factorial_r(n)

  end = time.time()
  print(end - begin)


if __name__ == "__main__":
  main()

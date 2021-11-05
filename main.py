
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

def isPrime(num):
  if num < 1:
        return False
  elif num == 2:
        return True
  else:
        for i in range(2, num):
            if num % i == 0:
              return False
  return True 

def isEven(num):
  if num%2==0:
     return True
  else:
    return False
def digits(num):
  x = [int(a) for a in str(num)]
  print(x)

for i in range(50):
  print(fib(i), isPrime(i), isEven(i), digits(i))
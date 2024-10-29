# Phoenix Valent
  # U3L2
    # Make the following math function in three different ways !


def forFactorial(num):
  constant = num

  for i in range(1, constant):
    num*=i
  
  return num

def whileFactorial(num):
  constant = num

  while constant > 1:
    constant-=1
    num *= constant

  return num

def recursionFactorial(num):

  if num == 1:
    return num
  else:
    return recursionFactorial(num-1)*num


def main():
  num = 1000
  otherNum = num
  forFact = forFactorial(num)
  whileFact = whileFactorial(num)
  recurseFact = recursionFactorial(num)
  for i in [forFact, whileFact, recurseFact]:
    print(f"{num}! = {i}")

if __name__ == "__main__":
  main()
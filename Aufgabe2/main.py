from random import randint


SWITCH_OPERATOR = {
  "+":"-",
  "-":"+",
  "*":"/",
  "/":"*"
}

def is_integer_num(n):
  ''' Wahr zurückgeben wenn die Zahl ein int ist oder ein gerades float '''
  if isinstance(n, int):
    return True
  if isinstance(n, float):
    return n.is_integer()
  return False

def main(start):
  #bs = []
  #for _ in range(100000):
  #  (a,b,operator) = randomOp(randint(1,100000))
  #  bs.append(b)
  #print(sum(bs)/100000)
  for _ in range(10):
    (a,b,operator) = randomOp(randint(1,100000))
    print(str(a) + operator + str(b) + "=" + str(eval(str(a) + operator + str(b))))

def randomOp(a):
  b = randint(2,9)
  operator = ["+","-","*","/"][randint(0,3)]
  if reverseCalculate(a, b, operator):
    return a,b,operator
  else: 
    return randomOp(a)

def reverseCalculate(a, b, operator):
    if is_integer_num(eval(str(a) + SWITCH_OPERATOR[operator] + str(b))) and is_integer_num(eval(str(a) + operator + str(b))):
      #print(str(eval(str(a) + SWITCH_OPERATOR[operator] + str(b))) + operator + str(b) + "=" + str(a))
      return True
    else:
      #print(eval(str(a) + SWITCH_OPERATOR[operator] + str(b)))
      return False

if __name__ == "__main__":
  main(4324)
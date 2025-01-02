def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        print('Cant divide')
    else:
      return a/b

def sub(a,b):
   return a-b

def main():
    operator =input("enter operator")
    a=1
    b=2

    if operator == '+':
        print (f"Sum is {mult(a,b)}")
main()
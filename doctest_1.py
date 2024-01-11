def add(a,b):
    """function to add two numbers
    usage examples-
    >>> add(2,9)
    11.0
    >>> add(100.1,9.2)
    109.3
    """
    return float(a + b)

def square(x,y):
    """function to square a number
    examples:-
    >>> square(3,2)
    9
    >>> square(5,3)
    125.0
    """
    return int(x**y)

def chocolates(chocolate1, chocolate2, chocolate3):
  """function to print fav chocolate
  examples:-
  >>> chocolates(chocolate1 = "dairymilk", chocolate2 = "bournville", chocolate3 = "truffle")
  my favourite chocolate is bournville
  >>> chocolates(chocolate1 = "eclairs", chocolate2 = "amul", chocolate3 = "kitkat")
  my favourite chocolate is eclairs
  """
  print("my favourite chocolate is " + chocolate2)

chocolates(chocolate1 = "dairymilk", chocolate2 = "bournville", chocolate3 = "truffle")

def factorial(n):
    """function to find factorial
    example:-
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    """
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 


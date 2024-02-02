def tonysEquation(x:int|float, y:int|float, m:int|float, d:int|float) -> float:
  """Takes the sum of two numbers x and y, multiplies them by m, divides them by d, and returns the resault.

  Args:
    x:int|float - left additive
    y:int|float - right additive
    m:int|float - right factor
    d:int|float - right divider

  Returns:
    ((x+y)*m)/d
  """
  sum:int = x + y
  product:int = sum * m
  dividend:float = product / d
  return dividend
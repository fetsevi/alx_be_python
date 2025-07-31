# Robust division function

def safe_divide(numerator, denominator):
    try:
      num=float(numerator)
      deno=float(denominator)
      try:
        return f"The result of the division is {num/deno:.1f}"
      except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return"Error: Please enter numeric values only."

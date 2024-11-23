# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  tens_digit = str(num // 10)
  ones_digit = str(num % 10)
  return int(ones_digit + tens_digit)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))

# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  ones = num % 10
  tens = (num // 10) % 10
  hundreds = (num // 100) % 10
  return ones + tens + hundreds


# Invoke the function with any three-digit number
print(digits_sum(123))

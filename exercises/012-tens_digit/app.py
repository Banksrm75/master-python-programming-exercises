# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  remove_ones_place = num // 10
  return remove_ones_place % 10


# Invoke the function with any integer
print(tens_digit(1234))

# Your code here
def squares_dictionary(n):
    squares_dictionary = {}
    for i in range(1, n+1):
        squares_dictionary[i] = i * i
    return squares_dictionary

print(squares_dictionary(8))
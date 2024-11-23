def apple_sharing(n,k):
  basket = k % n 

  return ((k-basket)/n), basket


print(apple_sharing(6,50))

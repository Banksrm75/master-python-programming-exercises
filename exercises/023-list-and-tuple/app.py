# Your code here

def list_and_tuple(*nums):
    list = []
    for number in nums:
        list.append(str(number))
    new_tuple = tuple(list)
    return list, new_tuple


result_list, result_tuple = list_and_tuple(5, 4, 13, 24, 45)
print(result_list)
print(result_tuple)
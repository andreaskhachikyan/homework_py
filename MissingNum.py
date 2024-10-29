import random


def create_arr(n):
    rand = random.randint(1, n + 1)
    arr = []
    for i in range(1, n + 1):
        if i != rand:
            arr.append(i)
    return arr


def find_missing_number(arr, n):
    return n * (n + 1) // 2 - sum(arr)


n = 15
arr = create_arr(n)
print(arr)
print('Missing number is: ', find_missing_number(arr, n))

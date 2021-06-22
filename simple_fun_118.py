def sum_or_product(arr):
    """
    You are given an array of positive integers. While the array has more than one
    element you can choose two elements and replace them with their sum or product.

    Your task is to find the maximum possible number that can remain in the array
    after multiple such operations.

    arr = [1, 3, 2] => 9
    """
    arr.sort()
    while len(arr) > 1:
        if arr[0] == 1 and arr.count(2) >= 2:
            # add a 3 and remove a 1,2
            arr.append(3)
            arr.pop(0)
            arr.remove(2)
        elif arr[0] == 1:
            # less than 2 twos, append sum of smallest, remove nums
            arr.append(arr[0]+arr[1])
            arr = arr[2:]
        else:
            # no 1s so multiply two smallest and remove
            arr.append(arr[0]*arr[1])
            arr = arr[2:]
        arr.sort()

    return arr[0]


test_cases = [
    ([1, 2, 3],  9),
    ([1, 1, 2],  4),
    ([1, 1, 1],  3),
    ([1],  1),
    ([9],  9),
    ([1, 1],  2),
    ([1, 5],  6),
    ([1, 5, 7],  42),
    ([1, 5, 6],  36),
    ([1, 1, 5, 7],  70),
    ([1, 1, 1, 1],  4),
    ([1, 1, 1, 1, 1],  6),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  1458),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  972),
    ([1, 1, 2, 4, 5],  80),
    ([10, 20, 30],  6000)
]

for arr, expected in test_cases:
    assert sum_or_product(arr) == expected

arr = [1]*50
print(sum_or_product(arr))

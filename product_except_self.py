def find_product_except_self(arr):
    left_products, right_products, res = [], [], []
    left_products.append(1)
    right_products.append(1)
    for i in range(len(arr)-1):
        left_products.append(arr[i]*left_products[-1])
    for j in range(len(arr)-1, 0, -1):
        right_products.append(arr[j]*right_products[-1])
    for k in range(len(arr)):
        res.append(left_products[k]*right_products[::-1][k])
    return res


print(find_product_except_self([1, 2, 3, 4]))

def multiply(*args):
    total_product = 1
    for el in args:
        total_product *= el
    return total_product

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
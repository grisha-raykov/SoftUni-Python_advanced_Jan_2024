even_set = set()
odd_set = set()
for row in range(1, int(input())+1):
    result = sum(ord(x) for x in input()) // row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)
if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

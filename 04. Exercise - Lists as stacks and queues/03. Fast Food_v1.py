from collections import deque

food = int(input())
# Using map()
orders = deque(map(int, input().split()))
# Using list comprehension
orders_list_comp = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if food >= order:
        food -= order
    else:
        print(f'Orders left:', *orders) # join can be used here
        break
else:
    print('Orders complete')

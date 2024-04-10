from collections import deque

food = int(input())
# Using map()
orders_map = deque(map(int, input().split()))
# Using list comprehension
# orders_list_comprehension = deque([int(x) for x in input().split()])

print(max(orders_map))

for order in orders_map.copy():
    if food >= order:
        orders_map.popleft()
        food -= order
    else:
        print(f'Orders left:', order, *orders_map)  # join can be used here
        break
else:
    print('Orders complete')

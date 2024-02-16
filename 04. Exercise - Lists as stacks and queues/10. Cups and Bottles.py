from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

for cup in cups.copy():
    bottle = bottles.pop()
    if bottle > cup:
        wasted_water += bottle - cup
        cups.popleft()
    else:
        cup -= bottle
        for b in bottles[::-1]:
            while cup > 0:
                cup -= b


else:
    if bottles:
        print(f'Bottles: {" ".join(str(i) for i in bottles)}')
        wasted_water += sum(bottles)
    elif cups:
        print(f'Cups {" ".join(str(i) for i in cups)}')
    print(wasted_water)
    # pass

# TODO not finished
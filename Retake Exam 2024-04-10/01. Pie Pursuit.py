from collections import deque

pieces_per_contestant = deque(int(x) for x in input().split())
pieces_per_pie = deque(int(x) for x in input().split())

while pieces_per_contestant and pieces_per_pie:
    current_contestant = pieces_per_contestant.popleft()
    current_pie = pieces_per_pie.pop()

    if current_contestant >= current_pie:
        current_contestant -= current_pie
        if current_contestant > 0:
            pieces_per_contestant.append(current_contestant)
    else:
        current_pie -= current_contestant
        if current_pie > 1 or len(pieces_per_pie) == 0:
            pieces_per_pie.append(current_pie)
        elif len(pieces_per_pie) > 0:
            pieces_per_pie[-1] += 1

if not pieces_per_contestant:
    if not pieces_per_pie:
        print("We have a champion!")
    else:
        print("Our contestants need to rest!")
        print("Pies left:", ', '.join([str(x) for x in pieces_per_pie]))
else:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left:", ', '.join([str(x) for x in pieces_per_contestant]))
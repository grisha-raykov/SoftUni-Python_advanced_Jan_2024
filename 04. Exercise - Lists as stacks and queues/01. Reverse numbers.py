from collections import deque

numbers = deque(input().split())

# Works with while too
for _ in range(len(numbers)):
    print(numbers.pop(), end=' ')

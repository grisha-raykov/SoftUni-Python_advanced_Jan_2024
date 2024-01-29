n = int(input())

cars = set()

for _ in range(n):
    direction, car_number = input().split()
    if direction == 'IN':
        cars.add
from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
passed_cars = 0

while True:
    command = input()
    if command == "END":
        break
    elif command == "green":
        green_light = green_light_duration
        free_window = free_window_duration
        while green_light > 0 and cars:
            car = cars.popleft()
            for i in range(len(car)):
                if green_light > 0:
                    green_light -= 1
                elif free_window > 0:
                    free_window -= 1
                else:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[i]}.")
                    exit(0)
            passed_cars += 1
    else:
        cars.append(command)

print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")
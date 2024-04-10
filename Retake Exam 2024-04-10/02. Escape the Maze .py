# Input
matrix_size = int(input())
maze = [list(input()) for _ in range(matrix_size)]
commands = []
hp = 100
position = None
while True:
    try:
        command = input()
        if command:
            commands.append(command)
        else:
            break
    except EOFError:
        break

for i in range(matrix_size):
    for j in range(matrix_size):
        if maze[i][j] == 'P':
            position = (i, j)
            break
    if position is not None:
        break

for direction in commands:
    x, y = position
    if direction == "up":
        new_position = (x - 1, y)
    elif direction == "down":
        new_position = (x + 1, y)
    elif direction == "right":
        new_position = (x, y + 1)
    elif direction == "left":
        new_position = (x, y - 1)

    if 0 <= new_position[0] < matrix_size and 0 <= new_position[1] < matrix_size:
        maze[x][y] = '-'
        x, y = new_position
        if maze[x][y] == 'M':
            hp -= 40
            if hp <= 0:
                hp = 0
                maze[x][y] = 'P'
                break
        elif maze[x][y] == 'H':
            hp += 15
            if hp > 100:
                hp = 100
        elif maze[x][y] == 'X':
            maze[x][y] = 'P'
            break
        position = (x, y)
        maze[x][y] = 'P'

if hp > 0:
    print("Player escaped the maze. Danger passed!")
else:
    print("Player is dead. Maze over!")
print(f"Player's health: {hp} units")
for row in maze:
    print(''.join(row))
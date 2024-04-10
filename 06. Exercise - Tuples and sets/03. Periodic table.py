input_lines = int(input())
elements = set()
for _ in range(input_lines):
    for element in input().split():
        elements.add(element)
print(*elements, sep='\n')
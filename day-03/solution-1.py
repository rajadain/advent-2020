slope = []

with open('input-1.txt') as f:
    slope = f.readlines()

num_trees = 0
x = 0
y = 0

while y < len(slope):
    # print(f'{y+1} {(x+1) % 31} {slope[y][x % 31]}')
    if slope[y][x % 31] == '#':
        num_trees += 1

    x += 3
    y += 1

print(num_trees)  # 265

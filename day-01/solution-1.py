nums = []

with open('input-1.txt') as f:
    nums = [int(line) for line in f.readlines()]

for num in nums:
    complement = 2020 - num
    if complement in nums:
        print(num)  # 1312
        print(complement)  # 708
        print(num * complement)  # 928896
        exit()

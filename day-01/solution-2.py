nums = []

with open('input-1.txt') as f:
    nums = [int(line) for line in f.readlines()]

for one in nums:
    complement = 2020 - one
    viables = [x for x in nums if x < complement]
    for two in viables:
        three = complement - two
        if three in viables:
            print(one)  # 798
            print(two)  # 664
            print(three)  # 558
            print(one * two * three)  # 295668576
            exit()

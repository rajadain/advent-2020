password = '3-4 t: dttt'


class Password:
    _min = 0
    _max = 0
    _letter = ''
    _value = ''
    _count = 0

    def __init__(self, min, max, letter, value):
        self._min = min
        self._max = max
        self._letter = letter
        self._value = value

    def check(self):
        occurrences = len([occ for occ in self._value if occ == self._letter])
        return self._min <= occurrences <= self._max


def toPassword(string):
    left, right = string.split('-')
    _min = int(left)
    left, right, _value = right.split(' ')
    _max = int(left)
    _letter = right[0]

    return Password(_min, _max, _letter, _value)


passes = []

with open('input-1.txt') as f:
    passes = [toPassword(line) for line in f.readlines()]

checks = [password.check() for password in passes]

num_valids = len([p for p in checks if p])
print(num_valids)  # 586

password = '3-4 t: dttt'


class Password:
    _min = 0
    _max = 0
    _letter = ''
    _value = ''

    def __init__(self, min, max, letter, value):
        self._min = min
        self._max = max
        self._letter = letter
        self._value = value

    def check(self):
        if self._max > len(self._value):
            return False

        is_first = self._value[self._min - 1] == self._letter
        is_second = self._value[self._max - 1] == self._letter

        return (is_first and not is_second) or (is_second and not is_first)


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
print(num_valids)  # 352

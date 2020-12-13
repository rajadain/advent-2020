from pathlib import Path

pp_req_fields = set(['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'])
pp_opt_fields = set(['cid'])

pp_ecl_values = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def toDict(pp_string):
    output = {}

    pp_string = pp_string.strip().replace('\n', ' ')
    pairs = pp_string.split(' ')

    for pair in pairs:
        k, v = pair.split(':')
        output[k] = v

    return output


def isValid(pp_dict):
    fields = set(pp_dict.keys())
    if not (fields - pp_opt_fields) == pp_req_fields:
        return False

    # Birth Year
    try:
        byr = int(pp_dict['byr'])
        if not (1920 <= byr <= 2002):
            return False
    except ValueError:
        return False

    # Issue Year
    try:
        iyr = int(pp_dict['iyr'])
        if not (2010 <= iyr <= 2020):
            return False
    except ValueError:
        return False

    # Expiration Year
    try:
        eyr = int(pp_dict['eyr'])
        if not (2020 <= eyr <= 2030):
            return False
    except ValueError:
        return False

    # Height
    try:
        hgt = pp_dict['hgt']
        unit = hgt[-2:]
        if unit == 'cm':
            val = int(hgt[:-2])
            if not (150 <= val <= 193):
                return False
        elif unit == 'in':
            val = int(hgt[:-2])
            if not (59 <= val <= 76):
                return False
        else:
            return False
    except ValueError:
        return False

    # Hair Color
    try:
        hcl = pp_dict['hcl']
        if hcl[0] != '#':
            return False

        if len(hcl) != 7:
            return False

        int(hcl[1:], 16)
    except ValueError:
        return False

    # Eye Color
    if pp_dict['ecl'] not in pp_ecl_values:
        return False

    # Passport ID
    try:
        pid = pp_dict['pid']
        if len(pid) != 9:
            return False
        int(pid)
    except ValueError:
        return False

    return True


pp_strings = Path('input-1.txt').read_text().split('\n\n')
pp_dicts = map(toDict, pp_strings)
pp_checks = map(isValid, pp_dicts)

print(len([ppc for ppc in pp_checks if ppc]))  # 121

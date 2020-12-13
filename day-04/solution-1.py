from pathlib import Path

pp_req_fields = set(['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'])
pp_opt_fields = set(['cid'])


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
    return (fields - pp_opt_fields) == pp_req_fields


pp_strings = Path('input-1.txt').read_text().split('\n\n')
pp_dicts = map(toDict, pp_strings)
pp_checks = map(isValid, pp_dicts)

print(len([ppc for ppc in pp_checks if ppc]))  # 190

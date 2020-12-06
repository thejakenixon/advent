# Code from /u/xelf on Reddit

data = open('data.txt','r').read().split('\n\n')
passports = [ dict( x.split(':') for x in line.split() ) for line in data ]

def part1(d):
    return all(x in d for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid'])

print(sum(part1(p) for p in passports))
def part2(d):
    return all([
        1920<= int(d['byr']) <=2002,
        2010<= int(d['iyr']) <=2020,
        2020<= int(d['eyr']) <=2030,
        ( d['hgt'][-2:] == 'in' and 59<= int(d['hgt'][:-2]) <= 76 ) or
        ( d['hgt'][-2:] == 'cm' and 150<= int(d['hgt'][:-2]) <= 193),
        d['hcl'][0] == '#' and all (c in '0123456789abcdef' for c in d['hcl'][1:]),
        d['ecl'] in 'amb blu brn gry grn hzl oth'.split(),
        d['pid'].isdigit() and len(d['pid'])==9
    ])

print( sum(part1(p) and part2(p) for p in passports) )

health = 3
soc = 10
if health == 0 or health <= 0:
    exit

print('dzivibas',health)
print('tu piedzimi tavas darbibas?')
print('kliegt:1')
print('apcuraties:2')
d1 = input('1, 2:')
if d1 == '1':
    soc = soc - 1
    print('social approvment', soc)
    print('nafig kliedz?')

elif d1 == '2':
    print('labais es ari ta daritu')

print('tev ir 1 gads, ievadi savu svaru kilogramos')
d2 = int(input('es sveru:'))

if d2 <= 8:
    print('tev ir jauznem svaru')
    d3 = input('atteikties:1, peikrist:2 ')
    if d3 == '1':
        health = health - 1 
        print('dzivibas',health)
        print('tu esi neveseligs')
    elif d3 == '2':
        print('malacis tu labojies')
elif d2 >= 8 and d2 <= 12:
    print('skaistulis')
elif d2 >= 12:
    print('tu tefteli ej patreneties')
    d4 = input('atteikties:1, peikrist:2 ')
    if d4 == '1':
        health = health - 1 
        print('dzivibas',health)
        print('tu esi neveseligs')
    elif d4 == '2':
        print('malacis tu labojies')

print('')
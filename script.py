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

print('you are in the school')
print('school bully aproeches you')
if d4 == 1 or d3 == 1:
    print('bully laughs at you becouse of your body shape')
    soc = soc - 1
    print('social approvment', soc)
if soc >= 9:
    d5 = input('offend him:1, other:2 ')
if d5 == '2' or soc <= 9:
    d6 = input('ignor him:1, fight:2 ')
    if d6 == '1':
        soc = soc -1
        print('social approvment', soc)

bully = 10
you = 10
if d2 >= 8:
    you = you + 5
if d5 == '1' or d6 =='2':
    print('you are fighting the bully')
    while bully >= 0:
        atk = input('punch:1 kick:2 block:3 run:4 ')
        if atk == '4':
            break
        elif atk == '1':
            bully = bully -3
            print('bully hp:', bully)
            print('you punched him in the face')
        elif atk == '2':
            you = you -1
            print('your hp:', you)
            print('you missed the kick and fall on your back')
        elif atk == '3':
            print('you placed block')
        print('bully attacks')
        if atk == '3':
            you = you -2
            print('bully hits you on the shoulder, it hurts bad. your hp: ', you )
        elif atk == '1':
            you = you -4
            print('bully hit you in your stomach, it is painful. your hp: ', you)
        elif atk == '2':
            you = you -5
            print('')

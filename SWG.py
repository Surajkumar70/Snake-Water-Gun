
import random
def swg():
    point = 0
    computer = 0
    turns = 0
    while turns<10:
        a = ['Snake','Water','Gun']
        rd = random.choice(a)
        turns +=1
        dic = {1:'Snake',2:'Water',3:'Gun'}
        b = int(input('1.Snake,2.Water,3.Gun :'))
        if b in dic:
            print(dic[b])
            if rd == 'Snake':
                if dic[b] == 'Snake':
                    print('its tie')
                elif dic[b] == 'Water':
                    print('computer wins')
                    computer +=1
                elif dic[b] == 'Gun':
                    print('user wins')
                    point+=1
            elif rd == 'Water':
                if dic[b] == 'Snake':
                    print('user wins')
                    point+=1
                elif dic[b] == 'Water':
                    print('its tie')
                elif dic[b] == 'Gun':
                    print('computer wins')
                    computer +=1
            elif rd == 'Gun':
                if dic[b] == 'Snake':
                    print('computer wins')
                    computer+=1
                elif dic[b] == 'Water':
                    print('user wins')
                    point+=1
                elif dic[b] == 'Gun':
                    print('its a tie')
        else:
            print('retry entry')
    print('Game over', 'User Win :',point,'computer Win :',computer)
    if point>computer:
        print('player wins')
    elif computer>point:
        print('computer wins')
    else:
        print('the match is tied')
swg()
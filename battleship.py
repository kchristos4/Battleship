#KARAGIANNIDIS CHRISTOS , A.M. 4375



import random
players = ['player 1','player 2','cpu']

player1_ships = {'A1':'no_ship' ,'A2':'no_ship','A3':'no_ship','A4':'no_ship','A5':'no_ship',
                 'B1':'no_ship' ,'B2':'no_ship','B3':'no_ship','B4':'no_ship','B5':'no_ship',
                 'C1':'no_ship' ,'C2':'no_ship','C3':'no_ship','C4':'no_ship','C5':'no_ship',
                 'D1':'no_ship' ,'D2':'no_ship','D3':'no_ship','D4':'no_ship','D5':'no_ship',
                 'E1':'no_ship' ,'E2':'no_ship','E3':'no_ship','E4':'no_ship','E5':'no_ship'}
player2_ships = {'A1':'no_ship' ,'A2':'no_ship','A3':'no_ship','A4':'no_ship','A5':'no_ship',
                 'B1':'no_ship' ,'B2':'no_ship','B3':'no_ship','B4':'no_ship','B5':'no_ship',
                 'C1':'no_ship' ,'C2':'no_ship','C3':'no_ship','C4':'no_ship','C5':'no_ship',
                 'D1':'no_ship' ,'D2':'no_ship','D3':'no_ship','D4':'no_ship','D5':'no_ship',
                 'E1':'no_ship' ,'E2':'no_ship','E3':'no_ship','E4':'no_ship','E5':'no_ship'}
cpu_ships =     {'A1':'no_ship' ,'A2':'no_ship','A3':'no_ship','A4':'no_ship','A5':'no_ship',
                 'B1':'no_ship' ,'B2':'no_ship','B3':'no_ship','B4':'no_ship','B5':'no_ship',
                 'C1':'no_ship' ,'C2':'no_ship','C3':'no_ship','C4':'no_ship','C5':'no_ship',
                 'D1':'no_ship' ,'D2':'no_ship','D3':'no_ship','D4':'no_ship','D5':'no_ship',
                 'E1':'no_ship' ,'E2':'no_ship','E3':'no_ship','E4':'no_ship','E5':'no_ship'}
choices = ['A1','A2','A3','A4','A5',
           'B1','B2','B3','B4','B5',
           'C1','C2','C3','C4','C5',
           'D1','D2','D3','D4','D5',
           'E1','E2','E3','E4','E5']
cpu_choices = ['A1','A2','A3','A4','A5',
               'B1','B2','B3','B4','B5'
               'C1','C2','C3','C4','C5',
               'D1','D2','D3','D4','D5',
               'E1','E2','E3','E4','E5']




def num_to_text(num):
    if (num==0):return ' '
    elif (num==1):return 'O'
    elif (num==2): return 'X'





board1 = [[num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)]]
board2 = [[num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)],
         [num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0),num_to_text(0)]]






def grid():
    print('   P1         P2   ')
    print(' '+'A'+' '+'B'+' '+'C'+' '+'D'+' '+'E'+ ' '+' '+'A'+' '+'B'+' '+'C'+' '+'D'+' '+'E')
    for p in range(1,6):
        print(str(p)+ board1[p-1][0]+' '+board1[p-1][1]+' '+ board1[p-1][2]+' '+ board1[p-1][3]+' '+ board1[p-1][4]+
              ' '+
              str(p) + board2[p-1][0]+' '+board2[p-1][1]+' '+ board2[p-1][2]+' '+ board2[p-1][3]+' '+ board2[p-1][4])






def player1_attack_to_cpu():
    global win_p1
    win_player1 = win_p1
    attack_p1_to_cpu = input('Player 1 enter the position to throw your missile:')
    attack_p1_to_cpu = attack_p1_to_cpu.upper()
    print('missile thrown at '+ str(attack_p1_to_cpu))
    if (cpu_ships[str(attack_p1_to_cpu)] == 'destroyed') or (attack_p1_to_cpu not in choices):
          print('Invalid position, or missile already thrown there.Try again:')
          player1_attack_to_cpu()
    elif (cpu_ships[str(attack_p1_to_cpu)] == 'ship'):
        print('Target hit!')
        lista = position_to_board(attack_p1_to_cpu)
        board2[lista[1]][lista[0]] = num_to_text(1)        
        cpu_ships[str(attack_p1_to_cpu)] = 'destroyed'
        win_p1 += 1
        grid()
    elif (cpu_ships[str(attack_p1_to_cpu)] == 'no_ship'):
        print('Target missed!')
        lista = position_to_board(attack_p1_to_cpu)
        board2[lista[1]][lista[0]] = num_to_text(2)
        cpu_ships[str(attack_p1_to_cpu)] = 'destroyed'
        grid()
    return win_player1

def player1_attack_to_player2():
    global win_p1
    win_player1 = win_p1
    attack_p1_to_p2 = input('Player 1 enter the position to throw your missile:')
    attack_p1_to_p2 = attack_p1_to_p2.upper()
    print('missile thrown at '+ str(attack_p1_to_p2))
    if (player2_ships[str(attack_p1_to_p2)] == 'destroyed') or (attack_p1_to_p2 not in choices):
          print('Invalid position, or missile already thrown there.Try again:')
          player1_attack_to_player2()
    elif (player2_ships[str(attack_p1_to_p2)] == 'ship'):
        print('Target hit!')
        lista = position_to_board(attack_p1_to_p2)
        board2[lista[1]][lista[0]] = num_to_text(1)        
        player2_ships[str(attack_p1_to_p2)] = 'destroyed'
        win_p1 += 1
        grid()
    elif (player2_ships[str(attack_p1_to_p2)] == 'no_ship'):
        print('Target missed!')
        lista = position_to_board(attack_p1_to_p2)
        board2[lista[1]][lista[0]] = num_to_text(2)
        player2_ships[str(attack_p1_to_p2)] = 'destroyed'
        grid()
    return win_player1

def player2_attack_to_player1():
    global win_p2
    win_player2 = win_p2
    attack_p2_to_p1 = input('Player 2 enter the position to throw your missile:')
    attack_p2_to_p1 = attack_p2_to_p1.upper()
    print('missile thrown at '+ str(attack_p2_to_p1))
    if (player1_ships[str(attack_p2_to_p1)] == 'destroyed') or (attack_p2_to_p1 not in choices):
          print('Invalid position, or missile already thrown there.Try again:')
          player2_attack_to_player1()
    elif (player1_ships[str(attack_p2_to_p1)] == 'ship'):
        print('Target hit!')
        lista = position_to_board(attack_p2_to_p1)
        board1[lista[1]][lista[0]] = num_to_text(1)        
        player1_ships[str(attack_p2_to_p1)] = 'destroyed'
        win_p2 += 1
        grid()
    elif (player1_ships[str(attack_p2_to_p1)] == 'no_ship'):
        print('Target missed!')
        lista = position_to_board(attack_p2_to_p1)
        board1[lista[1]][lista[0]] = num_to_text(2)
        player1_ships[str(attack_p2_to_p1)] = 'destroyed'
        grid()
    return win_player2

def cpu_attack_to_player1():
    global win_p2
    win_player2 = win_p2
    cpu_attack_to_p1 = random.choice(choices)
    if (player1_ships[str(cpu_attack_to_p1)] == 'destroyed'):
        cpu_attack_to_player1()
    elif (player1_ships[str(cpu_attack_to_p1)] == 'ship'):
        print('missile thrown at '+ str(cpu_attack_to_p1))
        print('Target hit!')
        lista = position_to_board(cpu_attack_to_p1)
        board1[lista[1]][lista[0]] = num_to_text(1)
        player1_ships[str(cpu_attack_to_p1)] = 'destroyed'
        win_p2 +=1
        grid()
    elif (player1_ships[str(cpu_attack_to_p1)] == 'no_ship'):
        print('missile thrown at '+ str(cpu_attack_to_p1))
        print('Target missed!')
        lista = position_to_board(cpu_attack_to_p1)
        board1[lista[1]][lista[0]] = num_to_text(2)
        player1_ships[str(cpu_attack_to_p1)] = 'destroyed'
        grid()
    return win_player2



    
def position_to_board(position_given):
    available = ['A','B','C','D','E','1','2','3','4','5']
    lst = []
    for c in position_given:
        if c in available:
            lst.append(c)
    lst[0] = ord(str(lst[0])) - int(65)
    lst[1] = int(lst[1]) - int(1)
    return lst

def ship_chosing_p1():
        ship_chosen = input('player 1 enter the position of your ship no'+str(i)+':' )
        ship_chosen = ship_chosen.upper()
        if ship_chosen not in choices:
            print('Invalid position, or position already taken.Try again:')
            ship_chosing_p1()
        elif (player1_ships[ship_chosen] == 'ship'):
            print('Invalid position, or position already taken.Try again:')
            ship_chosing_p1()
        else:
            player1_ships[ship_chosen] = 'ship'

def ship_chosing_p2():
        ship_chosen = input('player 2 enter the position of your ship no'+str(i)+':' )
        ship_chosen = ship_chosen.upper()
        if ship_chosen not in choices:
            print('Invalid position, or position already taken.Try again:')
            ship_chosing_p2()
        elif (player2_ships[ship_chosen] == 'ship'):
            print('Invalid position, or position already taken.Try again:')
            ship_chosing_p2()
        else:
            player2_ships[ship_chosen] = 'ship'


def who_starts_first():
    starting_player = random.choice(players)
    return (starting_player)
def how_many_players():
    player_number = input('Input 1 for 1-player game or 2 for 2-player game:')
    return (player_number)



#================MAIN PROGRAM====================

print('BATTLESHIP GAME')
print('The objective is to sink the opponent\'s ships before the opponent sinks yours.')
play_num = str(how_many_players())
win_p1 = 0
win_p2 = 0
pl = ['1','2']


while (play_num not in pl):
    print('Invalid number of players.Try again:')
    play_num = how_many_players()
if (play_num == '1'):
    del(players[1])
    for i in range(1,6):
        ship_chosing_p1()    
    for i in range(1,6):
        cpu_ship_chosen = random.choice(cpu_choices)
        cpu_ships[cpu_ship_chosen] = 'ship'
        cpu_choices.remove(cpu_ship_chosen)
    str_pl = who_starts_first()
    print( str(str_pl) + ' starts first.')
    if (str_pl == 'player 1'):
        while (win_p1 != 5) and (win_p2 != 5):
            player1_attack_to_cpu()
            if (win_p1 == 5):
                break
            else:
                cpu_attack_to_player1()
    elif (str_pl == 'cpu'):
        while (win_p1 != 5) and (win_p2 != 5):
            cpu_attack_to_player1()
            if (win_p2 == 5):
                break
            else:
                player1_attack_to_cpu()
    if (win_p2 == 5):
        print ('CPU WINS!')
        print ('GAME OVER!')
    elif (win_p1 == 5):
        print ('PLAYER 1 WINS!')
        print ('GAME OVER!')
elif (play_num == '2'):
    del(players[2])
    for i in range(1,6):
        ship_chosing_p1()
    for i in range(1,6):
        ship_chosing_p2()
    str_pl = who_starts_first()
    print(str(str_pl) + ' stars first.')
    if (str_pl == 'player 1'):
        while (win_p1 != 5) and (win_p2 != 5):
            player1_attack_to_player2()
            if (win_p1 == 5):
                break
            else:
                player2_attack_to_player1()
    elif (str_pl == 'player 2'):
        while (win_p1 != 5) and (win_p2 != 5):
            player2_attack_to_player1()
            if (win_p2 == 5):
                break
            else:
                player1_attack_to_player2()
    if (win_p2 == 5):
        print('PLAYER 2 WINS!')
        print('GAME OVER!')
elif (win_p1 == 5):
    print('PLAYER 1 WINS!')
    print('GAME OVER')

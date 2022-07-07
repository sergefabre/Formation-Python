map = [
    [' 1 ',' 2 ',' 3 '],
    [' 4 ',' 5 ',' 6 '],
    [' 7 ',' 8 ',' 9 '],
]

def eqal_row(row):
    return map[row][0]==map[row][1]==map[row][2]
def eqal_col(col):
    return map[0][col]==map[1][col]==map[2][col]
def eqal_diag():
    return (map[0][0] == map[1][1] == map[2][2]) or (map[0][2] == map[1][1] == map[2][0])

def draw():
    for row in range(3):
        for col in range(3):
            print(map[row][col], end='')
        print()

def isWin():
    if eqal_diag(): 
        return True
    for i in range(3):
        for j in range(3):
            if(eqal_row(i) or eqal_col(j)):
                return True
    return False

def isNulle():
    for i in range(3):
        for j in range(3):
            if map[i][j].strip().isnumeric():
                return False
    return True

draw()

player1 = input(' Nom du player 1 ? > ')
player2 = input(' Nom du player 2 ? > ')
player = player1
symb = (' X ', ' O ')

while True:
    choice = input(f'{ player }, votre choix > ')
    if choice == 'Q':
        print('OK, on quitte la partie ...')
        break
    row_col = divmod(int(choice) - 1, 3)
    print('Row | Col -> ', row_col)
    if map[row_col[0]][row_col[1]] == ' X ' or map[row_col[0]][row_col[1]] == ' O ':
        print('Choix impossible ...')
    else:
        map[row_col[0]][row_col[1]] = symb[0] if player == player1 else symb[1]
    draw()
    if isWin():
        print(f'Bravo { player } !!, Vous avez gagné')
        break
    if isNulle():
        print('Partie nulle ...')
        break
    player = player1 if player == player2 else player2



def test():
    for row in range(9):
        print(f'it { row  + 1}', (row )//3, (row )%3, divmod(row,3))
# test()
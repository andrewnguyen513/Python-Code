import random
import sys

def printheader():
    print()
    print("Welcome to Tic Tac Toe")

def draw():
    table = ''
    for i in range(2,11):
        if i%3 == 0:
            table += '\n'
            table += '||\t' + str(i-2) + '\t||\t' + str(i-1) + '\t||\t' + str(i) + '\t||'
        else:
            table += '\n'
            table += '    __________      __________      __________'
    print(table)
    return table

def userxo():
    while 1:
        print()
        print("X or O?")
        xo = input("")
        if xo == 'X' or xo == 'O' or xo == 'x' or xo == 'o':
            xo = xo.upper()
            break
        else:
            print("Please choose X or O")
    return xo

def computerxo(xo):
    if xo == 'X':
        compxo = 'O'
    elif xo == 'O':
        compxo = 'X'
    return compxo

def usermove(xo):
    number = False
    while not number:                                       #input is a number and not taken
        space = input("Your Move, which space? (Enter 1-9) ")
        if space.isdigit() == True and table.find(space) != -1:
            number = True
        else:
            print("Please enter a valid, empty space")
    print(table.replace(space,xo))
    return table.replace(space,xo)
       
def computermove(compxo):
    print()
    print("Computer's Move:") 
    
    if table[168] == '5':
        print(table.replace(table[168],compxo))
        return table.replace(table[168],compxo)
    elif (table[51] == table[56] == xo or table[51] == table[56] == compxo) and table[61] == '3':                   #first row
        print(table.replace(table[61],compxo))
        return table.replace(table[61],compxo)
    elif (table[51] == table[61] == xo or table[51] == table[61] == compxo) and table[56] == '2':                 #first row
        print(table.replace(table[56],compxo))
        return table.replace(table[56],compxo)
    elif (table[56] == table[61] == xo or table[56] == table[61] == compxo) and table[51] == '1':                 #first row
        print(table.replace(table[51],compxo))
        return table.replace(table[51],compxo)
    elif (table[163] == table[168] == xo or table[163] == table[168] == compxo) and table[173] == '6':              #second row
        print(table.replace(table[173],compxo))
        return table.replace(table[173],compxo)
    elif (table[163] == table[173] == xo or table[163] == table[173] == compxo) and table[168] == '5':              #second row
        print(table.replace(table[168],compxo))
        return table.replace(table[168],compxo)
    elif (table[168] == table[173] == xo or table[168] == table[173] == compxo) and table[163] == '4':              #second row
        print(table.replace(table[163],compxo))
        return table.replace(table[163],compxo)
    elif (table[275] == table[280] == xo or table[275] == table[280] == compxo) and table[285] == '9':              #third row
        print(table.replace(table[285],compxo))
        return table.replace(table[285],compxo)
    elif (table[275] == table[285] == xo or table[275] == table[285] == compxo) and table[280] == '8':              #third row
        print(table.replace(table[280],compxo))
        return table.replace(table[280],compxo)
    elif (table[280] == table[285] == xo or table[280] == table[285] == compxo) and table[275] == '7':              #third row
        print(table.replace(table[275],compxo))
        return table.replace(table[275],compxo)
    elif (table[51] == table[163] == xo or table[51] == table[163] == compxo) and table[275] == '7':                       #first column
        print(table.replace(table[275],compxo))
        return table.replace(table[275],compxo)
    elif (table[51] == table[275] == xo or table[51] == table[275] == compxo) and table[163] == '4':                       #first column
        print(table.replace(table[163],compxo))
        return table.replace(table[163],compxo)
    elif (table[163] == table[275] == xo or table[163] == table[275] == compxo) and table[51] == '1':                       #first column
        print(table.replace(table[51],compxo))
        return table.replace(table[51],compxo)
    elif (table[56] == table[168] == xo or table[56] == table[168] == compxo) and table[280] == '8':             #second column
        print(table.replace(table[280],compxo))
        return table.replace(table[280],compxo)
    elif (table[56] == table[280] == xo or table[56] == table[280] == compxo) and table[168] == '5':             #second column
        print(table.replace(table[168],compxo))
        return table.replace(table[168],compxo)
    elif (table[168] == table[280] == xo or table[168] == table[280] == compxo) and table[56] == '2':             #second column
        print(table.replace(table[56],compxo))
        return table.replace(table[56],compxo)
    elif (table[61] == table[173] == xo or table[61] == table[173] == compxo) and table[285] == '9':             #third column
        print(table.replace(table[285],compxo))
        return table.replace(table[285],compxo)
    elif (table[61] == table[285] == xo or table[61] == table[285] == compxo) and table[173] == '6':             #third column
        print(table.replace(table[173],compxo))
        return table.replace(table[173],compxo)
    elif (table[173] == table[285] == xo or table[173] == table[285] == compxo) and table[61] == '3':             #third column
        print(table.replace(table[61],compxo))
        return table.replace(table[61],compxo)
    elif (table[51] == table[168] == xo or table[51] == table[168] == compxo) and table[285] == '9':               #diagonal bottom right to top left
        print(table.replace(table[285],compxo))
        return table.replace(table[285],compxo)
    elif (table[51] == table[285] == xo or table[51] == table[285] == compxo) and table[168] == '5':               #diagonal bottom right to top left
        print(table.replace(table[168],compxo))
        return table.replace(table[168],compxo)
    elif (table[168] == table[285] == xo or table[168] == table[285] == compxo) and table[51] == '1':               #diagonal bottom right to top left
        print(table.replace(table[51],compxo))
        return table.replace(table[51],compxo)
    elif (table[61] == table[168] == xo or table[61] == table[168] == compxo) and table[275] == '7':               #diagonal bottom left to top right
        print(table.replace(table[275],compxo))
        return table.replace(table[275],compxo)
    elif (table[61] == table[275] == xo or table[61] == table[275] == compxo) and table[168] == '5':               #diagonal bottom left to top right
        print(table.replace(table[168],compxo))
        return table.replace(table[168],compxo)
    elif (table[168] == table[275] == xo or table[168] == table[275] == compxo) and table[61] == '3':               #diagonal bottom left to top right
        print(table.replace(table[61],compxo))
        return table.replace(table[61],compxo)
    else:
        openslot = False
        while not openslot:
            slot = str(random.randint(1,9))
            if table.find(slot) != -1:
                openslot = True       
        print(table.replace(slot,compxo))
        return table.replace(slot,compxo) 

def checkwin(xo, compxo, table):
    gameover = False
    
    if table[51] == table[56] == table[61] == xo:               #first row
        print("You win! Congrats!")
        gameover = True
    elif table[51] == table[56] == table[61] == compxo:
        print("Computer wins! Sorry!")
        gameover =  True 
    elif table[163] == table[168] == table[173] == xo:            #second row
        print("You win! Congrats!")
        gameover =  True
    elif table[163] == table[168] == table[173] == compxo:
        print("Computer wins! Sorry!")
        gameover = True
    elif table[275] == table[280] == table[285] == xo:            #third row
        print("You win! Congrats!")
        gameover = True
    elif table[275] == table[280] == table[285] == compxo:
        print("Computer wins! Sorry!")
        gameover = True  
    elif table[51] == table[163] == table[275] == xo:             #first column
        print("You win! Congrats!")
        gameover = True
    elif table[51] == table[163] == table[275] == compxo:
        print("Computer wins! Sorry!")
        gameover = True
    elif table[56] == table[168] == table[280] == xo:             #second column
        print("You win! Congrats!")
        gameover = True
    elif table[56] == table[168] == table[280] == compxo:
        print("Computer wins! Sorry!")
        gameover = True   
    elif table[61] == table[173] == table[285] == xo:             #third column
        print("You win! Congrats!")
        gameover = True
    elif table[61] == table[173] == table[285] == compxo:
        print("Computer wins! Sorry!")
        gameover = True   
    elif table[51] == table[168] == table[285] == xo:               #diagonal right to left
        print("You win! Congrats!")
        gameover = True
    elif table[51] == table[168] == table[285] == compxo:
        print("Computer wins! Sorry!")
        gameover = True   
    elif table[61] == table[168] == table[275] == xo:               #diagonal left to right
        print("You win! Congrats!")
        gameover = True
    elif table[61] == table[168] == table[275] == compxo:
        print("Computer wins! Sorry!")
        gameover = True
    elif table.find('1') == -1 and table.find('2') == -1 and table.find('3') == -1 and table.find('4') == -1 and table.find('5') == -1 and table.find('6') == -1 and table.find('7') == -1 and table.find('8') == -1 and table.find('9') == -1 and gameover == False:
        print("Tie Game, Try Again!")
        gameover = True   
    return gameover

def playagain():
    playagain = input("Press Y to play again, N to exit = ")
    while playagain != 'Y' or 'N':
        if playagain == 'Y':
            printheader()
            return False
        elif playagain == 'N':
            print()
            print("Thanks for playing!")
            print()
            return True
        else:
           print("Please enter Y or N")
           playagain = input()
               


# main

table = draw()
gameover = False
printheader()
xo = userxo()
compxo = computerxo(xo)

while not gameover:    
    table = usermove(xo)
    gameover = checkwin(xo, compxo, table)                     #check after user move                  
    if gameover == True:
        gameover = playagain()
        if gameover == True:                            #dont play again
            sys.exit()
        if gameover == False:                           #play again
            table = draw()
          
    table = computermove(compxo)
    gameover = checkwin(xo, compxo, table)                     #check after computer move
    if gameover == True:
        gameover = playagain()
        if gameover == True:                            #dont play again
            sys.exit()
        if gameover == False:                           #play again
            table = draw()
            
            





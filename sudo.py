import os
import time
import random

table1 = [[5, 0, 0, 6, 0, 0, 9, 0, 3],
          [0, 3, 0, 0, 0, 1, 0, 7, 0],
          [2, 0, 1, 0, 3, 4, 8, 0, 0],
          [0, 9, 3, 0, 0, 0, 0, 0, 6],
          [0, 0, 6, 0, 1, 0, 3, 0, 0],
          [7, 0, 0, 0, 0, 0, 4, 9, 0],
          [0, 0, 5, 4, 7, 0, 1, 0, 9],
          [0, 1, 0, 8, 0, 0, 0, 4, 0],
          [8, 0, 4, 0, 0, 6, 0, 0, 7]]

table2 = [[7, 0, 0, 0, 0, 0, 1, 5, 0],
          [0, 0, 9, 0, 0, 0, 7, 0, 6],
          [0, 0, 0, 0, 8, 0, 0, 9, 0],
          [0, 2, 0, 9, 0, 1, 0, 0, 0],
          [0, 0, 3, 0, 5, 0, 4, 0, 0],
          [0, 0, 0, 8, 0, 4, 0, 6, 0],
          [0, 5, 0, 0, 7, 0, 0, 0, 0],
          [9, 0, 8, 0, 0, 0, 3, 0, 0],
          [0, 3, 4, 0, 0, 0, 0, 0, 2]]

table3 = [[6, 7, 0, 0, 0, 8, 0, 9, 3],
          [1, 0, 0, 3, 0, 4, 0, 0, 7],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 5, 0, 9, 0, 1, 0, 3, 0],
          [0, 0, 0, 0, 4, 0, 0, 0, 0],
          [0, 1, 0, 8, 0, 5, 0, 7, 4],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [3, 0, 0, 4, 0, 9, 0, 0, 1],
          [5, 4, 0, 7, 0, 0, 0, 8, 2]]

# numbers for deleting
tablefix1 = [[5, 0, 0, 6, 0, 0, 9, 0, 3],
             [0, 3, 0, 0, 0, 1, 0, 7, 0],
             [2, 0, 1, 0, 3, 4, 8, 0, 0],
             [0, 9, 3, 0, 0, 0, 0, 0, 6],
             [0, 0, 6, 0, 1, 0, 3, 0, 0],
             [7, 0, 0, 0, 0, 0, 4, 9, 0],
             [0, 0, 5, 4, 7, 0, 1, 0, 9],
             [0, 1, 0, 8, 0, 0, 0, 4, 0],
             [8, 0, 4, 0, 0, 6, 0, 0, 7]]

tablefix2 = [[7, 0, 0, 0, 0, 0, 1, 5, 0],
             [0, 0, 9, 0, 0, 0, 7, 0, 6],
             [0, 0, 0, 0, 8, 0, 0, 9, 0],
             [0, 2, 0, 9, 0, 1, 0, 0, 0],
             [0, 0, 3, 0, 5, 0, 4, 0, 0],
             [0, 0, 0, 8, 0, 4, 0, 6, 0],
             [0, 5, 0, 0, 7, 0, 0, 0, 0],
             [9, 0, 8, 0, 0, 0, 3, 0, 0],
             [0, 3, 4, 0, 0, 0, 0, 0, 2]]

tablefix3 = [[6, 7, 0, 0, 0, 8, 0, 9, 3],
             [1, 0, 0, 3, 0, 4, 0, 0, 7],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [7, 5, 0, 9, 0, 1, 0, 3, 0],
             [0, 0, 0, 0, 4, 0, 0, 0, 0],
             [0, 1, 0, 8, 0, 5, 0, 7, 4],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 0, 0, 4, 0, 9, 0, 0, 1],
             [5, 4, 0, 7, 0, 0, 0, 8, 2]]

# completed boards
tablefull1 = [[5, 4, 8, 6, 2, 7, 9, 1, 3],
              [6, 3, 9, 5, 8, 1, 2, 7, 4],
              [2, 7, 1, 9, 3, 4, 8, 6, 5],
              [1, 9, 3, 2, 4, 8, 7, 5, 6],
              [4, 5, 6, 7, 1, 9, 3, 2, 8],
              [7, 8, 2, 3, 6, 5, 4, 9, 1],
              [3, 6, 5, 4, 7, 2, 1, 8, 9],
              [9, 1, 7, 8, 5, 3, 6, 4, 2],
              [8, 2, 4, 1, 9, 6, 5, 3, 7]]

tablefull2 = [[7, 4, 2, 6, 9, 3, 1, 5, 8],
              [1, 8, 9, 2, 4, 5, 7, 3, 6],
              [3, 6, 5, 1, 8, 7, 2, 9, 4],
              [4, 2, 6, 9, 3, 1, 5, 8, 7],
              [8, 9, 3, 7, 5, 6, 4, 2, 1],
              [5, 1, 7, 8, 2, 4, 9, 6, 3],
              [2, 5, 1, 3, 7, 8, 6, 4, 9],
              [9, 7, 8, 4, 6, 2, 3, 1, 5],
              [6, 3, 4, 5, 1, 9, 8, 7, 2]]

tablefull3 = [[6, 7, 2, 1, 5, 8, 4, 9, 3],
              [1, 8, 5, 3, 9, 4, 6, 2, 7],
              [4, 9, 3, 6, 7, 2, 8, 1, 5],
              [7, 5, 4, 9, 6, 1, 2, 3, 8],
              [9, 3, 8, 2, 4, 7, 1, 5, 6],
              [2, 1, 6, 8, 3, 5, 9, 7, 4],
              [8, 6, 1, 5, 2, 3, 7, 4, 9],
              [3, 2, 7, 4, 8, 9, 5, 6, 1],
              [5, 4, 9, 7, 1, 6, 3, 8, 2]]


def clear():
    '''Clears the board'''
    os.system('cls' if os.name == 'nt' else 'clear')


def name_asker():
    '''Asks user name'''
    global name
    name = input('This is a simple sudoku game! Dear Guest, please enter you name!')


def startscreen():
    '''Startscreen with 3 options'''
    while True:
        clear()
        start = input('''\n If you want to know more about the RULES, please enter: rules!
        \n If you want to PLAY the game, please enter: play!
        \n If you want to EXIT from the game, please enter: exit!''')
        if start == "play":
            return
        if start == "rules":
            clear()
            print('''Fill a number in to every cell in the grid, using the numbers 1 to 9.
           \nYou can only use each number once in each row, each column, and in each of the 3×3 boxes!
           \nThe valid enters are for example: 123 (to enter a number) OR D12 (to delete a number)
           \nUppercase and lowercase letters are also accepted
           \nYou can exit if you enter <exit> instead of 3 values
           \nIf a number is a correct value on the right place, it turns yellow!''')
            time.sleep(4)
            continue
        if start == "exit":
            quit()


def game_chooser():
    '''It chooses a board randomly'''
    global table
    global tablefix
    global tablefull
    games = random.randint(0, 2)
    if games == 0:
        table = table1
        tablefix = tablefix1
        tablefull = tablefull1
        return
    elif games == 1:
        table = table2
        tablefix = tablefix2
        tablefull = tablefull2
        return
    elif games == 2:
        table = table3
        tablefix = tablefix3
        tablefull = tablefull3
        return


def initialize():
    '''Replaces the table elements containing zero with a dot'''
    print(table)
    for i in range(0, 9):
        for j in range(0, 9):
            if table[i][j] == 0:
                table[i][j] = "."


def draw():
    '''Draws the sudoku and calls the refresh function when finished'''
    clear()
    colorclose = "\x1b[0m"
    colorg = "\033[1;32m"
    colorw = "\033[1;37m"
    colorr = "\033[1;31m"
    colory = "\033[1;33m"
    print(colorg + "  | 1 2 3 | 4 5 6 | 7 8 9 |" + colorclose)
    print("---" * 9)
    counter = 1
    for row in range(0, len(table)):
        if row == 3 or row == 6:
            print("---" * 9)
        print(colorg + str(counter) + colorclose + " | ", end="")
        for column in range(0, len(table[0])):
            if column == 3 or column == 6:
                print("| ", end="")
            if table[row][column] == tablefull[row][column] and table[row][column] != tablefix[row][column]:
                print(colory + str(table[row][column]) + colorclose + " ", end="")
            elif tablefix[row][column] == 0:
                print(colorw + str(table[row][column]) + colorclose + " ", end="")
            else:
                print(colorr + str(table[row][column]) + colorclose + " ", end="")
        counter += 1
        print("|")
    print("---" * 9)
    refresh()


def refresh():
    '''Refreshes the console output'''
    while str(table) != str(tablefull):
        if "." not in str(table):
            fulltable_handling()
        input_handling()
    fulltable_handling()


def input_handling():
    '''Checks the input and updated the table if the input is valid'''
    rcnlist = []
    while True:
        rcnlist = input('''TO DELETE: D[rows][columns]
        \nTO ENTER: [rows][columns][number to write]! ''')
        if rcnlist == "exit":
            quit()
        else:
            rcnlist = space_handling(rcnlist)
        rcnlist = input_check(rcnlist)
        enter_execution(rcnlist)


def space_handling(rowcolnum):
    '''Fills a new list with only the elements of the input without spaces and returns with it'''
    rcn_list = []
    for i in range(len(rowcolnum)):
        if rowcolnum[i] != " ":
            rcn_list.append(rowcolnum[i])
    return rcn_list


def input_check(rawstring):
    '''Checks the rawstring whether it\'s to delete or to enter'''
    if len(rawstring) != 3:
        print("Please enter only 3 value!")
        time.sleep(2)
        draw()
    elif rawstring[0].lower() == "d":
        rawstring[0] = "d"
        rawstring.remove("d")
        rawstring = int_string(rawstring)
        delete_execution(rawstring)
    else:
        rawstring = int_string(rawstring)
        return rawstring


def int_string(listinput):
    '''Converts the list to contain only integers'''
    for i in range(len(listinput)):
        if listinput[i].isdigit() != True:
            print('Please enter numbers!')
            time.sleep(2)
            input_handling()
        else:
            listinput[i] = int(listinput[i])
    return listinput


def fixnumber_handling():
    '''Handles fixed numbers'''
    print('It\'s a fix number, enter or delete another!')
    time.sleep(2)
    draw()


def enter_execution(rcnlist):
    '''From the given input it checks the table and enters the element if it\'s not a fixed one'''
    while True:
        if table[(rcnlist[0]) - 1][(rcnlist[1]) - 1] == ".":
            table[(rcnlist[0]) - 1][(rcnlist[1]) - 1] = rcnlist[2]
            draw()
        else:
            fixnumber_handling()


def delete_execution(drcnlist):
    '''From the given input it checks the table and deletes the element if it\'s not a fixed one'''
    while True:
        if tablefix[drcnlist[0] - 1][drcnlist[1] - 1] == 0:
            table[(drcnlist[0]) - 1][(drcnlist[1]) - 1] = "."
            draw()
        else:
            fixnumber_handling()


def fulltable_handling():
    '''Checks the full table if it contains the good solution'''
    answer = input('Have you finished ' + name + '? Enter yes or no!')
    # if answer == "yes" :
    if str(table) != str(tablefull):
        print('Sorry, ' + name + '! You haven\'t finished yet! Try again!')
        return
    elif str(table) == str(tablefull):
        print('You\'ve already finished ' + name + '!')
        time.sleep(2)
    else:
        return
    clear()
    print(('\nWell done ' + name + '!') * 10)
    quit()


def main():
    clear()
    name_asker()
    startscreen()
    game_chooser()
    initialize()
    draw()
    refresh()


'''Program starts here'''
main()

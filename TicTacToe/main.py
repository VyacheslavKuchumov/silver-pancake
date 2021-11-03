import os
import sys
RUN = True

a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' '
turn = 1
while RUN:

    os.system('cls')
    print(f"  1 2 3\nA {a1}|{a2}|{a3}\nB {b1}|{b2}|{b3}\nC {c1}|{c2}|{c3}\n")

    choice = input()

    if choice == 'q':
        RUN = False
    if choice == 'a1':
        if turn % 2 != 0:
            a1 = 'X'
        else:
            a1 = 'O'
    if choice == 'a2':
        if turn % 2 != 0:
            a2 = 'X'
        else:
            a2 = 'O'
    if choice == 'a3':
        if turn % 2 != 0:
            a3 = 'X'
        else:
            a3 = 'O'
    if choice == 'b1':
        if turn % 2 != 0:
            b1 = 'X'
        else:
            b1 = 'O'
    if choice == 'b2':
        if turn % 2 != 0:
            b2 = 'X'
        else:
            b2 = 'O'
    if choice == 'b3':
        if turn % 2 != 0:
            b3 = 'X'
        else:
            b3 = 'O'
    if choice == 'b3':
        if turn % 2 != 0:
            b3 = 'X'
        else:
            b3 = 'O'
    if choice == 'c1':
        if turn % 2 != 0:
            c1 = 'X'
        else:
            c1 = 'O'
    if choice == 'c2':
        if turn % 2 != 0:
            c2 = 'X'
        else:
            c2 = 'O'
    if choice == 'c3':
        if turn % 2 != 0:
            c3 = 'X'
        else:
            c3 = 'O'

    if a1 == a2 == a3 == 'X' or a1 == b2 == c3 == 'X' or c1 == b2 == a3 == 'X' or b1 == b2 == b3 == 'X' or c1 == c2 == c3 == 'X' or a1 == b1 == c1 == 'X' or a2 == b2 == c2 == 'X' or a3 == b2 == b3 == 'X':
        RUN = False
        os.system('cls')
        print('X won')
    if a1 == a2 == a3 == 'O' or a1 == b2 == c3 == 'O' or c1 == b2 == a3 == 'O' or b1 == b2 == b3 == 'O' or c1 == c2 == c3 == 'O' or a1 == b1 == c1 == 'O' or a2 == b2 == c2 == 'O' or a3 == b2 == b3 == 'O':
        RUN = False
        os.system('cls')
        print('O won')

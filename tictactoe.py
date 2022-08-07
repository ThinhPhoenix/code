# LIVESTREAM MAKING TIC TAC TOE GAME // PHOENIZ
# GIVE ME A LIKE AND SUBSCRIBE SO THAT I CAN KEEP DOING LIVESTREAM FOR YOU GUYS
from random import randrange
from time import sleep


a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
print(a, b, c)  # Print table
print(d, e, f)
print(g, h, i)
space = 0
turn = 1
bot_on = False
gamemode = 0
botloop = False

while True:
    sleep(0.5)
    turn = turn + 1
    if bot_on == False and gamemode == 0:
        gamemode = int(input("Please choose gamemode (1)vsBot, (2)PvP: "))
        if gamemode == 1:
            bot_on = True
            continue
        elif gamemode == 2:
            continue
    elif bot_on == True and gamemode == 1:  # PvBot

        if space == 9:
            space = 0
            print("Draw! Continue again.")
            a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
            print(a, b, c)  # Print table
            print(d, e, f)
            print(g, h, i)

        if turn % 2 == 0:
            botmove = randrange(1, 10)
            space = space + 1

            if botmove == 1 and a == "_":
                botloop = False
                print("X move:", botmove)
                a = "x"
            elif botmove == 2 and b == "_":
                botloop = False
                print("X move:", botmove)
                b = "x"
            elif botmove == 3 and c == "_":
                botloop = False
                print("X move:", botmove)
                c = "x"
            elif botmove == 4 and d == "_":
                botloop = False
                print("X move:", botmove)
                d = "x"
            elif botmove == 5 and e == "_":
                botloop = False
                print("X move:", botmove)
                e = "x"
            elif botmove == 6 and f == "_":
                botloop = False
                print("X move:", botmove)
                f = "x"
            elif botmove == 7 and g == "_":
                botloop = False
                print("X move:", botmove)
                g = "x"
            elif botmove == 8 and h == "_":
                botloop = False
                print("X move:", botmove)
                h = "x"
            elif botmove == 9 and i == "_":
                botloop = False
                print("X move:", botmove)
                i = "x"
            else:
                space = space - 1
                turn = turn - 1
                botloop = True

            if botloop == False:
                print(a, b, c)
                print(d, e, f)
                print(g, h, i)
            elif botloop == True:
                continue

            if a == "x" and b == "x" and c == "x":  # con1
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break
            elif d == "x" and e == "x" and f == "x":  # con2
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif g == "x" and h == "x" and i == "x":  # con3
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "x" and d == "x" and g == "x":  # con4
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif b == "x" and e == "x" and h == "x":  # con5
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "x" and f == "x" and i == "x":  # con6
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "x" and e == "x" and i == "x":  # con7
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "x" and e == "x" and g == "x":  # con8
                print("You lost")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

        else:
            o = int(input("O move: "))
            space = space + 1

            if o == 1 and a == "_":
                a = "o"
            elif o == 2 and b == "_":
                b = "o"
            elif o == 3 and c == "_":
                c = "o"
            elif o == 4 and d == "_":
                d = "o"
            elif o == 5 and e == "_":
                e = "o"
            elif o == 6 and f == "_":
                f = "o"
            elif o == 7 and g == "_":
                g = "o"
            elif o == 8 and h == "_":
                h = "o"
            elif o == 9 and i == "_":
                i = "o"
            else:
                print("That place is already taken! Choose another place.")
                turn = turn - 1
                space = space - 1

            print(a, b, c)  # Print table
            print(d, e, f)
            print(g, h, i)

            if a == "o" and b == "o" and c == "o":  # con1
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break
            elif d == "o" and e == "o" and f == "o":  # con2
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif g == "o" and h == "o" and i == "o":  # con3
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "o" and d == "o" and g == "o":  # con4
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif b == "o" and e == "o" and h == "o":  # con5
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "o" and f == "o" and i == "o":  # con6
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "o" and e == "o" and i == "o":  # con7
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "o" and e == "o" and g == "o":  # con8
                print("You won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    botloop = False
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

    elif bot_on == False:  # PvP

        if space == 9:
            space = 0
            print("Draw! Continue again.")
            a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
            print(a, b, c)  # Print table
            print(d, e, f)
            print(g, h, i)

        if turn % 2 == 0:
            x = int(input("X move: "))
            space = space + 1

            if x == 1 and a == "_":
                a = "x"
            elif x == 2 and b == "_":
                b = "x"
            elif x == 3 and c == "_":
                c = "x"
            elif x == 4 and d == "_":
                d = "x"
            elif x == 5 and e == "_":
                e = "x"
            elif x == 6 and f == "_":
                f = "x"
            elif x == 7 and g == "_":
                g = "x"
            elif x == 8 and h == "_":
                h = "x"
            elif x == 9 and i == "_":
                i = "x"
            else:
                print("That place is already taken! Choose another place.")
                turn = turn - 1
                space = space - 1

            print(a, b, c)  # Print table
            print(d, e, f)
            print(g, h, i)

            if a == "x" and b == "x" and c == "x":  # con1
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break
            elif d == "x" and e == "x" and f == "x":  # con2
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif g == "x" and h == "x" and i == "x":  # con3
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "x" and d == "x" and g == "x":  # con4
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif b == "x" and e == "x" and h == "x":  # con5
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "x" and f == "x" and i == "x":  # con6
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "x" and e == "x" and i == "x":  # con7
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "x" and e == "x" and g == "x":  # con8
                print("X won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

        else:
            o = int(input("O move: "))
            space = space + 1

            if o == 1 and a == "_":
                a = "o"
            elif o == 2 and b == "_":
                b = "o"
            elif o == 3 and c == "_":
                c = "o"
            elif o == 4 and d == "_":
                d = "o"
            elif o == 5 and e == "_":
                e = "o"
            elif o == 6 and f == "_":
                f = "o"
            elif o == 7 and g == "_":
                g = "o"
            elif o == 8 and h == "_":
                h = "o"
            elif o == 9 and i == "_":
                i = "o"
            else:
                print("That place is already taken! Choose another place.")
                turn = turn - 1
                space = space - 1

            print(a, b, c)  # Print table
            print(d, e, f)
            print(g, h, i)

            if a == "o" and b == "o" and c == "o":  # con1
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break
            elif d == "o" and e == "o" and f == "o":  # con2
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif g == "o" and h == "o" and i == "o":  # con3
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "o" and d == "o" and g == "o":  # con4
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif b == "o" and e == "o" and h == "o":  # con5
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "o" and f == "o" and i == "o":  # con6
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif a == "o" and e == "o" and i == "o":  # con7
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

            elif c == "o" and e == "o" and g == "o":  # con8
                print("O won")
                temp = str(input("Do you wanna continue?(y/n)"))
                if temp == "y":
                    a, b, c, d, e, f, g, h, i = "_", "_", "_", "_", "_", "_", "_", "_", "_"
                    print(a, b, c)  # Print table
                    print(d, e, f)
                    print(g, h, i)
                    space = 0
                    turn = 1
                    bot_on = False
                    gamemode = 0
                    continue
                elif temp == "n":
                    print("Thanks for playing.")
                    break

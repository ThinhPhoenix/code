from random import randrange

gametable = {
    1: '_', 2: '_', 3: '_',
    4: '_', 5: '_', 6: '_',
    7: '_', 8: '_', 9: '_'
}
turn = 1
gamemode = None
game_continue = True
space = 0
bmove = None


def update_table(temp):
    global gametable, turn, space
    if turn % 2 == 0:
        who = 'x'
    else:
        who = 'o'
    gametable.update({temp: who})


def bot_move():
    global bmove, gametable, space, turn
    bmove = randrange(1, 10)
    if gametable[bmove] == '_':
        update_table(bmove)
        print(f"Bot move: {bmove}")
        print((gametable[1], gametable[2], gametable[3]), '\n',
              (gametable[4], gametable[5], gametable[6]), '\n',
              (gametable[7], gametable[8], gametable[9]), sep='')
    else:
        bot_move()


def win_cases():
    global gametable, turn
    if turn % 2 == 0:
        who = 'O'
    else:
        who = 'X'
    if gametable[1] == gametable[2] == gametable[3] != '_':
        print(f"{who} win!")
        tieptuc(str(input("Do you wanna continue?(y/n) ")))
    elif gametable[4] == gametable[5] == gametable[6] != '_':
        print(f"{who} win!")
        tieptuc(str(input("Do you wanna continue?(y/n) ")))
    elif gametable[7] == gametable[8] == gametable[9] != '_':
        print(f"{who} win!")
        tieptuc(str(input("Do you wanna continue?(y/n) ")))
    elif gametable[1] == gametable[5] == gametable[9] != '_':
        print(f"{who} win!")
        tieptuc(str(input("Do you wanna continue?(y/n) ")))
    elif gametable[7] == gametable[5] == gametable[3] != '_':
        print(f"{who} win!")
        tieptuc(str(input("Do you wanna continue?(y/n) ")))


def tieptuc(temp):
    global game_continue, gamemode, gametable, turn, space
    match temp:
        case 'y' | 'Y':
            print("You chose to continue.")
            gametable = {
                1: '_', 2: '_', 3: '_',
                4: '_', 5: '_', 6: '_',
                7: '_', 8: '_', 9: '_'
            }
            turn = 1
            gamemode = None
            space = 0
        case 'n' | 'N':
            print("Thanks for playing!")
            game_continue = False
        case _:
            print("Error, just type 'y' or 'n' only.")
            tieptuc(str(input("Do you wanna continue?(y/n) ")))


while game_continue:
    turn += 1
    if space == 9:
        print("Draw!")
        space = 0
        gametable = {
            1: '_', 2: '_', 3: '_',
            4: '_', 5: '_', 6: '_',
            7: '_', 8: '_', 9: '_'
        }
        print((gametable[1], gametable[2], gametable[3]), '\n',
              (gametable[4], gametable[5], gametable[6]), '\n',
              (gametable[7], gametable[8], gametable[9]), sep='')
    win_cases()
    match gamemode:
        case None:
            gamemode = str(input("Enter gamemode [bot], [pvp]: "))
            turn -= 1
            if gamemode == 'bot' or gamemode == 'pvp':
                print((gametable[1], gametable[2], gametable[3]), '\n',
                      (gametable[4], gametable[5], gametable[6]), '\n',
                      (gametable[7], gametable[8], gametable[9]), sep='')
        case 'bot':
            if turn % 2 == 0:
                moving = int(input("Your move: "))
                if gametable[moving] == '_':
                    space += 1
                    update_table(moving)
                    print((gametable[1], gametable[2], gametable[3]), '\n',
                          (gametable[4], gametable[5], gametable[6]), '\n',
                          (gametable[7], gametable[8], gametable[9]), sep='')
                else:
                    print("Your place had been taken!")
                    turn -= 1
            else:
                bmove = randrange(1, 10)
                if gametable[bmove] == '_':
                    space += 1
                    update_table(bmove)
                    print(f"Bot move: {bmove}")
                    print((gametable[1], gametable[2], gametable[3]), '\n',
                          (gametable[4], gametable[5], gametable[6]), '\n',
                          (gametable[7], gametable[8], gametable[9]), sep='')
                else:
                    turn -= 1
        case 'pvp':
            if turn % 2 == 0:
                who = 'X'
            else:
                who = 'O'
            moving = int(input(f"{who} move: "))
            if gametable[moving] == '_':
                space += 1
                update_table(moving)
                print((gametable[1], gametable[2], gametable[3]), '\n',
                      (gametable[4], gametable[5], gametable[6]), '\n',
                      (gametable[7], gametable[8], gametable[9]), sep='')
            else:
                print("Your place had been taken!")
                turn -= 1
        case _:
            print("Error, type 'bot' or 'pvp' only.")
            turn -= 1
            gamemode = None
            continue

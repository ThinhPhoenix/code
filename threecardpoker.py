from random import choice
import os
bo_bai = [
    "1♥", "1♦", "1♣", "1♠",
    "2♥", "2♦", "2♣", "2♠",
    "3♥", "3♦", "3♣", "3♠",
    "4♥", "4♦", "4♣", "4♠",
    "5♥", "5♦", "5♣", "5♠",
    "6♥", "6♦", "6♣", "6♠",
    "7♥", "7♦", "7♣", "7♠",
    "8♥", "8♦", "8♣", "8♠",
    "9♥", "9♦", "9♣", "9♠",
    "10♥", "10♦", "10♣", "10♠",
    "J♥", "J♦", "J♣", "J♠",
    "Q♥", "Q♦", "Q♣", "Q♠",
    "K♥", "K♦", "K♣", "K♠",
]

turn = None
you_cards = []
bot_cards = []
game_continue = True


def tieptuc(temp):
    global turn, game_continue
    match temp:
        case 'y' | 'Y':
            print("You chose to continue game.")
            reset()
            os.system('cls')  # windows clear terminal
            os.system('clear')  # mac&linux clear teminal
        case 'n' | 'N':
            print("Thanks for playing!")
            game_continue = False
        case _:
            print("Error, just type 'y' or 'n' only!")
            return tieptuc(str(input("Do you wanna continue?(y/n) ")))


def reset():
    global turn, bo_bai, you_cards, bot_cards
    bo_bai = [
        "1♥", "1♦", "1♣", "1♠",
        "2♥", "2♦", "2♣", "2♠",
        "3♥", "3♦", "3♣", "3♠",
        "4♥", "4♦", "4♣", "4♠",
        "5♥", "5♦", "5♣", "5♠",
        "6♥", "6♦", "6♣", "6♠",
        "7♥", "7♦", "7♣", "7♠",
        "8♥", "8♦", "8♣", "8♠",
        "9♥", "9♦", "9♣", "9♠",
        "10♥", "10♦", "10♣", "10♠",
        "J♥", "J♦", "J♣", "J♠",
        "Q♥", "Q♦", "Q♣", "Q♠",
        "K♥", "K♦", "K♣", "K♠",
    ]
    turn = None
    you_cards = []
    bot_cards = []


while game_continue:

    if turn == None:
        chose = str(input("Enter [heads] or [tails]: "))
        if chose == "heads" or chose == "tails":
            coinface = ["heads", "tails"]
            coin = choice(coinface)
            if chose == coin:
                print("Card will be dealt to you first!")
                turn = "you"
            else:
                print("Card will be dealt to bot first!")
                turn = "bot"
        else:
            print("Error, just type [heads] or [tails] only.")

    else:
        if turn == "you":
            for _ in range(3):
                dealer = choice(bo_bai)
                you_cards.append(dealer)
                bo_bai.remove(dealer)

                dealer = choice(bo_bai)
                bot_cards.append(dealer)
                bo_bai.remove(dealer)

            print("You: ", you_cards, "\n", "Bot: ", bot_cards, sep="")
        elif turn == "bot":
            for _ in range(3):
                dealer = choice(bo_bai)
                bot_cards.append(dealer)
                bo_bai.remove(dealer)

                dealer = choice(bo_bai)
                you_cards.append(dealer)
                bo_bai.remove(dealer)

            print("You: ", you_cards, "\n", "Bot: ", bot_cards, sep="")

    if len(you_cards) == 3 & len(bot_cards) == 3:
        for i in range(3):
            if you_cards[i][0] == "J" or you_cards[i][0] == "Q" or you_cards[i][0] == "K" or you_cards[i][1] == "0":
                you_cards[i] = 10
            else:
                you_cards[i] = int(you_cards[i][0])

            if bot_cards[i][0] == "J" or bot_cards[i][0] == "Q" or bot_cards[i][0] == "K" or bot_cards[i][1] == "0":
                bot_cards[i] = 10
            else:
                bot_cards[i] = int(bot_cards[i][0])

        yourscore = str(you_cards[0] + you_cards[1] + you_cards[2])[1]
        yourscore = int(yourscore)

        botscore = str(bot_cards[0] + bot_cards[1] + bot_cards[2])[1]
        botscore = int(botscore)

        if yourscore > botscore:
            print("You win!")
            tieptuc(str(input("Do you wanna continue?(y/n) ")))
        elif yourscore < botscore:
            print("Bot win!")
            tieptuc(str(input("Do you wanna continue?(y/n) ")))
        else:
            print("Draw!")
            tieptuc(str(input("Do you wanna continue?(y/n) ")))

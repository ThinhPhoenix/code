from random import choice

def tieptuc(temp):
    match temp:
        case 'y'|'Y':
            print("You chose to continue game.")
            main()
        case 'n'|'N':
            print("Thanks for playing!")
        case _:
            print("Error, just type 'y' or 'n' only!")
            return tieptuc(str(input("Do you wanna continue?(y/n) ")))

def main():
    player = str(input("Enter [rock], [paper], [scissors]: "))
    choose = ['rock','paper','scissors']
    bot = choice(choose)

    print(f"You chose: {player}\nBot chose: {bot}")
    
    match player:
        case 'rock':
            if bot == 'scissors':
                print("You win!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
            else:
                print("You lose!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
        case 'paper':
            if bot == 'rock':
                print("You win!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
            else:
                print("You lose!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
        case 'scissors':
            if bot == 'paper':
                print("You win!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
            else:
                print("You lose!")
                tieptuc(str(input("Do you wanna continue?(y/n) ")))
        case _:
            print("Tie!")
            tieptuc(str(input("Dp you wanna continue? (y/n) ")))

main()
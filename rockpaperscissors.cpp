#include <iostream>
#include <string>
#include <time.h>
#include <stdlib.h>
using namespace std;

bool continue_game = true;

void tieptuc()
{
    std::cout << "Do you wanna continue?(y/n) ";
    char temp;
    std::cin >> temp;
    switch (temp)
    {
    case 'y':
    case 'Y':
        std::cout << "You chose to continue.\n";
        break;
    case 'n':
    case 'N':
        std::cout << "Thanks for playing!\n";
        continue_game = false;
        break;
    default:
        std::cout << "Error, just type 'y' or 'n' only!\n";
        tieptuc();
        break;
    }
}

int main()

{
    std::string player;
    std::string bot;
    std::string types[3] = {
        "rock",
        "paper",
        "scissors"
    };

    while (continue_game)
    {
        std::cout << "Enter [rock], [paper], [scissors]: ";
        std::cin >> player;

        srand(time(NULL));
        int randomnumber;
        randomnumber = rand() % 3;
        bot = (types[randomnumber]);

        std::cout << "You chose: " << player << "\nBot chose: " << bot << std::endl;

        if (player == bot)
        {
            std::cout << "Tie!\n";
            tieptuc();
        }
        else if (player == "rock")
        {
            if (bot == "scissors")
            {
                std::cout << "You win!\n";
                tieptuc();
            }
            else
            {
                std::cout << "You lose!\n";
                tieptuc();
            }
        }
        else if (player == "paper")
        {
            if (bot == "rock")
            {
                std::cout << "You win!\n";
                tieptuc();
            }
            else{
                std::cout << "You lose!\n";
                tieptuc();
            }
        }
        else if (player == "scissors")
        {
            if (bot == "paper")
            {
                std::cout << "You win!\n";
                tieptuc();
            }
            else
            {
                std::cout << "You lose!\n";
                tieptuc();
            }
        }
    }
    return 0;
}
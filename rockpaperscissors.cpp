#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
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
        continue_game = true;
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

    const char *choice[] = {
        "rock",
        "paper",
        "scisscors",
    };
    int table_size = 3;

    while (continue_game)
    {
        std::cout << "Enter [rock], [paper], [scissors]: ";
        std::cin >> player;
        srand(time(NULL));
        const char *bot = choice[rand() % table_size];

        std::cout << "You chose: " << player << "\nBot chose: ";
        printf("%s\n", bot);

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
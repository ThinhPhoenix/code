#include <iostream>
#include <string>
#include <time.h>
#include <stdlib.h>
using namespace std;

std::string gamemode = "0";
bool game_continue = true;
int turn = 1;
int space = 0;
int bmove = 0;
std::string who;

std::string gametable[9] = {
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_"};

void printtable()
{
    std::cout << "( " << gametable[0] << ", " << gametable[1] << ", " << gametable[2] << ")\n"
              << "( " << gametable[3] << ", " << gametable[4] << ", " << gametable[5] << ")\n"
              << "( " << gametable[6] << ", " << gametable[7] << ", " << gametable[8] << ")\n";
}

void update_table(int temp)
{
    if (turn % 2 == 0)
    {
        gametable[temp] = 'x';
    }
    else
    {
        gametable[temp] = 'o';
    }
}

void tieptuc()
{
    std::cout << "Do you wanna continue?(y/n) ";
    char temp;
    std::cin >> temp;
    switch (temp)
    {
    case 'y':
    case 'Y':
        for (int i = 0; i < 9; i++)
        {
            gametable[i] = '_';
        }
        turn = 1;
        space = 0;
        bmove = 0;
        gamemode = "0";

        std::cout << "You chose to continue.\n";
        break;
    case 'n':
    case 'N':
        std::cout << "Thanks for playing!\n";
        gamemode = "stop";
        game_continue = false;
        break;
    default:
        std::cout << "Error, just type 'y' or 'n' only!\n";
        tieptuc();
        break;
    }
}

void win_cases()
{
    std::string player;
    if (turn % 2 != 0)
    {
        if (gamemode == "bot")
        {
            player = "Bot";
        }
        else
        {
            player = "O";
        }
    }
    else
    {
        if (gamemode == "bot")
        {
            player = "You";
        }
        else
        {
            player = "X";
        }
    }
    if (gametable[0] == gametable[1] && gametable[1] == gametable[2] && gametable[2] != "_")
    {
        std::cout << player << " Win!" << std::endl;
        tieptuc();
    }

    else if (gametable[3] == gametable[4] && gametable[4] == gametable[5] && gametable[5] != "_")
    {
        std::cout << player << " Win!" << std::endl;
        tieptuc();
    }

    else if (gametable[6] == gametable[7] && gametable[7] == gametable[8] && gametable[8] != "_")
    {
        std::cout << player << " Win!" << std::endl;
        tieptuc();
    }

    else if (gametable[0] == gametable[4] && gametable[4] == gametable[8] && gametable[8] != "_")
    {
        std::cout << player << " Win!" << std::endl;
        tieptuc();
    }

    else if (gametable[6] == gametable[4] && gametable[4] == gametable[2] && gametable[2] != "_")
    {
        std::cout << player << " Win!" << std::endl;
        tieptuc();
    }
}

int main()
{
    while (game_continue)
    {
        win_cases();
        if (space == 9)
        {
            cout << "Draw!\n";
            for (int i = 0; i < 9; i++)
            {
                gametable[i] = '_';
            }
            turn = 1;
            space = 0;
            bmove = 0;
            printtable();
        }

        turn++;

        if (gamemode == "0")
        {
            turn--;
            std::cout << "Enter gamemode [bot], [pvp]: ";
            std::cin >> gamemode;
            if (gamemode == "bot" or gamemode == "pvp")
            {
                printtable();
            }
        }
        else if (gamemode == "bot")
        {
            if (turn % 2 == 0)
            {
                int moving;
                std::cout << "Your move: ";
                std::cin >> moving;
                if (gametable[moving - 1] == "_")
                {
                    space++;
                    update_table(moving - 1);
                    printtable();
                }
                else
                {
                    std::cout << "Your place had been taken!\n";
                    turn--;
                }
            }
            else
            {
                srand(time(NULL));
                bmove = rand() % 9;
                if (gametable[bmove] == "_")
                {
                    space++;
                    update_table(bmove);
                    std::cout << "Bot move: " << bmove + 1 << "\n";
                    printtable();
                }
                else
                {
                    turn--;
                }
            }
        }
        else if (gamemode == "pvp")
        {
            if (turn % 2 == 0)
            {
                who = "X";
            }
            else
            {
                who = "O";
            }
            int moving;
            std::cout << who << " move: ";
            std::cin >> moving;
            if (gametable[moving - 1] == "_")
            {
                space++;
                update_table(moving - 1);
                printtable();
            }
            else
            {
                std::cout << "Your place had been taken!\n";
                turn--;
            }
        }
        else if (gamemode == "stop"){}
        else
        {
            cout << "Error, just type [bot] or [pvp] only.\n";
            turn--;
            gamemode = "0";
        }
    }
    return 0;
}

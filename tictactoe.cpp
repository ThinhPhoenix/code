#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

// variables
char a = '_';
char b = '_';
char c = '_';
char d = '_';
char e = '_';
char f = '_';
char g = '_';
char h = '_';
char i = '_';
int turn = 1;
int mov = 0;
int space = 0;
bool quit_game = false;

// def printboard()
void printboard()
{
    std::cout << a << " " << b << " " << c << "\n"
              << d << " " << e << " " << f << "\n"
              << g << " " << h << " " << i << "\n";
}

// winner finding functions
void win_case_x()
{
    if (a == 'x' and b == 'x' and c == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (d == 'x' and e == 'x' and f == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (g == 'x' and h == 'x' and i == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (a == 'x' and d == 'x' and g == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (b == 'x' and e == 'x' and h == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (c == 'x' and f == 'x' and i == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (a == 'x' and e == 'x' and i == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (c == 'x' and e == 'x' and g == 'x')
    {
        char temp;
        printf("X won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
}
void win_case_o()
{
    if (a == 'o' and b == 'o' and c == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (d == 'o' and e == 'o' and f == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (g == 'o' and h == 'o' and i == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (a == 'o' and d == 'o' and g == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (b == 'o' and e == 'o' and h == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (c == 'o' and f == 'o' and i == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (a == 'o' and e == 'o' and i == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
    else if (c == 'o' and e == 'o' and g == 'o')
    {
        char temp;
        printf("O won!\n");
        printf("Do you wanna continue? ");
        std::cin >> temp;
        if (temp == 'y' or temp == 'Y')
        {
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            turn = 1;
            mov = 0;
            space = 0;
            printboard();
        }
        else
        {
            printf("Thanks for playing!\n");
            quit_game = true;
        }
    }
}

int main()
{
    // while loop
    while (true)
    {

        // print board & turn += 1 & stop game if there are winner
        printboard();
        win_case_x();
        win_case_o();
        turn++;

        // quit game
        if (quit_game == true)
        {
            break;
        }

        // full space
        if (space == 9)
        {
            std::cout << "Draw! continue.\n";
            space = 0;
            a = '_';
            b = '_';
            c = '_';
            d = '_';
            e = '_';
            f = '_';
            g = '_';
            h = '_';
            i = '_';
            printboard();
        }

        // x turn
        if (turn % 2 == 0)
        {
            std::cout << "X move: ";
            std::cin >> mov;
            if (mov == 1 and a == '_')
            {
                a = 'x';
                space++;
            }
            else if (mov == 2 and b == '_')
            {
                b = 'x';
                space++;
            }
            else if (mov == 3 and c == '_')
            {
                c = 'x';
                space++;
            }
            else if (mov == 4 and d == '_')
            {
                d = 'x';
                space++;
            }
            else if (mov == 5 and e == '_')
            {
                e = 'x';
                space++;
            }
            else if (mov == 6 and f == '_')
            {
                f = 'x';
                space++;
            }
            else if (mov == 7 and g == '_')
            {
                g = 'x';
                space++;
            }
            else if (mov == 8 and h == '_')
            {
                h = 'x';
                space++;
            }
            else if (mov == 9 and i == '_')
            {
                i = 'x';
                space++;
            }
            else
            {
                std::cout << "Your place had been taken!\n";
                space--;
                turn--;
            }
        }

        // o turn
        else
        {
            std::cout << "O move: ";
            std::cin >> mov;
            if (mov == 1 and a == '_')
            {
                a = 'o';
                space++;
            }
            else if (mov == 2 and b == '_')
            {
                b = 'o';
                space++;
            }
            else if (mov == 3 and c == '_')
            {
                c = 'o';
                space++;
            }
            else if (mov == 4 and d == '_')
            {
                d = 'o';
                space++;
            }
            else if (mov == 5 and e == '_')
            {
                e = 'o';
                space++;
            }
            else if (mov == 6 and f == '_')
            {
                f = 'o';
                space++;
            }
            else if (mov == 7 and g == '_')
            {
                g = 'o';
                space++;
            }
            else if (mov == 8 and h == '_')
            {
                h = 'o';
                space++;
            }
            else if (mov == 9 and i == '_')
            {
                i = 'o';
                space++;
            }
            else
            {
                std::cout << "Your place had been taken!\n";
                space--;
                turn--;
            }
        }
    }
    return 0;
}

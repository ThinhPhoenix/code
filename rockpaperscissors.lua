local game_continue = true

function tieptuc()
    io.write("Do you wanna continue?(y/n) ");
    local temp = io.read()
    if temp == "y" or temp == "Y" then
    elseif temp == "n" or temp == "N" then
        game_continue = false
    else
        print("Error, just type 'y' or 'n' only.")
        tieptuc()
    end
end

while game_continue do
    local random_number = math.random(1, 3)
    local choice = { "rock", "paper", "scissors" }
    local bot = choice[random_number]
    io.write("Enter [rock], [paper], [scissors]: ");
    local you = io.read()
    if you == bot then
        io.write("You chose: ", you, "\nBot chose: ", bot, "\n")
        io.write("Tie!\n")
        tieptuc()
    elseif you == "rock" then
        io.write("You chose: ", you, "\nBot chose: ", bot, "\n")
        if bot == "scissors" then
            io.write("You win!\n")
            tieptuc()
        else
            io.write("You lose!\n")
            tieptuc()
        end
    elseif you == "paper" then
        io.write("You chose: ", you, "\nBot chose: ", bot, "\n")
        if bot == "rock" then
            io.write("You win!\n")
            tieptuc()
        else
            io.write("You lose!\n")
            tieptuc()
        end
    elseif you == "scissors" then
        io.write("You chose: ", you, "\nBot chose: ", bot, "\n")
        if bot == "paper" then
            io.write("You win!\n")
            tieptuc()
        else
            io.write("You lose!\n")
            tieptuc()
        end
    else
        print("Error, just type 'rock', 'paper', 'scissors' only.")
    end
end

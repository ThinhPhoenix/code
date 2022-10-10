io.write("What n? ")
local n = io.read()
local S = 1

function factorials(x)
    if x == 1 then
        io.write("Factorials of (", n, ") is ", S)
    else
        S = S * x
        factorials(x - 1)
    end
end

factorials(n)

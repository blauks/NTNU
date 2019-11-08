function usegreed(coins)
    # Din kode her
    for c in 1:length(coins) - 1
        if coins[c] % coins[c + 1] != 0
            return false
        end
    end
    return true
end

function mincoinsgreedy(coins, value)
    # Din kode her
    howMany = 0
    for c in coins
        if c <= value
            while c <= value
                howMany = howMany + 1 
                value = value - c
            end
        end
    end
    return howMany
end 

#println(mincoinsgreedy([1000,500,100,20,5,1], 8))

function mincoins(coins, value)
    # Om du ikke trenger inf kan du fjerne den
    inf = typemax(Int)
    # Din kode her
end
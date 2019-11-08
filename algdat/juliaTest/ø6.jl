function lislength(s)
    mls = ones(Int, size(s))
    mls[1] = 1
    q = 1
    for j in 2:length(s)
        q = 1
        for i in 1:j
            if s[j] > s[i] && mls[i] >= q
                q = mls[i] + 1
            end
        end
        mls[j] = q
    end
    println(mls)
    return maximum(mls) # Returnerer det største tallet i listen
end

#println(lislength([682, 52, 230, 441, 1000, 22, 678, 695, 0, 681]))

function lis(s, mls)
    ml = maximum(mls)
    lis = []
    for i = length(mls):-1:1
        if mls[i] == ml
            pushfirst!(lis, s[i])
            ml = ml - 1 
        end
    end
    return lis
end

#println(lis([5,3,3,6,7], [1,1,1,2,3]))

function cumulative(weights)
    rows, cols = size(weights)
    
end
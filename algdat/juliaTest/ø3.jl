# x og y er to sorterte tabeller, coordinate angir koordinat
function mergearrays(x, y, coordinate)
    mergedArray = [x; y]

    x = [x ; [Int64(9999999999999) Int64(9999999999999)]]
    y = [y ; [Int64(9999999999999) Int64(9999999999999)]]

    i = 1
    j = 1

    for k in 1:(size(x, 1) + size(y, 1) - 2)
        if x[i, coordinate] <= y[j, coordinate]
            mergedArray[k, :] = x[i, :]
            i = i + 1
        else
            mergedArray[k, :] = y[j, :]
            j = j + 1
        end
    end

    return mergedArray

end

# x er en usortert tabell, coordinate angir koordinat vi skal sortere langs
function mergesort(x, coordinate)   
    if size(x, 1) == 1
        return x
    end
    
    l1 = reshape([], 0, 2)
    l2 = reshape([], 0, 2)

    alternate = 0

    for k in 1:size(x, 1)
        if alternate == 0
            l1 = [l1; [x[k, 1] x[k, 2]]]
            if k == Int32(floor(size(x, 1) / 2))
                alternate = 1
            end
        else
            l2 = [l2; [x[k, 1] x[k, 2]]]
        end
    end

    println(l1)
    println(l2)


    l1 = mergesort(l1, coordinate)
    l2 = mergesort(l2, coordinate)

    return mergearrays(l1, l2, coordinate)
        
end

#println(mergesort([5.0 5.0; 6.0 6.0; -3.0 3.0; 10.0 1.0; -1.0 2.0; 70.0 1.0], 2))

function binaryintervalsearch(x, delta, coordinate)
    if size(x, 1) % 2 == 0
        median = (x[Int64(floor(size(x, 1) / 2)), coordinate] + x[Int64(floor(size(x, 1) / 2) + 1), coordinate]) / 2
    else
        median = x[Int64(floor(size(x, 1) / 2)) + 1, coordinate]
    end

    stIntervall = median - delta
    slIntervall = median + delta

    st = 0
    sl = 0

    for k in 1:size(x, 1)
        if x[k, coordinate] >= stIntervall
            st = k
            break
        end
    end

    for k in 1:size(x, 1)
        if x[k, coordinate] <= slIntervall
            sl = k
        end
    end

    sl - st < 0 && return (-1, -1)


    return (st, sl)

end

println(binaryintervalsearch([1.0 0.0; 2.0 0.0; 3.0 0.0; 4.0 0.0], 0.1, 2))

function bruteforce(x)
    shortestD = 999999999999999999999999
    for k in 1:size(x, 1)
        for i in k + 1:size(x, 1)
            if sqrt((x[k,1] - x[i,1])^2 + (x[k,2] - x[i,2])^2) < shortestD
                shortestD = sqrt((x[k,1] - x[i,1])^2 + (x[k,2] - x[i,2])^2)
            end
        end
        return shortestD
    end
end

#println(bruteforce([1 1; 10 0; 2 2; 5 5]))

function splitintwo(x, y)
	
end
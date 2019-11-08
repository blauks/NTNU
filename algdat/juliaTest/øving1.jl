function insertionsort(A)
    for x = 2: length(A)
        key = A[x]
        i = x - 1
        while i > 0 && A[i] > key
            A[i+1] = A[i]
            i = i -1
        end
        A[i+1] = key
    end
end

insertionsort([1,5,5,3,54,4,6,3])

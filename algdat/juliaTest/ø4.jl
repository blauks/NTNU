function countingsortletters(A, position)
    k = 0
    B = ["" for i in 1:length(A)]

    for i in 1:length(A)
        if k < chartodigit(A[i][position])
            k = chartodigit(A[i][position])
        end
    end

    C = [0 for i in 1:k + 1]

    for j in 1:length(A)
        C[chartodigit(A[j][position])] = C[chartodigit(A[j][position])] + 1 
    end

    for i in 2:k
        C[i] = C[i] + C[i - 1]
    end

    j = length(A)

    while j > 0
        B[C[chartodigit(A[j][position])]] = A[j]
        C[chartodigit(A[j][position])] = C[chartodigit(A[j][position])] - 1 
        j -= 1
    end

    return B

end



function chartodigit(character)
    #Dette er en hjelpefunksjon for å få omgjort en char til tall
    #Den konverterer 'a' til 1, 'b' til 2 osv.
    #Eksempel: chartodigit("hei"[2]) gir 5 siden 'e' er den femte bokstaven i alfabetet.

    return character - '`'
end

#println(countingsortletters(["aa", "bb", "cc"], 1))
#println(countingsortletters(["cc", "bb", "aa"], 2))
#println(countingsortletters(["ac", "bb", "ca"], 2))
#println(countingsortletters(["ccc", "cba", "ca", "ab", "abc"], 2))

function countingsortlength(A)

    k = 0
    B = ["" for i in 1:length(A)]

    for i in 1:length(A)
        if k < length(A[i])
            k = length(A[i])
        end
    end

    C = [0 for i in 1:k + 1]

    for j in 1:length(A)
        C[length(A[j]) + 1] = C[length(A[j]) + 1] + 1 
    end

    for i in 2:k + 1
        C[i] = C[i] + C[i - 1]
    end

    j = length(A)

    println(C)

    while j > 0
        B[C[length(A[j]) + 1]] = A[j]
        C[length(A[j]) + 1] = C[length(A[j]) + 1] - 1 
        j -= 1
    end

    return B

end

#println(countingsortlength(["bbbb", "aa", "aaaa", "ccc"]))

function flexradix(A, maxlength)
    

end


println(flexradix(["kobra", "aggie", "agg", "kort", "hyblen"], 6))
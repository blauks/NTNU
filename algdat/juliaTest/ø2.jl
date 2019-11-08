mutable struct Node
    next::Union{Node, Nothing} # next kan peke på et Node-objekt eller ha verdien nothing.
    value::Int
end

function createlinkedlist(length)
    # Creates the list starting from the last element
    # This is done so the last element we generate is the head
    child = nothing
    node = nothing

    for i in 1:length
        node = Node(child, rand(1:800))
        child = node
    end
    return node
end

function findindexinlist(linkedlist, index)
    next = linkedlist
    curValue = 0

    for i in 1:index
        curValue = next.value
        if next.next == nothing && i != index
            return -1
        end
        next = next.next
    end

    return curValue

end

tempNode = createlinkedlist(5)
println(tempNode)
println(findindexinlist(tempNode, 6))

function reverseandlimit(array, maxnumber)
    startA = Int16[]

    for i in 1:length(array)
        push!(startA, array[i]<maxnumber ? array[i] : maxnumber)
    end
    return reverse!(startA)
end

#println(reverseandlimit([40, -23, -10, -20, -14], 0))



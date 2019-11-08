mutable struct NodeDoublyLinked
    prev::Union{NodeDoublyLinked, Nothing} # Er enten forrige node eller nothing
    next::Union{NodeDoublyLinked, Nothing} # Er enten neste node eller nothing
    value::Int # Verdien til noden
end

function createLinkedListDoublyLinked(length)
    # Create the list from the last element in the chain
    # This is so the returned element will be the first in the chain
    current = nothing
    beforeCurrent = nothing

    for i in 1:length
        # only fill out the next field because prev will be filled out later
        current = NodeDoublyLinked(nothing, beforeCurrent, rand(-100:100))
        # link up the node before this node to this node
        if beforeCurrent != nothing
            beforeCurrent.prev = current
        end
        beforeCurrent = current
    end
    return current
end

function maxofdoublelinkedlist(linkedlist)
    maxNum = -999999999999999999999999999999999
    first = linkedlist
    next = linkedlist
    prev = linkedlist
    while true
        if next.value > maxNum
            maxNum = next.value
        end
        if next.next == nothing
            break
        end
        next = next.next
    end
    while true
        if prev.value > maxNum
            maxNum = prev.value
        end
        if prev.prev == nothing
            break
        end
        prev = prev.prev
    end
    
    return maxNum

end

doubleList = createLinkedListDoublyLinked(20)
println(doubleList)
println(maxofdoublelinkedlist(doubleList))

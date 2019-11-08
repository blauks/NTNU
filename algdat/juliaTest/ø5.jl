function dnasimilarity(s1, s2)
    return length(s1) > 1 ? Int32(s1[1] == s2[1]) + dnasimilarity(s1[2:end], s2[2:end]) : Int32(s1[1] == s2[1])
end

println(dnasimilarity("AAAA", "AAAA"))

mutable struct Node
    children::Dict{Char,Node}
    count::Int
end

function searchtree(root, dna)
    function searchtree(root, dna)
        currentNode = root
        for i in 1:length(dna)
            if(haskey(currentNode.children, dna[i]))
                currentNode = currentNode.children[dna[i]]
            else
                return 0
            end
        end
        return currentNode.count
    end 
end
    

root1 = Node(Dict('A' => Node(Dict{Char,Node}(), 1), 'G' => Node(Dict('A' => Node(Dict{Char,Node}(), 2)), 1)), 0)
root2 = Node(Dict('A' => Node(Dict{Char,Node}(), 1), 'G' => Node(Dict('A' => Node(Dict{Char,Node}(), 1), 'G' => Node(Dict{Char,Node}(), 1)), 1), 'T' => Node(Dict('G' => Node(Dict('T' => Node(Dict{Char,Node}(), 1)), 0), 'T' => Node(Dict('G' => Node(Dict{Char,Node}(), 1)), 0)), 0), 'C' => Node(Dict('C' => Node(Dict('A' => Node(Dict{Char,Node}(), 1)), 1)), 1)), 0)

s1 = "AG"
s2 = "GA"
s3 = "TGT"

#println(searchtree(root1, s1))
#println(searchtree(root1, s2))
#println(searchtree(root1, s3))
#println(searchtree(root2, s1))
#println(searchtree(root2, s2))
#println(searchtree(root2, s3))
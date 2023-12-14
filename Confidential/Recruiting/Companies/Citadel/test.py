def findMaximumPathSum(currentNode, previousNode, adj, A):
    nonlocal answer
    
    stack = [(currentNode, previousNode)]
    
    # Nodes to which currentNode
    # is connected to
    while stack:
        currentNode, previousNode = stack.pop(-1)
        
        v = adj[currentNode]
        maximumBranchSum1 = 0
        maximumBranchSum2 = 0
        
        for i in range(len(v)):

            # Checking whether the branch
            # is visited already
            if (v[i] == previousNode):
                continue

            findMaximumPathSum(v[i],
                            currentNode, adj,
                            A)
            stack.append((v[i], currentNode))

            # Storing the maximum of value of branch path
            # sums maximumBranchSum1 will store the maximum
            # value maximumBranchSum2 will store the 2nd
            # most maximum value
            if (A[v[i]] > maximumBranchSum1):
                maximumBranchSum2 = maximumBranchSum1
                maximumBranchSum1 = A[v[i]]

            else:
                maximumBranchSum2 = max(maximumBranchSum2, A[v[i]])

    answer = max(answer, A[currentNode] +
                maximumBranchSum1 + maximumBranchSum2)

    # Updating the value of current node with
    # maximum path sum including currentNode
    A[currentNode] += maximumBranchSum1
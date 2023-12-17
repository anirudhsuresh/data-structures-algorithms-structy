def all_tree_paths(root):
    if not root:
        return None
    
    stack = [[root, [root.val]]]  # Ensure that you're storing the value of the root, not the root object itself
    res = []

    while stack:
        node, path = stack.pop()

        # If the node is a leaf, add the path to the result
        if not node.left and not node.right:
            res.append(path)
        
        # If the node has a right child, add it and its value to the stack
        if node.right:
            stack.append([node.right, path + [node.right.val]])  # Append the value, not the node
        
        # If the node has a left child, add it and its value to the stack
        if node.left:
            stack.append([node.left, path + [node.left.val]])  # Append the value, not the node

    return res

# Iterative approach 
# Time complexity : O(N^2)
# Space complexity: O(N log N)
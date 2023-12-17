from collections import deque 
def leaf_list(root):
    if root is None:
        return []
    
    q=deque()
    q.append(root)

    leaf_list=[]  # to store results 

    while q:
        
        current = q.popleft()

        if not current.left and not current.right:
            leaf_list.append(current.val)
        
        if current.left is not None:
            q.append(current.left)  

        if current.right is not None:
            q.append(current.right) 
    
    return leaf_list
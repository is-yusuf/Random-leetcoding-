class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        if root == None : return "" 
        
        q = deque()
        q.append(root)
        while q :
            k = len(q)
            for i in range (k):
                node = q.popleft()
                if node:
                    ret.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    ret.append("N")
                    
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        nodes = data.split(",")
        if not nodes[0]:            
            return None
        q = deque()
        root = TreeNode(nodes[0])
        q.append(root)
        i = 1
        while i < len(nodes[1:]):
            if not q :
                return root
            curnode = q.popleft()
            if nodes[i] != "N":
                curnode.left = TreeNode(int(nodes[i]))
                q.append(curnode.left)
            i+=1
            if nodes[i] != "N":
                curnode.right = TreeNode(int(nodes[i]))
                q.append(curnode.right)
            i+=1
            
        return root

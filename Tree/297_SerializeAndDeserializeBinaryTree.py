"""
1. return rserialize(root, ''):

We pass '' as the initial accumulator for building the serialized string.

It's like starting with an empty string and adding node values as we traverse.

2. l in rdeserialize(l):

l is the list of node values obtained from data.split(',').

Each recursive call pops the first element (l[0]) because preorder traversal ensures the next root to process is always at the front.

3. l.pop(0):

Removes the first element once it's processed (whether it's a node value or 'None'), so the recursion always looks at the correct "current" node.

"""

class Codec:

  # Serialization: DFS, Preorder(root -> left subtree -> right subtree)
    def serialize(self, root):
        def rserialize(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(int(l[0]))
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

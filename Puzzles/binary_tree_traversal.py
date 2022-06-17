from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(inorder) == 0:
            return None

        if len(preorder) == 1:
            last_node = TreeNode(preorder[0])
            return last_node
        
        # ind is storing the index/location of the root node
        ind = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[ind])
        
        node.left = self.build_tree(preorder, inorder[:ind])
        node.right = self.build_tree(preorder, inorder[ind+1:])
        
        return node

preorder_list = [3, 9, 20, 15, 7]
inorder_list = [9, 3, 15, 20, 7]

obj = Solution()
binary_tree = obj.build_tree(preorder_list, inorder_list)
print(binary_tree)

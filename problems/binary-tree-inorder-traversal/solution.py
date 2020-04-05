# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dfsStack = []

        def dfs(root: TreeNode):
            if not root:
                return []
            result = []
            # set up dfsStack
            dfsStack.append(root)
            # start iter dfs
            while dfsStack:
                curNode = dfsStack[-1]
                if curNode.left:  # if left exists, append left
                    dfsStack.append(curNode.left)
                    curNode.left = None
                else:  # if left not exists, output and pop the mid node
                    result.append(curNode.val)
                    dfsStack.pop()
                    if curNode.right:  # if right exists, append the right
                        dfsStack.append(curNode.right)
            return result

        return dfs(root)
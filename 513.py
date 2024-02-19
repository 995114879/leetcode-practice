# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def t1(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.right: queue.append(node.right)
        if node.left: queue.append(node.left)
    return node.val
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        while queue:
            vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                vals.append(node.val)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            ans.append(vals)
        return ans[-1][-1]
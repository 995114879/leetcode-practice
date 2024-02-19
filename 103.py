# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        even = False
        while queue:
            vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                vals.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(vals[::-1] if even else vals)
            even = not even
        return ans
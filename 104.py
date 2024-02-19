from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 初始化二叉树
# 初始化节点
n0 = TreeNode(val=0)
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
n6 = TreeNode(val=6)
# 构建引用指向（即指针）
n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6

def level_order(root: TreeNode) -> List[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res
res = []
# print(level_order(n0))
def pre_order(root: TreeNode):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)
    return res

def in_order(root: TreeNode):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)
    return res

def post_order(root: TreeNode):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)
    return res

# print(pre_order(n0))
# print(in_order(n0))
# print(post_order(n0))
# Definition for a binary tree node.

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    l_depth = maxDepth(root.left)
    r_depth = maxDepth(root.right)
    return max(l_depth, r_depth) + 1  

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def f(node, cnt):
            if node is None:
                return
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)
            f(node.left, cnt)
            f(node.right, cnt)
        f(root, 0)
        return ans


print(Solution().maxDepth(n0))

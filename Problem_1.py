'''
199 Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Solution:
1. Level order traversal. At each level, compute the length of the queue. That determines the no. of nodes at that level. Add the last node at that level to the result.

Time: O(N), Space: O(N) (more accurately, space = O(diameter))

'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level_order(values):
    N = len(values)
    if N == 0:
        return None
    q = deque()
    tree = TreeNode(values[0])
    q.append(tree)
    i=0
    while i < N and q:
        node = q.popleft()
        left_index = 2*i+1
        right_index = left_index + 1
        if left_index < N and values[left_index] is not None:
            node.left = TreeNode(values[left_index])
            q.append(node.left)
        if right_index < N and values[right_index] is not None:
            node.right = TreeNode(values[right_index])
            q.append(node.right)
        i += 1
    return tree

def right_view(root):
    if not root:
        return []
    result = []
    q = deque()
    q.append(root)
    while q:
        K = len(q)
        for k in range(K):
            root = q.popleft()
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if k == K-1:
                result.append(root.val)
    return result

def run_right_view():
    tests = [([1,2,3,None,5,None,4],[1,3,4]),
             ([1,2,3,4,None,None,None,5],[1,3,4,5]),
             ([1,None,3], [1,3]),
             ([],[])]
    for test in tests:
        root, ans = test[0], test[1]
        print(f"\nroot = {root}")
        tree = build_tree_level_order(root)
        view = right_view(tree)
        print(f"Right view = {view}")
        print(f"Pass: {ans == view}")

run_right_view()
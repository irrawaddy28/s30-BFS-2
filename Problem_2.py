'''
993 Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.

Solution:
1. Use level order traversal. While enqueing nodes, enque both the node and its parent. At each level, check if both the target nodes (x,y) were encountered at that level.
yes,
    check if their parents are different
        yes: they are cousins.
        no: not cousins
no:
    if only one of the targets was encountered, then it is guaranteed that the other target is at a different level or not present at all. Hencc, they cannot be cousins.

    if none of the target nodes were encountered, then go to the next level lower.

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

def is_cousins(root, x, y):
    if not root:
        return False
    q = deque()
    q.append((root, None))
    while q:
        K = len(q)
        count = 0
        h = {x:None, y:None}
        for _ in range(K):
            (root, parent_val) = q.popleft()
            if root.left:
                q.append((root.left, root.val))
            if root.right:
                q.append((root.right,root.val))

            if root.val in h:
                h[root.val] = parent_val
                count += 1

            if h[x] and h[y]:
                if h[x] != h[y]:
                    return True
        if count > 0:
            return False
    return False

def run_is_cousins():
    tests = [([1,2,3,4],4,3,False),
             ([1,2,3,None,4,None,5],5,4,True),
             ([1,2,3,None,4],2,3,False),
            ]
    for test in tests:
        root, x, y, ans = test[0], test[1], test[2], test[3]
        print(f"\nroot = {root}")
        tree = build_tree_level_order(root)
        flag = is_cousins(tree,x,y)
        print(f"{x} and {y} are cousins? {flag}")
        print(f"Pass: {ans == flag}")

run_is_cousins()
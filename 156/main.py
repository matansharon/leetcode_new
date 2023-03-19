class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import random
def random_tree(node=None):
    if node is None:
        return None
    chance= random.random()
    print(chance)
    # if chance>0.3:
    #     node.left = TreeNode(random.randint(0, 100))
    #     random_tree(node.left)
    # if chance<0.7:
    #     node.right =TreeNode(random.randint(0, 100))
    #     random_tree(node.right)
    # return node
head=TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
random_tree()

    

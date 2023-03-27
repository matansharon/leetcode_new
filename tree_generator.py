import random
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def generate_random_tree(number_of_nodes):

    head=TreeNode(random.randint(0, 100))
    for i in range(number_of_nodes):
        son=TreeNode(random.randint(0, 100))
        insert_randomly(head,son)
    return head
def insert_randomly(father,node):
    chance=random.randint(0,1)
    if chance==0:
        if father.left is None:
            father.left=node
        else:
            insert_randomly(father.left,node)
    else:
        if father.right is None:
            father.right=node
        else:
            insert_randomly(father.right,node)
def print_tree(node):
    if node is not None:
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)
        
if __name__ == '__main__':
    head=generate_random_tree(10)
    print_tree(head)
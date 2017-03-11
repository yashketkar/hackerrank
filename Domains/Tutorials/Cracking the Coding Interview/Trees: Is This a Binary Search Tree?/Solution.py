""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

mylist = []

def minorder(root):
    if root == None:
        return
    else:
        minorder(root.left)
        mylist.append(root.data)
        minorder(root.right)
    return

def check_binary_search_tree_(root):
    minorder(root)
    if len(mylist) != len(set(mylist)):
        return False
    if sorted(mylist) == mylist:
        return True
    return False

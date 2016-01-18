class Tree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data=data
        self.left_child = left_child
        self.right_child = right_child

def init_tree():
    global root
    leaf = []
    for i in range(6):
        leaf.append( Tree(i+1) )

    left_subtree = Tree(9, Tree(7, leaf[0], leaf[1]), Tree(8, leaf[2], leaf[3]) )
    right_subtree = Tree(10, leaf[4], leaf[5])

    root = Tree(11, left_subtree, right_subtree)
    return root

def preorder_traverse(tree):
    if tree == None: return
    print tree.data,
    preorder_traverse(tree.left_child)
    preorder_traverse(tree.right_child)

def inorder_traverse(tree):
    if tree == None: return
    inorder_traverse(tree.left_child)
    print tree.data,
    inorder_traverse(tree.right_child)

def postorder_traverse(tree):
    if tree == None: return
    postorder_traverse(tree.left_child)
    postorder_traverse(tree.right_child)
    print tree.data,

def levelorder_traverse(tree):
    global levelq
    levelq.append(tree)
    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print visit_node.data,
        # child put
        if visit_node.left_child != None:
            levelq.append(visit_node.left_child)
        if visit_node.right_child != None:
            levelq.append(visit_node.right_child)

def Main():
    a = init_tree()
    preorder_traverse(a)
    print "\n"
    inorder_traverse(a)
    print "\n"
    postorder_traverse(a)
    print "\n"
    levelorder_traverse(a)
    print "\n"

levelq=[]
Main()
import random
import sys


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data) #Dodanie elementu do kolejki
        return data

    def pop(self):
        return self.queue.pop(0) #Zwrócenie i usunięcie pierwszego elementu z kolejki (o indeksie 0)

    def is_empty(self):
        return len(self.queue) == 0 #True jeżeli kolejka jest pusta, False jeżeli nie

# FILO
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data) #Dodanie elementu do stosu
        return data

    def pop(self):
        return self.stack.pop() #Zwrócenie i usunięcie ostatniego elementu z stosu (o indeksie -1)

    def is_empty(self):
        return len(self.stack) == 0 #True jeżeli stos jest pusty, False jeżeli nie


def traverse_preorder(top, visit):  #
    if top is None:
       return visit(top)
    traverse_preorder(top.left, visit)
    traverse_preorder(top.right, visit)

def traverse_inorder(top, visit):
    if top is None:
        return traverse_inorder(top.left, visit)
    visit(top)
    traverse_inorder(top.right, visit)

def traverse_postorder(top, visit):
    if top is None:
        return traverse_postorder(top.left, visit)
    traverse_postorder(top.right, visit)
    visit(top)

def traverse_stack(top, visit):
    if top is None:
        return
    stack = list()  # stos symulujemy przez listę Pythona
    stack.append(top)
    while stack:
        node = stack.pop()
        visit(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def breadth_first_search(tree):
    q = Queue()
    q.put(tree)
    while not q.is_empty():
        node = q.pop()
        print(node)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

def depth_first_search(tree):
    stack = Stack()
    stack.push(tree)
    while not stack.is_empty():
        node = stack.pop()
        print(node)
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)

def leaves(tree):
    if tree is None:
        return 0
    elif tree.left is None and tree.right is None:
        return 1
    else:
        return leaves(tree.right) + leaves(tree.left)

def nodes_counter(top):
    if top is None:
        return 0
    queue = Queue()
    lev, count = [0, 0, 0, 0], 0
    queue.put(top)
    while not queue.is_empty():
        current = queue.pop()
        if count == 0:
            lev[0] += 1
        elif int(str(current)) == 2 or int(str(current)) == 3:
            lev[1] += 1
        elif int(str(current)) >= 4 and int(str(current)) <= 7:
            lev[2] += 1
        else:
            lev[3] += 1
        count += 1
        if current.left:
            queue.put(current.left)
        if current.right:
            queue.put(current.right)

    for i in range(0, len(lev)):
        print(f"Poziom {i+1}, wierzchołki: {lev[i]}")

def the_shortest_path(root):
    # base case
    if root is None:
        return 0
    l = the_shortest_path(root.left)
    r = the_shortest_path(root.right)
    if root.left is None:
        return 1 + r
    if root.right is None:
        return 1 + l
    return min(l, r) + 1

def the_shortest_path_leaves(root, path, x = 1):
    if x == path and root.left is None and root.right is None:
        print("Liście na poziomie: ", root)
        sys.exit()
    if root is None:
        return 0
    l = the_shortest_path_leaves(root.left, path, x+1)
    r = the_shortest_path_leaves(root.right, path, x+1)
    if root.left is None:
        return 1 + r
    if root.right is None:
        return 1 + l
    return min(l, r) + 1

def btree_count_iteratively(top):
    if top is None:
        return 0
    counter = 0
    stack = list()
    stack.append(top)
    while stack:
        node = stack.pop()
        counter += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return counter

def btree_print_indented(top, level=0):   #funkcja rysująca drzewo
    if top is None:
        return
    btree_print_indented(top.right, level+1)
    print("{}* {}".format('   '*level, top))
    btree_print_indented(top.left, level+1)

# Wersja rekurencyjna wstawiania.
def btree_random_insert(top, node):   # zwraca nowy korzeń
    if top is None:
        return node
    if random.random() < 0.5:
        top.left = btree_random_insert(top.left, node)
    else:
        top.right = btree_random_insert(top.right, node)
    return top

# Wersja rekurencyjna wyszukiwania.
def btree_random_search(top, data):   # zwraca węzeł lub None
    if top is None or top.data == data:
        return top
    node = btree_random_search(top.left, data)
    if node:
        return node
    else:
        return btree_random_search(top.right, data)

# Wersja rekurencyjna wstawiania.
def bst_insert(top, node):   # zwraca nowy korzeń
    if top is None:
        return node
    if node.data < top.data:
        top.left = bst_insert(top.left, node)
    elif node.data > top.data:
        top.right = bst_insert(top.right, node)
    else:
        pass          # ignorujemy duplikaty
    return top            # bez zmian

# Wersja rekurencyjna wyszukiwania.
def bst_search(top, data):   # zwraca węzeł lub None
    if top is None or data == top.data:
        return top
    elif data < top.data:
        return bst_search(top.left, data)
    else:   # data > top.data
        return bst_search(top.right, data)

# Wersja iteracyjna wyszukiwania.
def bst_search_iteratively(top, data):   # zwraca węzeł lub None
    while top is not None:
        if data == top.data:
            return top
        elif data < top.data:
            top = top.left
        else:   # data > top.data
            top = top.right
    return None

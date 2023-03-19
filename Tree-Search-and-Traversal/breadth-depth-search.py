import functions
import copy

root = None
root = functions.Node(1)
root.left = functions.Node(2)
root.right = functions.Node(3)
root.left.left = functions.Node(4)
root.left.right = functions.Node(5)
root.right.left = functions.Node(6)
root.right.right = functions.Node(7)
root.left.left.left = functions.Node(8)
root.left.left.right = functions.Node(9)
root.left.right.left = functions.Node(10)
root.left.right.right = functions.Node(11)
root.right.left.left = functions.Node(12)
root.right.left.right = functions.Node(13)
root.right.right.left = functions.Node(14)
root.right.right.right = functions.Node(15)

functions.btree_print_indented(root)

copied_tree = copy.deepcopy(root)

print("Przeszukiwanie wszerz:")
functions.breadth_first_search(root)

print("Przeszukiwanie w głąb:")
functions.depth_first_search(copied_tree)

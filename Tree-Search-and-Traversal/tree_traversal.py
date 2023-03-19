import functions


root = None
root = functions.Node(1)
root.left = functions.Node(2)
root.right = functions.Node(3)
root.left.left = functions.Node(4)
root.left.right = functions.Node(5)
root.right.right = functions.Node(7)
root.left.left.left = functions.Node(8)
root.left.left.right = functions.Node(9)
root.left.right.left = functions.Node(10)
root.left.right.right = functions.Node(11)
root.right.right.left = functions.Node(14)
root.right.right.right = functions.Node(15)

functions.btree_print_indented(root)

print(f"\nLiczba liści powyższego drzewa: {functions.leaves(root)}")
functions.nodes_counter(root)
path = functions.the_shortest_path(root)
print("Najkrótsza ścieżka: ", path)
print(functions.the_shortest_path_leaves(root, path))

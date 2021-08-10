import path_finder.tree as tree

node1 = tree.Node(1, 1)
node2 = tree.Node(2, 2)
node3 = tree.Node(3, 3)
node4 = tree.Node(4, 4)
node5 = tree.Node(5, 0)
node6 = tree.Node(6, 6)
node7 = tree.Node(7, 7)
node8 = tree.Node(8, 8)
node9 = tree.Node(9, 9)
node10 = tree.Node(10, 0)

node1.addChilds([node2, node3])
node2.addChilds([node4, node6])
node3.addChilds([node5])
node5.addChilds([node7, node9])
node6.addChilds([node8, node10])

tree1 = tree.Tree(node1)

tree1.find(0, tree1.root)
found = sorted(tree1.found, key=lambda element: element[2])
print('Found: ', found)

tree1.tracePathToRoot(found[0][1])
print('Path:', tree1.path)
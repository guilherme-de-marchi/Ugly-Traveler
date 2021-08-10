class Tree:
    def __init__(self, root_node) -> None:
        self.root = root_node
        self.found = []
        self.path = []

    def find(self, target, target_node, counter=0):
        counter += 1
        
        if target_node.value == target:
            self.found.append([target_node.id, target_node, counter])
        
        for child in target_node.childs:
            self.find(target, child, counter)

    def tracePathToRoot(self, target_node):
        if target_node.parent != None:
            self.path.append(target_node.parent)
            self.tracePathToRoot(target_node.parent)

class Node:
    def __init__(self, id, value, parent=None) -> None:
        self.id = id
        self.parent = parent
        self.value = value
        self.childs = []

    def addChilds(self, childs_list) -> None:
        for child in childs_list:
            child.parent = self
            self.childs.append(child)
import tree

class Body:
    def __init__(self) -> None:
        self.x_tree = None
        self.y_tree = None
        
    def insert_body(self, position:tuple):
        self.x_tree = tree.insert(self.x_tree, position[0])
        self.y_tree = tree.insert(self.y_tree, position[1])

    def delete_body(self, position:tuple):
        self.x_tree = tree.deleteNode(self.x_tree, position[0])
        self.y_tree = tree.deleteNode(self.y_tree, position[1])

    def is_body(self, position:tuple):
        pass
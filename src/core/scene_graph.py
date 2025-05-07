class SceneNode:
    def __init__(self):
        self.transform = np.identity(3)
        self.children = []
        self.parent = None

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

class GarudaScene:
    def __init__(self, size=(1280, 720)):
        self.root_node = SceneNode()
        self.active_camera = None
        self.render_queue = []
    
    def traverse(self, node):
        yield node
        for child in node.children:
            yield from self.traverse(child)
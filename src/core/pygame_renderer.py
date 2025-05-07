class PygameRenderer:
    def __init__(self, scene, fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode(
            scene.size, 
            pygame.OPENGL | pygame.DOUBLEBUF
        )
        self.clock = pygame.time.Clock()
        self.scene = scene
    
    def render_frame(self):
        self.screen.fill((0,0,0))
        for node in self.scene.traverse():
            if hasattr(node, 'draw'):
                node.draw(self.screen)
        pygame.display.flip()
        return pygame.surfarray.array3d(self.screen)
class GarudaScene:
    def __init__(self, size=(1280, 720)):
        self.size = size
        self.renderer = PygameRenderer(self)  # Add this line
        self.timeline = []
        
    def render(self):
        """Main rendering entry point"""
        self.renderer.run_animation()
        return self.renderer  # Enables .export()
    
    def play(self, animation):
        self.timeline.append(animation)
        
    def wait(self, duration):
        self.timeline.append(('wait', duration))
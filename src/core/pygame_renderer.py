class PygameRenderer:
    def __init__(self, scene):
        self.scene = scene
        self.frames = []
        
    def run_animation(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.scene.size)
        clock = pygame.time.Clock()
        
        start_time = time.time()
        while self.scene.timeline:
            current_animation = self.scene.timeline.pop(0)
            
            if current_animation[0] == 'wait':
                time.sleep(current_animation[1])
            else:
                # Process animation transforms
                pass
            
            self.frames.append(self.render_frame())
            clock.tick(60)
            
        pygame.quit()
    
    def export(self, filename):
        import cv2
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, 60, self.scene.size)
        
        for frame in self.frames:
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        out.release()
import cv2
import numpy as np

class PyGameRecorder:
    def __init__(self, screen, fps=30):
        self.frames = []
        self.screen = screen
        
    def capture(self):
        frame = pygame.surfarray.array3d(self.screen).transpose(1,0,2)
        self.frames.append(frame)
        
    def export(self, filename):
        height, width = self.frames[0].shape[:2]
        writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
        for frame in self.frames:
            writer.write(frame)
        writer.release()
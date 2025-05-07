import pygame
import cv2
import numpy as np

class PyGameRecorder:
    def __init__(self, screen, fps=30):
        self.frames = []
        self.screen = screen
        self.fps = fps

    def capture(self):
        arr = pygame.surfarray.array3d(self.screen)
        arr = arr.transpose([1,0,2])
        self.frames.append(arr.copy())

    def export(self, filename):
        if not self.frames:
            print("No frames to export!")
            return
        height, width = self.frames[0].shape[:2]
        writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (width, height))
        for frame in self.frames:
            writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        writer.release()
        print(f"Exported video to {filename}")
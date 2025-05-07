import pygame
from exporter import PyGameRecorder

class GarudaScene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        self.clock = pygame.time.Clock()
        self.mobjects = []
        self.recorder = PyGameRecorder(self.screen)

    def add(self, mobject):
        self.mobjects.append(mobject)

    def play(self, animation, run_time=2):
        start_time = pygame.time.get_ticks()
        duration = run_time * 1000
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            now = pygame.time.get_ticks()
            alpha = min(1, (now - start_time) / duration)
            animation.update(alpha)
            self.render()
            self.recorder.capture()
            if alpha >= 1:
                finished = True
            self.clock.tick(30)

    def render(self):
        self.screen.fill((255,255,255))
        for mobj in self.mobjects:
            mobj.draw(self.screen)
        pygame.display.flip()
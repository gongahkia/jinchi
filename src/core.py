import pygame
from effects import Animation

class GarudaScene:
    def __init__(self):
        self.mobjects = []
        self.playbook = []
        self.screen = pygame.display.set_mode((1280, 720))
        self.recorder = PyGameRecorder(self.screen)

    def add(self, mobject):
        self.mobjects.append(mobject)

    def play(self, *animations, run_time=1):
        for anim in animations:
            anim.start(run_time)
            while not anim.is_finished():
                anim.update()
                self.render()
                self.recorder.capture()

    def render(self):
        self.screen.fill((255,255,255))
        for mobj in self.mobjects:
            mobj.draw(self.screen)
        pygame.display.flip()
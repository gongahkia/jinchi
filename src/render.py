import pygame.freetype
from pygments import lex
from pygments.lexers import get_lexer_by_name

class CodeObject:
    def __init__(self, text, language='python', style='monokai'):
        self.text = text
        self.tokens = list(lex(text, get_lexer_by_name(language)))
        self.font = pygame.freetype.SysFont('Consolas', 24)
        self._apply_style(style)

    def draw(self, screen):
        x, y = 50, 50
        for token, value in self.tokens:
            self.font.render_to(screen, (x, y), value, fgcolor=self.colors[token])
            x += self.font.get_rect(value).width
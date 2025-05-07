import pygame.freetype
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name

def get_token_colors(style_name):
    style = get_style_by_name(style_name)
    return {token: '#' + style.style_for_token(token)['color'] if style.style_for_token(token)['color'] else '#000000'
            for token in style.styles}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

class CodeObject:
    def __init__(self, text, language='python', style='monokai'):
        self.text = text
        self.visible_text = ""
        self.font = pygame.freetype.SysFont('Consolas', 24)
        self.tokens = list(lex(text, get_lexer_by_name(language)))
        self.colors = get_token_colors(style)
        self.language = language

    def draw(self, screen):
        x, y = 50, 50
        shown = self.visible_text if self.visible_text else self.text
        tokens = list(lex(shown, get_lexer_by_name(self.language)))
        for token, value in tokens:
            color = self.colors.get(token, '#000000')
            self.font.render_to(screen, (x, y), value, fgcolor=hex_to_rgb(color))
            x += self.font.get_rect(value).width
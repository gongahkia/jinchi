from core.scene_graph import GarudaScene
from core.animator import Animator
from core.text_processor.lexers import CodeLexer

class CodeExecutionVisualizer(GarudaScene):
    def construct(self):
        code = '''
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        '''
        
        # Create code block with syntax highlighting
        code_block = TextElement(code, lexer=CodeLexer())
        self.add(code_block.center())
        
        # Animation sequence
        self.play(HighlightLines(code_block, 0))  # def line
        self.wait(0.5)
        self.play(HighlightLines(code_block, 1))  # if condition
        self.play(IndentArrow(code_block, 2))     # return 1
        self.wait(1)

if __name__ == "__main__":
    scene = CodeExecutionVisualizer()
    scene.construct()  # Build animations
    scene.render().export("code_animation.mp4")  # Now works
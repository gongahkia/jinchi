from core.scene_graph import GarudaScene
from core.text_processor.lexers import LegalLexer

class LegalDocumentScene(GarudaScene):
    def construct(self):
        statute_text = """
        § 1.01. Definitions
        Art. 2 - For purposes of this Act:
        (a) "Person" means individual or corporation;
        (b) "Contract" refers to mutual agreement per Smith v. Jones (2020)
        """
        
        # Parse and style legal text
        doc = LegalTextElement(
            statute_text, 
            lexer=LegalLexer(),
            font_size=24
        )
        
        # Animate section by section
        self.play(SlideIn(doc.section(0), direction="left"))  # § 1.01
        self.play(Reveal(doc.subsections(1)))  # Art. 2
        self.play(
            Highlight(doc.find_token(Name.Entity))  # Smith v. Jones
            .set_color("#e74c3c")
        )
        self.wait(2)

if __name__ == "__main__":
    scene = LegalDocumentScene()
    scene.render().export("statute_animation.mp4")
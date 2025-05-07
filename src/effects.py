import time

class TypewriterEffect:
    def __init__(self, text_obj):
        self.obj = text_obj
        self.visible_chars = 0
        
    def update(self, alpha):
        self.visible_chars = int(alpha * len(self.obj.text))
        self.obj.visible_text = self.obj.text[:self.visible_chars]
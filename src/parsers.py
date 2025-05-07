class LegalParser:
    def parse(self, text):
        return [self._process_section(s) for s in text.split('\n\n')]
    
    def _process_section(self, text):
        return {'type': 'section', 'content': text}

class CodeParser:
    def parse(self, text):
        return {'type': 'code_block', 'content': text}
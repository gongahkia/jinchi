from pygments.lexer import RegexLexer
from pygments import token

class LegalLexer(RegexLexer):
    name = 'Legal'
    tokens = {
        'root': [
            (r'§\s*\d+\.\d+', token.Generic.Heading),
            (r'Art\.\s*\d+', token.Generic.Subheading),
            (r'[A-Z][a-z]+ v\. [A-Z][a-z]+', token.Name.Entity),
            (r'\bWhereas\b', token.Keyword.Declaration),
            (r'.', token.Text)
        ]
    }
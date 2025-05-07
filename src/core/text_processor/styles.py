from pygments.style import Style
from pygments.token import *

class GarudaStyle(Style):
    """Base color scheme for code/legal text"""
    
    default_style = "#ffffff"
    styles = {
        Generic.Heading:    "#2ecc71 bold",
        Generic.Subheading: "#3498db italic",
        Name.Entity:        "#e74c3c underline",
        Keyword.Declaration:"#9b59b6",
        Keyword:            "#e74c3c",
        Name.Function:      "#2980b9",
        String:             "#f1c40f",
        Comment:            "#95a5a6 italic",
    }

def load_colorscheme(filepath: str) -> Style:
    """Load custom color scheme from YAML/JSON"""
    import yaml
    with open(filepath) as f:
        colors = yaml.safe_load(f)
    return type('CustomStyle', (Style,), {'styles': colors})
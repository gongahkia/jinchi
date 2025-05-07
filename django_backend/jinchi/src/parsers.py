# ----- required imports -----

import re
from typing import List, Dict, Any, Optional

# ----- class definitions -----


class LegalParser:
    SECTION_PATTERN = re.compile(r"^(Section|§)\s*(\d+[A-Za-z\-]*)\.?", re.MULTILINE)
    SUBSECTION_PATTERN = re.compile(r"^\s*\(([a-zA-Z0-9]+)\)", re.MULTILINE)
    CITATION_PATTERN = re.compile(r"\b(\d+\s+U\.S\.C\.|[A-Z][a-z]+\s+Act)\b")

    def parse(self, text: str) -> List[Dict[str, Any]]:
        sections = []
        for sec_match in self.SECTION_PATTERN.finditer(text):
            sec_start = sec_match.start()
            sec_end = text.find("\nSection", sec_start + 1)
            if sec_end == -1:
                sec_end = len(text)
            section_text = text[sec_start:sec_end].strip()
            section = self._process_section(section_text)
            sections.append(section)
        if not sections:
            sections.append(self._process_section(text.strip()))
        return sections

    def _process_section(self, text: str) -> Dict[str, Any]:
        title_match = self.SECTION_PATTERN.search(text)
        title = title_match.group(0) if title_match else "Section"
        body = text[title_match.end() :].strip() if title_match else text
        subsections = []
        for sub_match in self.SUBSECTION_PATTERN.finditer(body):
            sub_start = sub_match.start()
            next_sub = body.find("\n(", sub_start + 1)
            if next_sub == -1:
                next_sub = len(body)
            sub_text = body[sub_start:next_sub].strip()
            subsections.append({"label": sub_match.group(1), "content": sub_text})
        citations = self.CITATION_PATTERN.findall(text)
        return {
            "type": "section",
            "title": title,
            "body": body,
            "subsections": subsections,
            "citations": citations,
        }


class CodeParser:
    FUNC_PATTERN = re.compile(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\):", re.DOTALL)
    CLASS_PATTERN = re.compile(
        r"class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*(\([^\)]*\))?:", re.DOTALL
    )
    DOCSTRING_PATTERN = re.compile(r'("""|\'\'\')(.+?)\1', re.DOTALL)

    def parse(self, text: str, language: Optional[str] = "python") -> Dict[str, Any]:
        if language == "python":
            return self._parse_python(text)
        else:
            return {"type": "code_block", "language": language, "content": text}

    def _parse_python(self, text: str) -> Dict[str, Any]:
        functions = []
        for match in self.FUNC_PATTERN.finditer(text):
            name = match.group(1)
            params = match.group(2)
            func_body = self._extract_block(text, match.end())
            docstring = self._extract_docstring(func_body)
            functions.append(
                {
                    "name": name,
                    "params": params,
                    "docstring": docstring,
                    "body": func_body,
                }
            )
        classes = []
        for match in self.CLASS_PATTERN.finditer(text):
            name = match.group(1)
            bases = match.group(2) if match.group(2) else ""
            class_body = self._extract_block(text, match.end())
            docstring = self._extract_docstring(class_body)
            classes.append(
                {
                    "name": name,
                    "bases": bases,
                    "docstring": docstring,
                    "body": class_body,
                }
            )
        module_docstring = self._extract_docstring(text)
        return {
            "type": "code_block",
            "language": "python",
            "module_docstring": module_docstring,
            "functions": functions,
            "classes": classes,
            "content": text,
        }

    def _extract_block(self, text: str, start: int) -> str:
        lines = text[start:].splitlines()
        block_lines = []
        for line in lines:
            if line.startswith(" ") or line.startswith("\t"):
                block_lines.append(line)
            else:
                break
        return "\n".join(block_lines)

    def _extract_docstring(self, text: str) -> Optional[str]:
        match = self.DOCSTRING_PATTERN.search(text)
        return match.group(2).strip() if match else None

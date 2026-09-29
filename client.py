"""DOM Readability & Boilerplate Remover.
100% Python Standard Library.
"""

import re

class ReadabilityBoilerplateRemover:
    """Strips boilerplate navigational elements and extracts substantive article text."""
    @staticmethod
    def extract_main_content(html_str):
        cleaned = re.sub(r'<(nav|footer|header|aside|script|style)\b[^>]*>.*?</\1>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
        paragraphs = re.findall(r'<p\b[^>]*>(.*?)</p>', cleaned, flags=re.DOTALL | re.IGNORECASE)
        substantive = []
        for p in paragraphs:
            plain = re.sub(r'<[^>]+>', '', p).strip()
            if len(plain) > 25:
                substantive.append(plain)
        return "\n\n".join(substantive)

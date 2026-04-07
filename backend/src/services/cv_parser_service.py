from io import BytesIO
from pypdf import PdfReader

SECTION_HEADERS = ["summary", "experience", "education", "certifications", "skills"]


class CvParserService:
    def extract_text(self, file_bytes: bytes) -> str:
        reader = PdfReader(BytesIO(file_bytes))
        return "\n".join(page.extract_text() or "" for page in reader.pages).strip()

    def normalize_sections(self, text: str) -> dict:
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        text_lower = text.lower()
        sections = {h: "" for h in SECTION_HEADERS}
        for h in SECTION_HEADERS:
            idx = text_lower.find(h)
            if idx != -1:
                snippet = text[idx: idx + 600]
                sections[h] = snippet

        if not sections["skills"]:
            skills_lines = [line for line in lines if "," in line and len(line) < 120][:3]
            sections["skills"] = "; ".join(skills_lines)
        return sections

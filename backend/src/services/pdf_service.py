from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PdfService:
    def build_document(self, title: str, body: str) -> bytes:
        buffer = BytesIO()
        doc = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        doc.setFont("Helvetica-Bold", 16)
        doc.drawString(50, height - 60, title)

        doc.setFont("Helvetica", 10)
        y = height - 90
        for line in body.splitlines():
            safe_line = line[:110]
            doc.drawString(50, y, safe_line)
            y -= 14
            if y < 60:
                doc.showPage()
                doc.setFont("Helvetica", 10)
                y = height - 60

        doc.save()
        buffer.seek(0)
        return buffer.read()

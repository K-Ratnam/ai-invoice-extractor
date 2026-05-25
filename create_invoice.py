from reportlab.pdfgen import canvas

def create_invoice():
    file_name = "sample_invoice.pdf"
    c = canvas.Canvas(file_name)

    c.setFont("Helvetica", 12)

    c.drawString(100, 800, "Invoice Number: INV-1001")
    c.drawString(100, 780, "Company: Amazon")
    c.drawString(100, 760, "Date: 2026-05-25")
    c.drawString(100, 740, "Total: 250.00 EUR")

    c.save()
    print("Invoice created successfully!")

create_invoice()
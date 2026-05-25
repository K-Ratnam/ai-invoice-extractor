import pdfplumber
import re

def extract_invoice_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""

        for page in pdf.pages:
            text += page.extract_text()

    invoice_number = re.search(r'Invoice\s*Number[:\s]*([A-Z0-9-]+)', text)
    amount = re.search(r'Total[:\s]*€?([\d.,]+)', text)
    date = re.search(r'Date[:\s]*([\d/-]+)', text)

    return {
        "invoice_number": invoice_number.group(1) if invoice_number else "Not Found",
        "amount": amount.group(1) if amount else "Not Found",
        "date": date.group(1) if date else "Not Found"
    }

if __name__ == "__main__":
    result = extract_invoice_data("sample_invoice.pdf")
    print(result)
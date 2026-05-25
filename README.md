# AI Invoice Extractor

An AI-inspired automation project built with Python that extracts invoice information from PDF files and converts unstructured data into structured Excel reports.

---

## Features

- Generate sample invoice PDFs
- Extract invoice data automatically
- Parse:
  - Invoice Number
  - Amount
  - Date
- Save extracted data into Excel
- Automated PDF processing workflow

---

## Technologies Used

- Python
- pdfplumber
- pandas
- openpyxl
- reportlab
- Regular Expressions (Regex)

---

## Project Structure

```bash
ai-invoice-extractor/
│
├── create_invoice.py
├── extract_pdf.py
├── sample_invoice.pdf
├── invoices.xlsx
├── README.md
└── .gitignore
```

---

## Installation

```bash
pip install pdfplumber pandas openpyxl reportlab
```

---

## Run Project

### Generate Sample Invoice

```bash
python create_invoice.py
```

### Extract Invoice Data

```bash
python extract_pdf.py
```

---

## Example Output

```python
{
 'invoice_number': 'INV-1001',
 'amount': '250.00',
 'date': '2026-05-25'
}
```

---

## Future Improvements

- AI-based invoice understanding
- Gmail invoice automation
- OCR support
- Streamlit dashboard
- Batch invoice processing

---

## Author

K-Ratnam
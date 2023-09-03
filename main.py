from fpdf import FPDF
from glob import glob
from pathlib import Path

filepaths = glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    pdf.add_page()
    name = Path(filepath).stem.title()
    pdf.set_font(family="Arial", size=20, style="B")
    pdf.cell(w=0, h=10, txt=name, ln=1)
    with open(filepath) as file:
        content = file.read()
    pdf.set_font(family="Arial", size=10)
    pdf.multi_cell(w =0, h=6, txt=content)

pdf.output(f"PDFs/output.pdf")

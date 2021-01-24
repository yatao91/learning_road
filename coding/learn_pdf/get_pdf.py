# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader, PdfFileWriter


def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)

    # Add hardware page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('document2.pdf', 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    path = 'Jupyter_Notebook_An_Introduction.pdf'
    rotate_pages(path)
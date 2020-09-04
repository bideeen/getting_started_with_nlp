# Collecting Data From PDF
import PyPDF2
from PyPDF2 import PdfFileReader

# Extracting Text from PDf
# creating a pdf file
pdf = open('data/file.pdf', 'rb')
# creating pdf reader
pdf_reader = PyPDF2.PdfFileReader(pdf)
# checking number of pages in a pdf file
print(pdf_reader.numPages)
# creating a page object
page = pdf_reader.getPage(0)
# finally extracting text from the page
print(page.extractText())
# closing the pdf file
pdf.close()
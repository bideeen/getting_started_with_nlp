# Import the library
from docx import Document
# Creating a word file object
doc = open('data/file.docx', 'rb')
# creating word reader object
document = docx.Document(doc)
# creat an empty string and call this document
docu = ""
for para in document.paragraghs:
    docu += para.text

# output
print(docu)
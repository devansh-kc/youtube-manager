import docx
import docx.document
document  = docx.document("resume.docx")
for paragraph in document.paragraphs:
    print(paragraph.text)
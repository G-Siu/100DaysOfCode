# Get all text in word document as strings
import docx


def get_text(file_name):
    doc = docx.Document(file_name)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return "\n".join(full_text)


print(get_text("demo.docx"))

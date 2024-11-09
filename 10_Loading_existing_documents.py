from docx import Document

# Load an existing document
existing_doc = Document("assets/sample.docx")

# Print all paragraphs
for para in existing_doc.paragraphs:
    print(para.text)

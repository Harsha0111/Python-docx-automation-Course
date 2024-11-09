from docx import Document

# Load an existing document
existing_doc = Document("assets/sample.docx")

# Modify the first paragraph
existing_doc.paragraphs[0].text = "Modified text."

# Save the modified document
existing_doc.save("output/11_Modifying_existing_documents.docx")

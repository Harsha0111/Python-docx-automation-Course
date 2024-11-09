from docx import Document

# Create a new Document
doc = Document()

# Add a footer with a simple page number indication
footer = doc.sections[0].footer
footer_paragraph = footer.add_paragraph("Page X")

# Save the document
doc.save("output/09_Inserting_page_numbers.docx")

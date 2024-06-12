import PyPDF2

# Open the PDF file in binary mode
pdf = open("pdf extractor.pdf", "rb")

# Initialize PdfReader
reader = PyPDF2.PdfReader(pdf)

# Get the specified page (page index starts from 0)
page = reader.pages[0]

# Extract text from the page
text = page.extract_text()

# Count words
word_count = len(text.split())

# Close the PDF file
pdf.close()
print(text)

print("Total words in the PDF:", word_count)

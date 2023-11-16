import PyPDF2

file1 = open("meetingminutes1.pdf", "rb")
pdf = PyPDF2.PdfReader(file1)

# print(len(pdf.pages))  # Number of pages in the file
# page = pdf.pages[0]  # Get the page at specified page number
# print(page.extract_text())  # Get text from the page number specified
# for page in range(len(pdf.pages)):
#     print(pdf.pages[page].extract_text())  # Prints text in the whole file
writer = PyPDF2.PdfWriter()
for pages in range(len(pdf.pages)):
    page = pdf.pages[pages]
    writer.add_page(page)
file2 = open("meetingminutes2.pdf", "rb")
pdf2 = PyPDF2.PdfReader(file2)
for pages in range(len(pdf2.pages)):
    page = pdf2.pages[pages]
    writer.add_page(page)

output_file = open("combined_minutes.pdf", "wb")
writer.write(output_file)

file1.close()
file2.close()
output_file.close()

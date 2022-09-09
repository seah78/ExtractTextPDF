import PyPDF2

pdf = open("testextract.pdf", "rb")

reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extract_text())
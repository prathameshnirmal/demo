import PyPDF2

template = PyPDF2.PdfFileReader(open("dummy2.pdf", "rb"))
page = template.getPage(0)
watermark = PyPDF2.PdfFileReader("wtr.pdf", "rb")
page.mergePage(watermark.getPage(0))

output = PyPDF2.PdfFileWriter()
output.addPage(page)

with open("mergepdf.pdf", "wb") as old_file:
    output.write(old_file)

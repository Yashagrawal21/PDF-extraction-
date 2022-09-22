import PyPDF2
a = PyPDF2.PdfFileReader('5_6124989600252297803.pdf')
print(a.documentInfo)
print(a.getNumPages())

str = ""
for i in range(1,11):
    str += a.getPage(i).extractText()

with open("text.txt", "w", encoding='utf8') as f:
    f.write(str)


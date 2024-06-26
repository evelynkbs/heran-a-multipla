class Document:
    def show(self):
        return "Showing document base"

class Printable:
    def print(self):
        return "Print document"

class Editable:
    def edit(self):
        return "Edit document"

class PdfDocument(Document, Printable, Editable):
    pass

pdf = PdfDocument()
print(pdf.show())  # Usa método de Document
print(pdf.print())  # Usa método de Printable
print(pdf.edit())  # Usa método de Editable

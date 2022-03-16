import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    return '\n'.join(fullText)

print(getText('/home/alin/Documents/Automate-The-Boring-Stuff-With-Python/14) Excel, Word and PDF FIles/demo.docx'))
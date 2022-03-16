import PyPDF2
import os
os.chdir('/home/alin/Documents/Automate-The-Boring-Stuff-With-Python/14) Excel, Word and PDF FIles')
pdfFile = open('meetingminutes1.pdf', 'rb')   ## Open as read binary
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages

from pdf2docx import Converter



arq = input('nome do arquivo ')


pdffile = arq+'.pdf'
docxfile = arq+'.docx'

converter = Converter(pdffile)
converter.convert(docxfile)
converter.close()

print('acabou')
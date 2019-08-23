import os
import PyPDF2

file = os.listdir()

for file in os.listdir():
    pg_ok = PyPDF2.PdfFileWriter()
    if '.pdf' in file:
        with open(file,'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            n_Pag = pdf.getNumPages()
            for i in range(n_Pag):
                pagina = pdf.getPage(i)
                txt = pagina.extractText()
                if txt != ' \n':
                    pg_ok.addPage(pagina)
                    print(i)
            ok = open(file[:-4]+'_novo'+'_.pdf','wb')
            pg_ok.write(ok)
            ok.close()
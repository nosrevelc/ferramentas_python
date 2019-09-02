import glob
import PyPDF2
import os

#Conta quantidade de pagina no PDF e coloca um prefixo com a quaqntidade de página no nome do ficheiro.(Cleverson)

for i in glob.glob('*.pdf'):
    file=open(i,"rb")
    paginas=PyPDF2.PdfFileReader(file)
    num = paginas.getNumPages()
    file.close()
    os.rename(i,'{}pag-{}'.format(num,i))
    print(i)
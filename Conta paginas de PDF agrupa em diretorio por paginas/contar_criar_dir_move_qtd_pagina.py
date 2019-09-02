import glob
import PyPDF2
import os, time



for i in glob.glob('*.pdf'):
    if '.pdf' in i:
        file=open(i,"rb")
        paginas=PyPDF2.PdfFileReader(file)
        num = paginas.getNumPages()
        pasta = str(num)+'paginas'
        diretorio = os.path.exists(pasta)
        if not diretorio:
            os.makedirs(pasta)
        file.close()
        os.rename(i,'.\\'+pasta+'\\'+i)
        print(i)
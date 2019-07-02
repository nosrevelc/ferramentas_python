####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

#Progrma para sobrepor PDF´s Util para por exemplo colocar carta institucional como fundo em cartas em branco.

# Programa para arquivos em PDF.

# importando as bibliotecas nescessárias
from PyPDF2 import PdfFileWriter, PdfFileReader

# Aqui solicitamos dados nescessários para execução do programa.
ficheiro_frente = input('Qual nome ficheiros para colocar o fundo? \nDigite sem a extenção :')

pg_fundo = input('Qual nnome do ficheiro de fundo? \nDigite sem a extenção :')

# Aqui definimos na variável 'pdf_fundo' o PDF que será a nossa marca d'água
pdf_fundo = PdfFileReader(pg_fundo+'.pdf') 
#Do PDF que solicitou para fundo vamos informar qual página será utilizada, neste caso á Página e a '(0)'
watermark_page = pdf_fundo.getPage(0) 

# Aqui definimos na variável 'pdf_frente' o PDF que receberá a marca d'água.
pdf_frente = PdfFileReader(ficheiro_frente+'.pdf')

pdf_writer = PdfFileWriter()

# Definindo um contador
cont = 0
#Penango a quantidade páginas que serão tratadas
total = pdf_frente.getNumPages()

# Adicionando os fundos em todas as páginas do ficheiro.
for page in range(pdf_frente.getNumPages()):
        page = pdf_frente.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
        cont +=1
        # Exibe a quantidade de páginas já processdas de um valor total. 
        print(str(cont)+'- página de um total de :'+str(total)) 
# Abrindo e escrevendo o ficheiro.
with open('com_fundo_frente_'+ficheiro_frente+'.pdf', 'wb') as pdf_pronto:
    pdf_writer.write(pdf_pronto)

####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

# Programa para arquivos em PDF.

# Pretende-se que:
# O programa cheque os ficheiros começados com determinado prefixo.
# Cheque os ficheiros para verificar se teen páginas pares.
    # Caso existea um ficheiro de páginas cuja contagem acuse ser impar o programa exibe uma Box com alerta e registra em ficheiro txt, como um tipo de log.
# Faça o merge dos tais ficheiros tranformando-os em apenas um, ficheiro.
# Logo a seguir ,serpare as paginas corespondentes a página da frente da página do verso.

# importando as bibliotecas nescessárias
import os
import PyPDF2
from tkinter import messagebox


#Aqui o sistema busca o prefixo que será informado em um conunto de ficheiros
# Vale resaltar que o program esta preparado para tratar somente ficheiros em PDF.



# Preparando algumas variáveis
file = os.listdir()
coletar_arquivos = PyPDF2.PdfFileMerger()
arquivos_erros = []
Erro = 0
msg_no_close ='''

###########################################

            NÃO FECHE O PROGRAMA

###########################################

''' 
# Aqui inicia ciclo de leitura da lista de ficheiros. 
for file in os.listdir():    
    if 'pdf' in file :
    # Abertura e coleta de dados do ficheiro de cada ficheiro.
        with open(file,'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            n_Pag = pdf.getNumPages() #Será utilizado par verificar se é par ou impar.
            coletar_arquivos.append(file) # Se for par
            print(file)
    
# Caso não haja erro o sistema aqui vamos criar o ficheiro PDF já mesclado. 
print(msg_no_close)
  


coletar_arquivos.write('merge.pdf')
#Fim    

 
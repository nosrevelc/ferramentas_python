import os
import PyPDF2

####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

'''
Faz a leiruta de uma lista de PDF e devolve um csv com nome do ficheiro e a quantidade páginas de cada PDF
'''

cabecalho = '''
      
#############################################################  
#                                                           #
#       RENOMEIA A TODOS OS FICHEIROS DE UM DIRETÓTIO       #
#                                                           #
#############################################################            
                                                                       
 '''                                                             
print(cabecalho)

csvText='FICHEIRO;QNT.PAG;\n'
    
for file in sorted(os.listdir()):    
    if ('pdf' in file) or ('PDF' in file):
        with open(file,'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            n_Pag = pdf.getNumPages()   
            csvText+='{};{}'.format(file,n_Pag)+'\n'
            print('{},{}'.format(file,n_Pag))        
    csv = open('contagem.csv','w', encoding='utf-8')
    csv.write(csvText)
    csv.close()
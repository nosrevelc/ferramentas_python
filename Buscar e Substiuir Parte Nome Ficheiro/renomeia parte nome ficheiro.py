import os
import PyPDF2

####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

'''
Precisa renomear todo um lote de ficheiros, este script pode ajudar!
'''

cabecalho = '''
      
#############################################################  
#                                                           #
#       RENOMEIA A TODOS OS FICHEIROS DE UM DIRETÓTIO       #
#                                                           #
#############################################################            
                                                                       
 '''                                                             
print(cabecalho)

print('\n --- ATENÇÃO A LETRAS MAIUSCULAS E MINUSCULAS --- \n')       
str_atual=input('O que deseja buscar e renomear?')
str_novo=input('Renomear para.., ou omitir para remover -> ')
    
for nome_arquivo in os.listdir():
    qtd_carcteres = len(nome_arquivo)
    novo_nome =  nome_arquivo.replace(str_atual,str_novo)  
    os.rename(nome_arquivo,novo_nome)


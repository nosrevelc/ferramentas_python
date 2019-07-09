import os
import PyPDF2

####################################
# Autor:    Cleverson Vieira       #
#    cleverson.vieira@gmail.com    #
####################################

'''
Algumas vezes precisas adicionar um prefixo a varios ficheiros de um  diretório, com este script será bem fácil!
'''

cabecalho = '''
      
#############################################################  
#                                                           #
#   ADICIONA PREFIXO A TODOS OS FICHEIROS DE UM DIRETÓTIO   #
#                                                           #
#############################################################            
                                                                       
 '''                                                             
print(cabecalho)

prefixo=input('Qual prefixo deseja adicionar?')# Recebendo o prefixo.

# Correndo a lista e adicionando o prefixo.
for nome_arquivo in os.listdir():
    novo_nome = prefixo +'-'+ nome_arquivo
    os.rename(nome_arquivo,novo_nome)
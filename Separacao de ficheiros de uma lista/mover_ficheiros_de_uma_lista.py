
import os
 
lista = open('.\\lista_para_separar.txt', 'r', encoding = 'utf-8')
mover_ficheiros = [filetomove[:-1] for filetomove in lista]
lista.close()

if not os.path.exists('.\\separado'):
        os.makedirs('.\\separado')


for arquivo in os.listdir():
	for cod in mover_ficheiros:
		if arquivo.startswith(cod):
			os.rename(arquivo,'.\\separado\\' + arquivo)
			print(arquivo)
			break
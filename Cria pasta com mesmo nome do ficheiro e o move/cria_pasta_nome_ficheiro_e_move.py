import os

 # Se preferir um estenção espeficia adicione apos o ponto Ex.: '.pdf' ou se preferir ficheiros que contenham algum conteudo espeficico na nomenclatura, retire o ponto e colque a parte do nome que desja.

ficheiro = 'REA'

for i in os.listdir():
    if ficheiro in i: 
        if not os.path.exists('.\\'+i[:-4]):
            os.makedirs('.\\'+i[:-4])					
            os.rename(i,'.\\'+i[:-4]+'\\'+i)

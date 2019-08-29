import os
cont = 1
for i in os.listdir():
    if 'py' not in i:
        os.rename(i,str(cont)+'-'+i)
        cont +=1
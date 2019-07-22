
Adicione o ficheiro no diretamente no diretório que desja fazer a alteração!

Este programa, faz uma triagem de ficheiros a partir de uma lista, onde ele irá buscar o conteudo de cada linha em "lista_para_separar.txt" localizando o nome do ficheiro que começar com tal parte do texto.
Exemplo

Lista de arquivos a serem triados:

20190722_1_contrato.pdf
20190722_2_contrato.pdf
20190722_3_contrato.pdf
20190723_1_contrato.pdf
20190723_2_contrato.pdf
20190723_3_contrato.pdf
20190725_1_contrato.pdf
20190725_2_contrato.pdf
20190725_3_contrato.pdf
20190726_1_contrato.pdf
20190726_2_contrato.pdf
201907256_3_contrato.pdf

Conteúdo do ficheiro "lista_para_separar.txt".


20190725
20190722

No caso acima o programa irá criar uma pasta com nome "separado" e irá mover os ficheiros que iniciarem com alguns dos itens listados no arquivo "lista_para_separar.txt", conforme o exemplo abaixo:


\separado
    20190722_1_contrato.pdf
    20190722_2_contrato.pdf
    20190722_3_contrato.pdf
    20190725_1_contrato.pdf
    20190725_2_contrato.pdf
    20190725_3_contrato.pdf

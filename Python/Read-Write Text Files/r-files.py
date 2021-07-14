#MODO MENOS INCORRETO DE FAZER TRATAMENTO DE FICHEIROS

#FICHEIROS NOUTRAS DIRETORIAS TEMOS DE DAR O PATH PARA O FICHEIRO
#open('C:\\Desktop\\...')
#'r'-> ler  'w'-> escrever  'a'-> append    'r+'-> ler e escrever
f = open('test.txt', 'r')

print("Nome de ficheiro aberto: " + f.name)
print("Ficheiro fechado? " + str(f.closed))

#AO ABRIR UM FICHEIRO DESTE MODO, DEPOIS ELE TEM SEMPRE DE SER FECHADO
#NO CASO DE SER LANCADA UMA EXCECAO, UM FICHEIRO PODE NAO SER FECHADO E GERAR UM PROBLEMA
f.close()
print("Ficheiro fechado? " + str(f.closed))


#----------------------------------------------------------------------------------------


#MODO MAIS CORRETO DE TRATAR DE FICHEIROS

#FICHEIRO FECHADO AUTOMATICAMENTE, MESMO EM CASO DE EXCECAO
with open('test.txt', 'r') as f:
    print("Nome de ficheiro aberto: " + f.name)
    print("Ficheiro fechado? " + str(f.closed))

#MESMO AQUI FORA, E POSSIVEL UTILIZAR A VARIAVEL, O FICHEIRO ESTA FECHADO NO ENTANTO
print("Ficheiro fechado? " + str(f.closed))



#IMPRIME TUDO DENTRO DO FICHEIRO
with open('test.txt', 'r') as f:
    print("\n1º Modo")
    f_contents = f.read()
    print(f_contents)


#GERA UM ARRAY COM AS LINHAS E IMPRIME O ARRAY
with open('test.txt', 'r') as f:
    print("\n2º Modo")
    f_contents = f.readlines()
    print(f_contents)


#LE A PRIMEIRA LINHA DO FICHEIRO E AVANCA O POINTER PARA A PROXIMA PRIMEIRA LINHA
with open('test.txt', 'r') as f:
    print("\n3º Modo")
    f_contents = f.readline()
    #NAO ADICIONAR \n NO FINAL
    print(f_contents, end='')
    f_contents = f.readline()
    #NAO ADICIONAR \n NO FINAL
    print(f_contents, end='')


#O MESMO QUE O ANTERIOR MAS LE TODAS AS LINHAS DO FICHEIRO UMA DE CADA VEZ
with open('test.txt', 'r') as f:
    print("\n4º Modo")
    
    for line in f:
        print(line, end='')


#LE OS PRIMEIROS 50 CARATERES
with open('test.txt', 'r') as f:
    print("\n\n5º Modo")
    f_contents = f.read(50)
    #NAO ADICIONAR \n NO FINAL
    print(f_contents, end='')


#LE O FICHEIRO INTEIRO AOS BOCADOS«
with open('test.txt', 'r') as f:
    print("\n\n6º Modo")
    
    size_to_read = 50
    f_contents = f.read(50)
    while len(f_contents) > 0:
        #NAO ADICIONAR \n NO FINAL
        print(f_contents, end='')
        f_contents = f.read(50)
    
    #SEEK COLOCA O POINTER NUM CARATER ESPECIFICO
    f.seek(0)
    print("\nVoltei ao inicio: " + f.readline())
    
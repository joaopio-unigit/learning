#COM O MODO APPEND 'a', O WRITE ACRESCENTA TEXTO AO FICHEIRO
with open('test.txt', 'a') as f:
    f.write('\nNova linha adicionada')

#COM O MODO ESCRITA 'W', SE O FICHEIRO NAO EXISTIR SERA CRIADO
#CASO EXISTA SERA REESCRITO POR CIMA DO CONTEUDO
with open('writing.txt', 'w') as f:
    f.write('1ª Escrita - A MAIOR\n')
    f.write('2ª Escrita\n')
    f.seek(0)
    f.write('3ª Escrita')


#COPIAR DE UM FICHEIRO DE TEXTO PARA OUTRO
with open('test.txt', 'r') as rf:
    with open('testCopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#COPIAR OS BYTES DE UM FICHEIRO PARA OUTRO
with open('photo.png', 'rb') as rf:
    with open('photoCopy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
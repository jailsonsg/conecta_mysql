import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='desafio_B'
)
meucursor = banco.cursor()
opcao = 0
while opcao != 3:
    opcao = int(input("1 - Consultar  2 - Inserir  3-Sair: "))
    if opcao == 1:
        pesquisa = 'select * from alunos;'
        meucursor.execute(pesquisa)
        # fetchall recebe tudo da pesquisa e retorna através de uma tupla
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)
    elif opcao == 2:
        nome1=input("Insira o nome: ")
        telefone1=input("Insira o telefone: ")
        sql = 'insert into alunos (nome,telefone) values (%s,%s)'
        data = (nome1,telefone1)
        meucursor.execute(sql,data)
        banco.commit()
    elif opcao == 3:
        print('Fechando banco')
        meucursor.close()
        banco.close()
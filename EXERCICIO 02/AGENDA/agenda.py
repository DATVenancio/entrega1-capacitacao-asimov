# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:46:22 2021

@author: Daniel
"""

import sqlite3,time

conectar = sqlite3.connect('dbagenda.db')

c=conectar.cursor()


def inserir(nome,telefone,email):
    data= time.strftime('%d/%m/%Y')
    c.execute('INSERT INTO cadastro VALUES (?, ?, ?, ?)',(nome,telefone,email,data))

    conectar.commit()
    
def pesquisar(busca):
    sql = "SELECT * FROM cadastro WHERE nome = ?"
    for row in c.execute(sql,(busca,)):
        print(row)

def criar_table():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone text, email text, data text)') 
    

def mostrar_table():
    sql = "SELECT * FROM cadastro "
    print("NOME   -  TELEFONE  -  EMAIL  -  DATA")
    for row in c.execute(sql):
        print(row)
        
        
def deletar(busca):
    sql = "DELETE FROM cadastro WHERE nome = ?"
    for row in c.execute(sql,(busca,)):
        print(row)
    
    
try: 
    criar_table()
except:
    print('ERRO AO CRIAR TABELA')
else:
    print('TABELA CRIADA COM SUCESSO')

fc=10000;

while fc != 0:
    fc = int(input("1: CADASTRAR \n2: PESQUISAR\n3: MOSTRAR TODOS CADASTROS \n4: DELETAR \n \n0: SAIR \nESCOLHA:  "))
    
    
    if fc==1:
         
        try: 
            print('CADASTRO DA AGENDA')
            time.sleep(2)
            
            nome=str(input('NOME:       '))
            telefone=str(input('TELEFONE:   '))
            email=str(input('E-MAIL:    '))
            
            inserir(nome,telefone,email)
        except:
            print('ERRO AO CADASTRAR')
        else:
            print('CADASTRO FEITO COM SUCESSO')
    
    elif fc==2:
        print('PESQUISANDO...')
        time.sleep(1)
        
        busca = str(input("DIGITE O NOME A SER PESQUISADO :  "))
        
        pesquisar(busca)
        
    elif fc==3:
        print('PESQUISANDO...')
        time.sleep(1)
        
        mostrar_table()
        
    elif fc==4:
        
        busca = str(input("DIGITE O NOME A SER DELETADO :  "))
        
        print('DELETANDO...')
        time.sleep(1)
        
        deletar(busca)
        
        print('DELETADO...')
        
    
    elif fc==4:
        

        
        print('SAINDO...')
    else:
        print('OPÇÃO INVÁLIDA')
    

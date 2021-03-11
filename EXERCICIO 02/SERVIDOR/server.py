# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:01:14 2021

@author: Daniel
"""
from socket import *
def main():
            

        
        #DADOS DA CONEXÃO COM O SERVIDOR
        
        meuHost='localhost' 
        minhaPort=30800 #porta que vai servir de conexão
        
        
        sockobj = socket(AF_INET,SOCK_STREAM) #você está usando um servidor TCP-IP
        
        sockobj.bind((meuHost,minhaPort))  #recebe as conexões
        
        sockobj.listen(5) #máximo de conexões
        
        
        
        #TESTANDO A CONEXÃO COM O SERVIDOR
        
        while True: #enquanto tiver aluem tentando conectar
            conexao,endereco = sockobj.accept() #aceita conexão
            
            print("o servidor está conectado por: ",endereco) #mostra quem está conectado
            print("A conexao ",endereco,"mandou a mensagem:")
            
            while True:#enquanto estiver mandando mensagem (cada conexão pode mandar mais de uma 'linha')
                data = conexao.recv(1024) #recebe a mensagem
                if not data: #se não tiver mensagem
                    break #sai
                print(data)
                conexao.send(b'OBRIGADO PELA MENSAGEM! ANALISAREMOS E RETORNAMOS O MAIS RAPIDO POSSIVEL!') #se tiver mensagem retorna a mensagem
            conexao.close() #fecha a conexão

main()

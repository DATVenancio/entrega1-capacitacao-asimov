# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:01:14 2021

@author: Daniel
"""

from socket import *




#DADOS DO CLIENTE PARA  CONEXÃO COM O SERVIDOR

serverHost='localhost' #quando deixa vazio fala que a conexão é local
serverPort=30800 #porta que vai servir de conexão


texto= str(input('DIGITE UMA MENSAGEM AO SERVIDOR:  '))

mensagem = [texto.encode()]

#cria socket e conecta no servidor
sockobj = socket(AF_INET,SOCK_STREAM) #você está usando um servidor TCP-IP

sockobj.connect((serverHost,serverPort))    #conecta no servidor que tenha endereço serverHost

print("MENSAGEM: ",texto)
print("RESPOSTA: ")

for linha in mensagem:
    sockobj.send(linha) #manda uma mensagem ao servidor
    data = sockobj.recv(1024) # recebe a mensagem de volta do servidor
    print(data)
sockobj.close()
    




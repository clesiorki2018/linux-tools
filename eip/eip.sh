#!/bin/bash
#
# eip.sh
#
# Este script mostra o IPv4 que está sendo visualizado pelos sites na internet
# utiliza a página https:check.torproject.org para buscar a informação
#
# @Autor Clesio Maxuel clesiorki2014@gmail.com
# @Copyright Clesio Maxuel
#
# Criado em Novembro de 2019
# Primeira versão

# Faz o dump da página em um arquivo temporário
curl https://check.torproject.org &> /tmp/.bufferip 

# Faz o parsing para separ o IP 
grep addr /tmp/.bufferip |awk -F'<' '{print $3}'|awk -F'>' '{print $2}'

# Limpeza...
rm /tmp/.bufferip


A privacidade online hoje está em cheque, seja você um repórter, um estudante,
um hacker ou um maldito criminoso(se você se enquadra nesse último por genti-
leza, faça uma declaração de doação de órgãos e vá a m***!!!). Enfim para obter
privacidade online pode-se fazer uso de VPN, rede Tor entre outras formas.
	Esses mecanismos prometem ocultar nosso IP enquanto navegamos. Mas afi-
nal qual é o IP que os sites enchergam quando navegamos? Existem sites que nos
auxiliam a descobrir a resposta como o www.myip.com ou o www.whatsmyip.com, e 
também podemos obter ao acessarmos nosso próprio modem/roteador, esteja ciente
 que ao utilizar o método do roteador o IP do roteador pode diferir do IP que 
os sites enchergam dependendo da sua operadora de telecomunicação.
	Há situações, portém, em que se faz necessário saber qual o nosso IP
externo via linha de comando, principalmente quando estamos realizando um pen-
tester ou implementando uma VPN. E nesse ponto vamos criar um pequeno script 
em bash que fará essa tarefa para nós.

Requisitos:
	* curl (Versão com suporte a https) Nativo na maioria das distribuições
	     linux
	* awk ou sed  nativos na maioria das distribuições linux
	* grep  também nativo
	* rm nativo
	* bash nativo

Limitações:
	Esse utilitário foi desenvolvido para ser utilizado com o  protocolo 
IPv4, porém em um futuro próximo também funcionará com o protocolo IPv6.


Primeiramente crie o arquivo eip.sh com seu editor preferido e adicione a linha
básica como primeira linha.

#!/bin/bash

em seguida  baixamos a página html do projeto tor (https://check.torproject.org)
que informa nosso IPv4 que está sendo visto pelo site, e salvamos em um 
arquivo temporário em /tmp/.bufferip. Isso pode ser feito com a linha abaixo.

curl https://check.torproject.org &> /tmp/.bufferip

o arquivo temporário se faz necessário para evitar poluir o terminal com mensa-
gens secundárias provenientes do comando curl

após fazer o dump da página utilizaremos um filtro com grep e awk para extrair
o IP. Essa linha faz isso para nós.

grep addr /tmp/.bufferip |awk -F'<' '{print $3}'|awk -F'>' '{print $2}'

após obter a informação removemos o arquivo temporário com a linha abaixo.

rm /tmp/.bufferip

com o script pronto salve o arquivo, e adicione a permição de execução com o co-
mando abaixo.

chmod a+x eip.sh

como root mova o arquivo eip.sh para o diretório /opt/

mv ./eip.sh /opt/

ainda como root crie um link simbólico do nosso script para o diretório 
/usr/bin/ para poder ser utilizado por qualquer usuário.

ln -s /opt/eip.sh /usr/bin/eip

para testar só executar o comando
eip

o código fonte completo pode ser encontrodo no meu github em 
https://github.com/clesiorki2018/linux-tools/eip/eip.sh



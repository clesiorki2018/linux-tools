#include <stdio.h>/* */
#include <unistd.h>/* unistd.h para open(), read(), */
#include <fcntl.h>/* fcntl.h para O_RDONLY e P_NONBLOCKs*/

#define NAME_LOG "key.log"

char *keymap[] = {
    "dummy", "<ESC>", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "-", "=", "<BACK>", "<TAB>", "q", "w", "e", "r", "t", "y", "u", "i",
    "o", "p", "`", "[", "\n", "<CTRL>", "a", "s", "d", "f", "g", "h", "j",
    "k", "l", "ç", "^", "'", "@", "]", "z", "x", "c", "v", "b", "n", "m",
    ",", ".", ";", "<SHIFT>", "*", "<ALT>", " ", "<CAPS>", "<F1>",
    "<F2>", "<F3>", "<F4>", "<F5>", "<F6>", "<F7>", "<F8>", "<F9>",
    "<F10>", "<NUM>", "<SCROLL>", "7", "8", "9", "-", "4", "5", "6",
    "+", "1", "2", "3", "0", ",", "dummy", "dummy", "\\", "<F11>",
    "<F12>", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy", "dummy",
    "\n", "<CTRL>", "/", NULL } ;


int fd, bytes, code, contador;
FILE *logFile;

int main(int argc, char *argv[]){
  logFile = fopen(NAME_LOG, "r");
  while(!feof(logFile)){
      fread(&bytes, 2, 1, logFile);
      printf("%c\n", keymap[bytes]);
  }
  fclose(logFile);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <signal.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    pid_t p = atoi(argv[1]);
    int ret = kill(p, SIGTERM);
    printf("%d\n", ret);
}

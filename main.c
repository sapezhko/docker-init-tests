#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <signal.h>
#include <unistd.h>

#define SIGTERM_MSG "SIGTERM received.\n"
#define SLEEP_TIME 3600

void sig_term_handler(int signum, siginfo_t *info, void *ptr)
{
    write(STDERR_FILENO, SIGTERM_MSG, sizeof(SIGTERM_MSG));
    while (1)
        ;
}

void catch_signals()
{
    static struct sigaction _sigtermact;

    memset(&_sigtermact, 0, sizeof(_sigtermact));

    _sigtermact.sa_sigaction = sig_term_handler;
    _sigtermact.sa_flags = SA_SIGINFO;

    sigaction(SIGTERM, &_sigtermact, NULL);
}

int main()
{
    catch_signals();
    while (1)
        ;
}

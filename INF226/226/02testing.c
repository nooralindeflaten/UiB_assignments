#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main(int argc, char **argv){
    char buffer[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

    printf("%lx\n", buffer);
    fflush(stdout);
}
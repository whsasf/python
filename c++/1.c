#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 10;
    printf("dec = %d; octal = %o; hex = %x\n", x, x, x);
    printf("dec = %d; octal = %#o; hex = %#x\n", x, x, x);
    printf("the lenhth of int is :%lu\n",sizeof(int));
    return 0;
}

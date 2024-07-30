#include <stdio.h>
int main() 
{
    int a,b;
    int *ptr,*pt;
    scanf("%d %d",&a,&b);
    ptr=&a;
    pt=&b;
    printf("%d",*ptr+*pt);
}

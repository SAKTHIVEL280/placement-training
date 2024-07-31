#include <stdio.h>
int main()
{
    int a,t=1;
    scanf("%d",&a);
    for (int i=1;i<=a;i++)
    {
        t*=i;
    }
    printf("FActorial of %d is %d",a,t);
}

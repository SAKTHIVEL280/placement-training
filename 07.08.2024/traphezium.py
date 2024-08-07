#include<stdio.h>
int main() 
{
   int n;
    scanf("%d",&n);
    int L=1,r=n*n+1;
    for(int i=n;i>0;i--)
    {
        for(int j=n;j>i;j--)
            printf("  ");
        for(int k=i;k>0;k--)
            printf("%d*",L++);
        for(int k=i;k>1;k--)
            printf("%d*",r++);
        printf("%d",r);
        r=r-2*(i-1);
        printf("\n");
    }
}

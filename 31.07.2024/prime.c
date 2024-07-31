#include<stdio.h>
int main()
{
    int a,f;
    printf("Enter the number : ");
    scanf("%d",&a);
    if(a==2)
    {
        printf("Its prime :)");
    }
    for(int i=2;i<=a/2;i++)
    {
        if (a % i ==0)
        {
            f=0;
            printf("Its not prime :(");
            break;
        }
        else{
            f=1;
        }
    }
    if(f==1)
    {
        printf("Its a prime :)");
    }
}

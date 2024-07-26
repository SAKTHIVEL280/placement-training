#include<stdio.h>
int main()
{
    int r;
    printf("Enter the range : ");
    scanf("%d",&r);
    int a[r],ind[2];
    for(int i=0;i<r;i++)
    {
        printf("Enter the %d element : ",i+1);
        scanf("%d",&a[i]);
    }
    int t;
    printf("Enter the target : ");
    scanf("%d",&t);
    for(int i=0;i<r;i++)
    {
        for(int j=i+1;j<r;j++)
        {
            if(a[i]+a[j]==t)
            {
                printf("%d\n",i+j);
                ind[0,1]=i,j;
            }
        }
    }
    for(int i=0;i<2;i++)
    {
        printf("%d ",ind[i]);
    }
}

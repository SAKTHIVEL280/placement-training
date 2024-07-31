#include <stdio.h>
int main()
{
    int r,max=0;
    scanf("%d",&r);
    int arr[r];
    for(int i=0;i<r;i++)
    {
        printf("Enter number %d : ",i+1);
        scanf("%d",&arr[i]);
    }
    int min=arr[0];
    for (int i=0;i<r;i++)
    {
        if(max<arr[i])
        {
            max=arr[i];
        }
        if(min>arr[i])
        {
            min=arr[i];
        }
    }
    printf("Maximum : %d\nMinimum : %d",max,min);
}

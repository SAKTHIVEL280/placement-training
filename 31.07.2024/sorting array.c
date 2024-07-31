#include <stdio.h>
int main() 
{
    int r,temp;
    printf("Enter how many elements u r going to entry : ");
    scanf("%d",&r);
    int arr[r];
    for (int i=0;i<r;i++)
    {
        printf("Enter the element %d : ",i+1);
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<r;j++)
        {
            if (arr[i]>arr[j]) //change the sign to change the sorting
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    for(int i=0;i<r;i++)
    {
        printf("%d ",arr[i]);
    }
}

#include <stdio.h>
struct st
{
    int r;
    char n[100];
    float m;
};
int main() 
{
    struct st a[3];
    for(int i=0;i<3;i++){
    printf("Enter the roll number :");
    scanf("%d",&a[i].r);
    printf("Enter the name :");
    scanf("%s",a[i].n);
    printf("Enter the mark :");
    scanf("%f",&a[i].m);
    }
    for(int i=0;i<3;i++){
    printf("roll :%d\n",a[i].r);
    printf("name :%s\n",a[i].n);
    printf("mark :%f\n",a[i].m);
    }
}

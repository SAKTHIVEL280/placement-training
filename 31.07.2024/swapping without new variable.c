#include <stdio.h>
int main()
{
    int x,y;
    printf("Enter two number : ");    
    scanf("%d %d",&x,&y);
    printf("x=%d y=%d\n",x,y);
    x = x + y;
    y = x - y;
    x = x - y;
    printf("x=%d y=%d",x,y);
}

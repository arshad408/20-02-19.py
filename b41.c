#include<stdio.h>
#include<conio.h>
void main()
{
int n,i;
char a;
clrscr();
printf("Enter the number:");
scanf("%d",&n);
printf("Enter the string:");
scanf("%s",a);
for(i=0;i<=n;i++)
{
printf("\n%s\n",a);
}
  getch();
}


import java.util.Scanner;
class fac{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the numebr : ");
        int a=sc.nextInt();
        double f=1;
        for (int i=1;i<=a;i++)
        {
            f*=i;
        }
        System.out.print("The Factorial of "+a+" is "+f);
    } 
}


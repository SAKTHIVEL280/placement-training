import java.util.Scanner;
class e {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter how many elements u r going to enter : ");
        int a=sc.nextInt();
        int l[]= new int[a];
        for(int i=0;i<a;i++)
        {
            System.out.print("Enter number - "+(i+1)+":");
            l[i]=sc.nextInt();
        }
        int max=0;
        for(int i=0;i<a;i++)
        {
            if(max<l[i])
            {
                max=l[i];
            }
        }
        System.out.println("Maximum : "+max);
    }
}

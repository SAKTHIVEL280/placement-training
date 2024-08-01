import java.util.Scanner;
class c {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the range : ");
        int a=sc.nextInt();
        System.out.println("All even upto the range :)");
        for (int i=1;i<=a;i++)
        {
            if(i%2==0){
            System.out.println(i);
            }
        }
    }
}

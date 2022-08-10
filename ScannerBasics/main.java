public static void main(String[] args) {
        int x, y, n;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter value for x: ");
        x = scanner.nextInt();

        System.out.print("Enter value for y: ");
        y = scanner.nextInt();

        System.out.print("Enter value for n: ");
        n = scanner.nextInt();

        System.out.println("x^y mod n = "+exponentiation(x,y,n));
}



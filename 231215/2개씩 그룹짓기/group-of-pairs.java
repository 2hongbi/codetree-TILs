import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }

        System.out.println(maxMinGroupSum(n, numbers));

    }

    private static int maxMinGroupSum(int n, int[] numbers) {
        Arrays.sort(numbers);
        int maxSum = 0;
        for (int i = 0; i < n; i++) {
            maxSum = Math.max(maxSum, numbers[i] + numbers[numbers.length - 1 - i]);
        }
        return maxSum;
    }
}
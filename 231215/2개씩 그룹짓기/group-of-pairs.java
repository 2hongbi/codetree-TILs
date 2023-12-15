import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static final int MAX_N = 1000;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] numbers = new int[2 * MAX_N];

        for (int i = 0; i < 2 * n; i++) {
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers, 0, 2 * n);

        int groupMax = 0;
        for (int i = 0; i < n; i++) {
            // i 번째와 2n - 1 - i 번째 원소를 매칭하기
            int groupSum = numbers[i] + numbers[2 * n - 1 - i];
            if (groupSum > groupMax) {
                groupMax = groupSum;
            }
        }

        System.out.println(groupMax);

    }
}
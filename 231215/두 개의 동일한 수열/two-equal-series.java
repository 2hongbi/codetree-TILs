import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums1 = new int[n];
        int[] nums2 = new int[n];

        for (int i = 0; i < n; i++) {
            nums1[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            nums2[i] = sc.nextInt();
        }

        Arrays.sort(nums1);
        Arrays.sort(nums2);

        if (Arrays.equals(nums1, nums2)) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }

    }
}
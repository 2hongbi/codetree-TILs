import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        String startString = sc.next();

        ArrayList<String> words = new ArrayList<>();

        // n개의 단어를 입력받아서, 시작 문자열 T로 시작하는 단어만 리스트에 추가하기
        for (int i = 0; i < n; i++) {
            String word = sc.next();
            if (word.startsWith(startString)) {
                words.add(word);
            }
        }

        // 리스트를 사전순으로 정렬
        Collections.sort(words);

        // k번째 단어 출력
        if (k <= words.size()) {
            System.out.println(words.get(k - 1));
        } else {
            System.out.println("해당하는 단어가 없습니다.");
        }
    }
}
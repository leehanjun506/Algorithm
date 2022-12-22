import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    사용한 자료구조: 배열
    사용한 알고리즘: 반복문
 */

public class Main {

    private static int n, b, c, a[];
    // 전체 감독관의 수는 정수 범위를 초과할 수 있기 때문에 long 으로 선언합니다.
    private static long result;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 1. 입력
        n = Integer.parseInt(br.readLine());
        a = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        // 2. 계산
        for(int i=1; i<=n; i++){
            // 1) 총 감독관의 수
            // 총 감독관은 한반에 한명씩 꼭 들어갑니다.
            a[i] = a[i] - b;
            result++;

            // 2) 부 감독관의 수
            // 남은 응시생이 있어야 부 감독관이 들어갑니다.
            if(a[i] > 0) {
                // 나눗셈을 통해 부 감독관의 수를 계산합니다.
                result += a[i] / c;

                // 나머지가 있으면 부 감독관을 한명더 늘려줍니다.
                if(a[i] % c > 0) result++;
            }
        }

        System.out.println(result);
    }
}
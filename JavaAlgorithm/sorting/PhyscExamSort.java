package sorting;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class PhyscExamSort {

    static class PhyscExamData {

        String name;
        int height;
        double vision;

        PhyscExamData(String name, int height, double vision) {
            this.name = name;
            this.height = height;
            this.vision = vision;
        }

        public String toString() {
            return name + " " + height + " " + vision;
        }

        static final Comparator<PhyscExamData> HEIGHT_ORDER = new HeightOrderComparator();

        private static class HeightOrderComparator implements Comparator<PhyscExamData> {
            @Override
            public int compare(PhyscExamData o1, PhyscExamData o2) {
                return (o1.height > o2.height) ? 1 :
                        (o1.height < o2.height) ? -1 : 0; // 키를 기준으로 오름차순 정렬
            }

        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        PhyscExamData[] x = {
                new PhyscExamData("A", 12, 0.4),
                new PhyscExamData("B", 94, 0.4),
                new PhyscExamData("C", 9, 0.5)
        };

        Arrays.sort(x, PhyscExamData.HEIGHT_ORDER);
        for (PhyscExamData physcExamData : x) {
            System.out.println(physcExamData);
        }
    }

}

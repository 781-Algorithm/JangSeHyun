public class test {

    public static void main(String[] args){
        String a = "aaa";
        String b = "aaa";
        String c = new String("aaa");
        String d = new String("aaa");
        System.out.println(a==b);
        System.out.println(a==c);
        System.out.println(c==d);
    }
}

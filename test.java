



public class test {
    public static void main(String[] args) {
        TestCursor new_test = new TestCursor("Loh",1,true);
        System.out.println(new_test.getName("Pidor"));
        secondCursor new_class = new secondCursor("Loh_runner",10,true,2);
        System.out.println(new_class.getName());
        
    }
    
}













class TestCursor{
    String name;
    int haha;
    boolean False;


    public TestCursor(String name, int haha, boolean True){
        this.False = True;
        this.name = name;
        this.haha = haha;
    }


    public String getName(){
        return this.name;
    }

    public String getName(String a){
        return this.name+" "+a;}
}

public class test {
    public static void main(String[] args) {
        TestCursor new_test = new TestCursor("Loh",1,true);
        System.out.println(new_test.getName("Pidor"));
        secondCursor new_class = new secondCursor("Loh_runner",10,true,2);
        System.out.println(new_class.getName());
        
    }
    
}



class secondCursor extends TestCursor{
    int position;

    public secondCursor(String name,int haha,boolean False,int position){
        super(name, haha, False);
        this.position = position;
    }

    public int getPostion(){
        return this.position;
    }

    @Override
    public String getName(){
        return this.name + " "+ "second Class";
    }
}



abstract class Cursor {
    int position;

    public Cursor(int position){
        this.position = position;
    }

    public int getPosition(){
        return this.position;
    }
}




public interface Inner_test {
    public void test();

    public void akunamatata();
}


public class Inner_test_impl implements Inner_test {
    public void test(){
        System.out.println("Test");
    }

    public void akunamatata(){
        System.out.println("Akunamatata");
    }
}
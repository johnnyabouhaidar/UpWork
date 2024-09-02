class HelloWorld{
    public static void main(String[] args){
        try{
        int sentence = 1;
        sentence = "test";
        }catch(Exception ex){
        System.out.println("ow");    
        }finally{
            System.out.println("ow1");    
        }

    }
}
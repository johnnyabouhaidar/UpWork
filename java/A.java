public class A{
    public static void main(String[]args){
        int[] inputArr={1,6,3,4,8,2,5,2,3,6,4,7};
        for (int i=0; i< inputArr.length;i++){
            for(int j=0;j<inputArr.length-i-1;j++){
                if (inputArr[j]>inputArr[j+1]){
                    int tmp = inputArr[j];
                    inputArr[j]=inputArr[j+1];
                    inputArr[j+1]=tmp;
                }
            }
        }
    
    for (int k=0;k<inputArr.length;k++)
    {
        System.out.println(inputArr[k]);
    }
    }
}
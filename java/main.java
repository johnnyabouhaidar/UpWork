class HelloWorld{
    public static void main(String[] args){
        int num_arr[]={4,2,3,5,6};
        
        for (int i=0;i<num_arr.length;i++){
            for (int j=0;j<num_arr.length-i-1;j++){
                if (num_arr[j]>num_arr[j+1]){
                    num_arr[j]=num_arr[j+1];
                    num_arr[j+1]=num_arr[j];
                }
            }
        }
        for (int k=0;k<num_arr.length;k++){
            System.out.println(num_arr[k]);
        }
    }
}
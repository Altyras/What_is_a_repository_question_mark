public class JavaTempMem {
    public static void main(String[] args) {
        int[][] stuff = new int[3][5];
        for (int i = 0; i < stuff.length; i++) {
            for (int j = 0; j < stuff[i].length; j++) {
                stuff[i][j]=i*j;
                System.out.print(stuff[i][j] + " ");
            }System.out.println();
}   }   }

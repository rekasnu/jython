/**
* Author : Ermins Dreimanis
* St. No. SB12408
*/

public class View{
    public View(){}
    
    // print matrix

    public void printMatrix(int [][] matrix){
	int rows = matrix.length;
    int columns = matrix[0].length;
	for ( int c = 0 ; c < rows ; c++ )
	{
	   for ( int d = 0 ; d < columns ; d++ ){
		 System.out.print(matrix[c][d]+"\t");
	   }
	   System.out.print("\n");
	}
    }
}
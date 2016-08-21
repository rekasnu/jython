/**
* Author : Ermins Dreimanis
* St. No. SB12408
*/

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.Random;
import java.util.Vector;
import java.util.Arrays;


public class Model{

	public Model(){}
		int [][] matrix;
		int[][] transpose;



	// get and validate user input
	public int getInput(String question){
		int inp = 0;
		boolean repeat = true;
		do{
			Scanner in = new Scanner(System.in);
			System.out.print(question);
			try{
				inp = in.nextInt();
				repeat = false;

			}catch(Exception e){
				System.out.println("Not a valid input! Integer - please!");
				repeat = true;
			}
		}while(repeat);
		return inp;
    }
    //generate heat matrix
    public void generateHeatMatrixes( int rows_columns, int step){
		matrix = new int[rows_columns][rows_columns];
		File file = new File("HeatdataJava.txt");
			try{

				FileWriter fw = new FileWriter(file.getAbsoluteFile());
				BufferedWriter bw = new BufferedWriter(fw);
				for (int c = 0 ; c < rows_columns+1 ; c=c+step ){
					for (int d = 0 ; d < rows_columns+1 ; d=d+step ){
						if(d == 0)
						   bw.write(""+d);
						if(d>0)
							bw.write(" "+d);
					}
					bw.newLine();
				}
				bw.close();

			} catch (IOException e) {
					e.printStackTrace();
			}
		File file1 = new File("TransposeHeatdataJava.txt");
			try{

				FileWriter fw = new FileWriter(file1.getAbsoluteFile());
				BufferedWriter bw = new BufferedWriter(fw);
				for (int c = 0 ; c < rows_columns+1 ; c=c+step ){
					for (int d = 0 ; d < rows_columns+1 ; d=d+step ){
						if(d == 0)
						   bw.write(""+c);
						if(d>0)
							bw.write(" "+c);
					}
					bw.newLine();
				}
				bw.close();

			} catch (IOException e) {
					e.printStackTrace();
			}
	}

	// generate matrix

	public int[][] generateMatrix( int rows_columns){
		Random randNum = new Random();
		matrix = new int[rows_columns][rows_columns];

		for (int c = 0 ; c < rows_columns ; c++ ){
			for (int d = 0 ; d < rows_columns ; d++ ){
				matrix[c][d] = randNum.nextInt(100);
			}
		}
		return matrix;

	}

	// transpose matrix

	public int[][] transposeMatrix(int [][]matrix1){
		int rows = matrix1.length;
        int columns = rows;

    //    System.out.println(rows+" ------------ "+columns);
		//transpose = new int[columns][rows];

		for (int c = 0 ; c < rows ; c++ )
		{
			for (int d = c+1 ; d < columns ; d++ ) {

				int temp = matrix[c][d];
				matrix1[c][d] = matrix[d][c];
				matrix[d][c] = temp;
			}

		}
		return matrix1;
}
}
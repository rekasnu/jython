 
import os
from subprocess import Popen,PIPE 


class Plot(object):
    def plotGraph(self, data):
        gnuplot = r'C:\Program Files (x86)\gnuplot\bin\gnuplot'
        plot=Popen([gnuplot,'-persist'],stdin=PIPE,stdout=PIPE,stderr=PIPE)
        plot.stdin.write(b"set title 'Performance analysis'\n")
        plot.stdin.write(b"set ylabel 'time in miliseconds'\n")
        plot.stdin.write(b"set xlabel 'matrix size n (the actual size of matrix is n x n)'\n")
        plot.stdin.write(b"set key  bottom right\n")
        plot.stdin.write(b"set yrange[0:*]\n")
        plot.stdin.write(b"plot '-' using 1:2 smooth csplines linecolor rgb 'green' title 'Java performance f(x)=O(N**2)' with lines\n")
        plot.stdin.write("\n".join("%f %f"%d for d in data).encode())
        plot.stdin.write(b"\ne\n")
        plot.stdin.flush()


    def plotHeatGraph(self):

        gnuplot = r'C:\Program Files (x86)\gnuplot\bin\gnuplot'
        plot=Popen([gnuplot,'-persist'],stdin=PIPE,stdout=PIPE,stderr=PIPE)
        plot.stdin.write(b"set title 'Performance analysis Heat map'\n")
        plot.stdin.write(b"set pm3d map\n")
        plot.stdin.write(b"set multiplot layout 1,2\n")
        plot.stdin.write(b"splot 'HeatdataJava.txt' matrix with image\n")
        plot.stdin.write(b"splot 'TransposeHeatdataJava.txt' matrix with image\n")
        #plot.stdin.write(b"splot '-' layout 2,1 matrix with image\n")
        #plot.stdin.write("\n".join("%s"%d for d in data2).encode())
        #plot.stdin.write(b"\ne\n")
        plot.stdin.flush() 
   

	

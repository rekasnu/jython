'''
* Author : Ermins Dreimanis
* St. No. SB12408
'''


import os
import time

import Model
import View
from view import Plot
plot = Plot()
m = Model()
v = View()
columns_rows = -3
increment = -2
start_columns_rows = -1
while(start_columns_rows<0):
    start_columns_rows = m.getInput("please enter the (min) number of columns and rows(n x n) of matrix (one integer number greater than 0): ")
while(columns_rows < start_columns_rows):
    columns_rows = m.getInput("please enter the (max) number of columns and rows(n x n) of matrix (one integer number): ")
'''
matrix1 = []
transpos = []
for a1 in range(columns_rows):
    for a2 in range(columns_rows):
        if(a2==0):
            datas = str(a1)
            datas2 = str(a2)
        if(a2>0):
            datas += ' '+str(a1)
            datas2 += ' '+str(a2)
    matrix1.append(datas)
    transpos.append(datas2)
''' 
#m.generateHeatMatrixes(columns_rows)

#plot.plotHeatGraph()

while(increment < 1):
    increment = m.getInput("increment value (one integer number) :")
m.generateHeatMatrixes(columns_rows,increment)

plot.plotHeatGraph()
x = raw_input('pres eny kay to continue')
data = []
totalTime =0
print "\nGenerating the matrix and transpose of matrix...\n"
for testMatrix in range(start_columns_rows,columns_rows,increment):
    matrix = m.generateMatrix(testMatrix)

    #v.printMatrix(matrix)
    start = time.time()
    m.transposeMatrix(matrix)
    end = time.time()
    #print "\n transpose matrix \n"
    #v.printMatrix(transpose)
    transposeTime = (end-start)*1000
    data.append((testMatrix, transposeTime))
    totalTime += transposeTime

print "\n Total transpose time for "+str(columns_rows)+" matrix in milliseconds : "+str(totalTime)

plot.plotGraph(data)



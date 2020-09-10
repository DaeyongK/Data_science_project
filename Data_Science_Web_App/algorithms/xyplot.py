# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:24:32 2020

@author: miked
"""

#Import libraries
import pandas as pandas
import matplotlib as matplotlib
import matplotlib.pyplot as pyplot

#File read
fileInput = pandas.read_csv("C:/Users/miked/Downloads/ford_escort.csv", sep=',')
#Which data column is x 
xColNInput = 0
#Which data column is y 
yColNInput = 2
#X axis label
xLblInput = None
#Y axis label
yLblInput = "Price ($)"
#Title
ttlInput = None
#X axis range
xRInput = [1994.5, 1998.5]
#Y axis range
yRInput = None

def xyplot(file, xColN, yColN, xLbl, yLbl, ttl, xR, yR):
    #Selects user input columns
    xCol = file.iloc[:, xColN]
    yCol = file.iloc[:, yColN]

    #Formatting that makes me happy
    matplotlib.rcParams['font.sans-serif'] = "Times New Roman"
    matplotlib.rcParams['font.family'] = "sans-serif"
    matplotlib.rcParams.update({'font.size': 15})

    #Creates figure
    fig = pyplot.figure()
    ax = fig.add_subplot()

    #Creates scatter plot
    ax.scatter(xCol, yCol, marker = "x", color = "red")

    #If axes labels not given, uses dataframe headers
    if xLbl == None:
        xLblF = file.columns[xColN]
        ax.set_xlabel(xLblF)
    else:
        xLblF = xLbl
        ax.set_xlabel(xLblF)
    if yLbl == None:
        yLblF = file.columns[yColN]
        ax.set_ylabel(yLblF)
    else:
        yLblF = yLbl
        ax.set_ylabel(yLblF)

    #Automatically determine title if not given
    if ttl == None:
        ax.set_title(yLblF + " vs. " + xLblF)
    else:
        ax.set_title(ttl)
        
    if xR != None:
        ax.set_xlim(xR[0], xR[1])
    if yR != None:
        ax.set_ylim(yR[0], yR[1])
        
    #Return figure
    return fig

#Execute
fig1 = xyplot(fileInput, xColNInput, yColNInput, xLblInput, yLblInput, ttlInput, xRInput, yRInput)

#Display Figure
pyplot.show()




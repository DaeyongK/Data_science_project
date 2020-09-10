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
fileInput = pandas.read_csv("C:/Users/miked/Downloads/hw_25000.csv", sep=',')
#Which data column is x 
xColNInput = 1
#Which data column is y 
yColNInput = 2
#X axis label
xLblInput = "Height (Inches)"
#Y axis label
yLblInput = "Weight (Lbs)"
#Title
ttlInput = None
#X axis range
xRInput = None
#Y axis range
yRInput = None
#Alpha
alphaValInput = 0.1

def xyplot(file, xColN, yColN, xLbl, yLbl, ttl, xR, yR, alphaVal):
    #Selects user input columns
    xCol = file.iloc[:, xColN]
    yCol = file.iloc[:, yColN]

    #Formatting that makes me happy
    matplotlib.rcParams['font.sans-serif'] = "Times New Roman"
    matplotlib.rcParams['font.family'] = "sans-serif"
    matplotlib.rcParams.update({'font.size': 15})
    matplotlib.rcParams['text.color'] = "black"
    matplotlib.rcParams['axes.labelcolor'] = "black"
    matplotlib.rcParams['xtick.color'] = "black"
    matplotlib.rcParams['ytick.color'] = "black"

    #Creates figure
    fig = pyplot.figure()
    ax = fig.add_subplot()

    #Creates scatter plot
    ax.scatter(xCol, yCol, marker = ".", color = "tab:orange", alpha = alphaVal)

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
fig1 = xyplot(fileInput, xColNInput, yColNInput, xLblInput, yLblInput, ttlInput, xRInput, yRInput, alphaValInput)

#Display Figure
pyplot.show()

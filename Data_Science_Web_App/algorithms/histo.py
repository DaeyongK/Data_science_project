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
colNInput = 1
#Which data column is y 
xLblInput = "Height (Inches)"
#Y axis label
yLblInput = None
#Title
ttlInput = None
#X axis range
xRInput = [60, 75]
#Y axis range
yRInput = None
#Hist style ("step", "bar")
hStyleInput = "step"
#Bin width
binPut = None
#Plot density?
densYesInput = True

def hist(file, colN, xLbl, yLbl, ttl, xR, yR, hStyle, binS, densYes):
    #Selects user input columns
    col = file.iloc[:, colN]

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

    #Contingency if no style is provided (basically saying default is bar)
    if hStyle == None:
        hStyle = "bar"

    #Creates scatter plot
    ax.hist(col, color = "tab:orange", density = True, histtype = hStyle, bins = binS)

    #Density function
    if densYes == True:
        col.plot(kind='density')
        
    #If axes labels not given, uses dataframe headers/#
    if xLbl == None:
        xLblF = file.columns[colN]
        ax.set_xlabel(xLblF)
    else:
        xLblF = xLbl
        ax.set_xlabel(xLblF)
    if yLbl == None:
        ax.set_ylabel("N (#)")
    else:
        yLblF = yLbl
        ax.set_ylabel(yLblF)

    #Automatically determine title if not given
    if ttl == None:
        ax.set_title("Histogram of " + xLblF)
    else:
        ax.set_title(ttl)
    
    #Set range if given
    if xR != None:
        ax.set_xlim(xR[0], xR[1])
    if yR != None:
        ax.set_ylim(yR[0], yR[1])
    
    #Set plot margins to 0
    pyplot.margins(0)
    
    #Return figure
    return fig

#Execute
fig1 = hist(fileInput, colNInput, xLblInput, yLblInput, ttlInput, xRInput, yRInput, hStyleInput, binPut, densYesInput)

#Display Figure
pyplot.show()
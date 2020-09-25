#Import libraries
import pandas as pandas
import matplotlib as matplotlib
import matplotlib.pyplot as pyplot
from scipy import interpolate

def xyplot(file, xColN, yColN, xLbl, yLbl, ttl, xR, yR, iKind):
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
    ax.scatter(xCol, yCol, marker = ".", color = "tab:orange")
    
    interF = interpolate.interp1d(xCol, yCol)
    
    ax.plot(xCol, interF(yCol))
    
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

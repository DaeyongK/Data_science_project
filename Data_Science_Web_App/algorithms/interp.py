#Import libraries
import pandas as pandas
import matplotlib as matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
from scipy import interpolate


def xyplot(file, xColN, yColN, xLbl, yLbl, ttl, xR, yR, alphaVal, interpkind):

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

    if alphaVal == "" or alphaVal == None:
        alphaVal = 20

    alphaVal /= 100

    #Creates interpolation function
    f = interpolate.interp1d(xCol, yCol, kind=interpkind)

    #Creates scatter plot
    ax.scatter(xCol, yCol, marker = ".", color = "tab:orange", alpha = alphaVal)

    #Creates interpolation plot
    pyplot.plot(xCol, f(xCol))

    #If axes labels not given, uses dataframe headers
    if xLbl == "":
        xLblF = file.columns[xColN]
        ax.set_xlabel(xLblF[2:-1])
    else:
        xLblF = xLbl
        ax.set_xlabel(xLblF)
    if yLbl == "":
        yLblF = file.columns[yColN]
        ax.set_ylabel(yLblF[2:-1])
    else:
        yLblF = yLbl
        ax.set_ylabel(yLblF)

    #Automatically determine title if not given
    if ttl == "":
        ax.set_title(yLblF[2:-1] + " vs. " + xLblF[2:-1])
    else:
        ax.set_title(ttl)

    if xR != "":
        ax.set_xlim(xR[0], xR[1])
    if yR != "":
        ax.set_ylim(yR[0], yR[1])

    #Return figure
    return fig

def range(file):
    intAr = file.split(',')
    intAr.sort()
    firstNum = intAr[0]
    lastNum = next(reversed(intAr))
    range = lastNum - firstNum
    return(range)

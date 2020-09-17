import statistics

def average(df):
    intAr = df.split(',')
    nums = list(map(int, intAr))
    avg = statistics.mean(nums)
    return(avg)

def median(df):
    intAr = df.split(',')
    intAr = list(map(int, intAr))
    intAr.sort()
    middleIndex = len(intAr)/2
    intMiddleIndex = int(middleIndex)

    if intMiddleIndex != middleIndex:
        return('is', intAr[intMiddleIndex], 'perfect')

    else:
        rightNum = int(intAr[intMiddleIndex])
        leftNum = int(intAr[intMiddleIndex - 1])
        trueMid = (rightNum + leftNum)/2
        return(leftNum, trueMid, rightNum)

def mode(df):
    intAr = df.split(',')
    nums = list(map(int, intAr))
    mode = statistics.multimode(nums)
    if len(mode) == len(nums):
        return (None)
    else:
        return(mode)

def strWSpace(int):
    return str(int) + ", "

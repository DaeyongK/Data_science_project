import statistics
import numpy as np

def strWSpace(int):
    return str(int) + ", "

def stdev(df):
    intAr = df.split(',')
    nums = list(map(int, intAr))

    #avg function
    avg = statistics.mean(nums)

    #Standard deviation function
    std = statistics.stdev(nums)

    #68.26% of values are from std1lower to std1upper
    std1lower = avg - std
    std1upper = avg + std
    #95.44% of values are from std2lower to std2upper
    std2lower = avg - (std*2)
    std2upper = avg + (std*2)
    #99.72% of values are from std3lower to std3upper
    std3lower = avg - (std*3)
    std3upper = avg + (std*3)

    #Variance function
    variance = statistics.variance(nums)

    #Median Function
    nums.sort()
    middleIndex = len(nums)/2
    intMiddleIndex = int(middleIndex)
    rightNum = None
    leftNum = None
    trueMid = None
    if intMiddleIndex != middleIndex:
        trueMid = nums[intMiddleIndex]
    else:
        rightNum = int(nums[intMiddleIndex])
        leftNum = int(nums[intMiddleIndex - 1])
        trueMid = (rightNum + leftNum)/2

    #First quartile
    Q1 = np.median(data[:int(len(nums)/2)])

    #Third quartile
    Q3 = np.median(data[int(len(nums)/2):])

    #Interquartile range
    IQR = Q3 - Q1

    #Returns everything
    return(std, std1lower, std1upper, std2lower, std2upper, std3lower,
    std3upper, variance, trueMid, Q1, Q3, IQR)

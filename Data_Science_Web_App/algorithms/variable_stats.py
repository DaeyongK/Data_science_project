import statistics
import numpy as np

def strWSpace(int):
    return str(int) + ", "

def variable_stats(df):
    intAr = df.split(',')
    nums = list(map(int, intAr))
    #Average function
    avg = statistics.mean(nums)
    #Mode function
    mode = statistics.multimode(nums)
    mode_return = None
    if not(len(mode) == len(nums)):
        mode_return = mode
    #Median Function
    nums.sort()
    middleIndex = len(nums)/2
    intMiddleIndex = int(middleIndex)
    rightNum = None
    leftNum = None
    trueMid = None

    if intMiddleIndex != middleIndex:
        rightNum = 'perfect'
        leftNum = 'is'
        trueMid = nums[intMiddleIndex]

    else:
        rightNum = int(nums[intMiddleIndex])
        leftNum = int(nums[intMiddleIndex - 1])
        trueMid = (rightNum + leftNum)/2

    #Standard Deviation Function
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

    #First quartile
    Q1 = np.median(nums[:int(len(nums)/2)])

    #Third quartile
    Q3 = np.median(nums[int(len(nums)/2):])

    #Interquartile range
    IQR = Q3 - Q1

    #Basic range function
    firstNum = nums[0]
    lastNum = next(reversed(nums))
    range = lastNum - firstNum

    #Returns everything
    return(avg, mode_return, leftNum, trueMid, rightNum, std, std1lower, std1upper, std2lower, std2upper, std3lower,
    std3upper, variance, Q1, Q3, IQR, range)

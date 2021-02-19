import statistics
import numpy as np

def strWSpace(int):
    return str(int) + ", "

def variable_stats(nums):
    # intAr = df.split(',')
    # nums = list(map(int, intAr))
    #Average function
    avg = round(statistics.mean(nums),10)
    #Mode function
    mode = statistics.multimode(nums)
    print(mode)
    for i in mode:
        i = round(i,10)
    print(mode)
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
        trueMid = round(nums[intMiddleIndex],10)

    else:
        rightNum = round(nums[intMiddleIndex],10)
        leftNum = round(nums[intMiddleIndex - 1],10)
        trueMid = round((rightNum + leftNum)/2,10)

    #Standard Deviation Function
    std = round(statistics.stdev(nums),10)

    #68.26% of values are from std1lower to std1upper
    std1lower = round(avg - std,10)
    std1upper = round(avg + std,10)
    #95.44% of values are from std2lower to std2upper
    std2lower = round(avg - (std*2),10)
    std2upper = round(avg + (std*2),10)
    #99.72% of values are from std3lower to std3upper
    std3lower = round(avg - (std*3),10)
    std3upper = round(avg + (std*3),10)

    #Variance function
    variance = round(statistics.variance(nums),10)

    #First quartile
    Q1 = round(np.median(nums[:int(len(nums)/2)]),10)

    #Third quartile
    Q3 = round(np.median(nums[int(len(nums)/2):]),10)

    #Interquartile range
    IQR = round(Q3 - Q1,10)

    #Basic range function
    firstNum = nums[0]
    lastNum = next(reversed(nums))
    range = round(lastNum - firstNum,10)

    #Returns everything
    return(avg, mode_return, leftNum, trueMid, rightNum, std, std1lower, std1upper, std2lower, std2upper, std3lower,
    std3upper, variance, Q1, Q3, IQR, range)

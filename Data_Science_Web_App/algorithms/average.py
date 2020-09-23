import statistics

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

    #Returns everything
    return(avg, mode_return, leftNum, trueMid, rightNum)

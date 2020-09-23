import statistics

def strWSpace(int):
    return str(int) + ", "

def stdev(df):
    intAr = df.split(',')
    nums = list(map(int, intAr))
    
    #Mean function
    mean = statistics.mean(nums)

    #Standard deviation function
    std = statistics.stdev(nums)

    #68.26% of values are from std1lower to std1upper
    std1lower = mean - std
    std1upper = mean + std
    #95.44% of values are from std2lower to std2upper
    std2lower = mean - (std*2)
    std2upper = mean + (std*2)
    #99.72% of values are from std3lower to std3upper
    std3lower = mean - (std*3)
    std3upper = mean + (std*3)

    #Variance function
    variance = statistics.variance(nums)

    #Returns everything
    return(std, std1lower, std1upper, std2lower,
    std2upper, std3lower, std3upper, variance)

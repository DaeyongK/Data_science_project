import statistics

def average(file):
    intAr = file.split(',')
    nums = list(map(int, intAr))
    avg = statistics.mean(nums)
    return(avg)

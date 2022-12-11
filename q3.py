def median(n_num):
    n_num.sort()
    n = len(n_num)
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    return median
def squares(l):
    return[i**2 for i in l]

def exercise3(l):
    average = sum(l)/len(l)
    maximum = max(l)
    med = median(l)
    minimum = min(l)
    S_l = squares(l)
    S_average = sum(S_l)/len(S_l)
    S_maximum = max(S_l)
    S_med = median(S_l)
    S_minimum = min(S_l)
    tuple1 = (minimum,average,med,maximum)
    tuple2 = (S_minimum,S_average,S_med,S_maximum)
    list_of_tuples = [tuple1,tuple2]
    return list_of_tuples

print(exercise3([1,2,3,4,5]))
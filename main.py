def times_three_plus_one(start):
    result = []
    while (start > 1):
        result.append(start)
        if (start % 2) == 1:
            start = 3 * start + 1
        else:
            start /= 2
        start = int(start)
    return result


s=[]
lenList=[]
maxValList=[]
maxValIndList=[]
for i in range(2, 100000):
    series = times_three_plus_one(i)
    s.append(i)
    ll = len(series)  # länge der Serie bis 1 erreicht
    m = max(series)  # maximal erreichter wert
    ind = series.index(m)  # nach wie vielen Iterationen
    lenList.append(ll)
    maxValList.append(m)
    maxValIndList.append(ind)
#    print('%5d %3d %5d %5d' % (i, ind, ll, m))

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7),dpi=100)
plt.title("Time 3 plus 1 Problem")
plt.xlabel("Starting value")
plt.ylabel("Maximum value reached")
plt.plot(s,maxValList,'b.')
#plt.plot(s,lenList,"r-")
plt.plot(y_scondary="Number of iterations")
plt.yscale("log")
plt.xscale("linear")
plt.savefig("Times3Plus1.pdf")
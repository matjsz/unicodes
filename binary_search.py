# A short binary search code I've made based on my course lectures.

def bin_search(v, l):
    l = l
    while True:
        t = int((len(l)/2)-1)
        if v > l[t]:
            l = list(filter(lambda x: x > l[t], l))
        elif v < l[t]:
            l = list(filter(lambda x: x < l[t], l))
        else:
            print(l[t])
            break
                
ln = list(range(0, 1025))
vt = 256

bin_search(vt, ln)

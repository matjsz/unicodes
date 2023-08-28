# algoritmo de ordenação com base no método bubble sort // ordination algorithm based on the bubble sort method

l = [5, 2, 4, 1, 0, 3]
k = 1

# versão curta // short version
while k < len(l):
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    k+=1

print(l)

# versão extendida // extended version
def ord_arr(l, rev=False):
    k = 1
    if rev:
        while k < len(l):
            for i in range(0, len(l)-1):
                if l[i] < l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
            k+=1
    else:
        while k < len(l):
            for i in range(0, len(l)-1):
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
            k+=1

l = [2, 4, 5, 0, 3, 1]
ord_arr(l)
print(l)

l = [5, 3, 4, 0, 1, 2]
ord_arr(l, True)
print(l)

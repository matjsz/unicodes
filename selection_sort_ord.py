# algoritmo de ordenação com base no método selection sort // ordination algorithm based on the selection sort method

l = [5, 2, 4, 1, 0, 3]

# versão curta // short version
for i in range(0, len(l)):
    for k in range(0, len(l)):
        if l[i] < l[k]:
            l[i], l[k] = l[k], l[i]

print(l)

# versão extendida // extended version
def ord_arr(arr, rev=False):
    if rev:
        for i in range(0, len(l)):
            for k in range(0, len(l)):
                if l[i] > l[k]:
                    l[i], l[k] = l[k], l[i]
    else:
        for i in range(0, len(l)):
            for k in range(0, len(l)):
                if l[i] < l[k]:
                    l[i], l[k] = l[k], l[i]

l = [3, 0, 4, 2, 5, 1]
ord_arr(l)
print(l)
l = [4, 3, 1, 0, 5, 2]
ord_arr(l, True)
print(l)

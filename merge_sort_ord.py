# algoritmo de ordenação com base no método merge sort // ordination algorithm based on the merge sort method

a = [5, 3, 4, 2, 1, 8, 7, 6]

def div_conq(a):
    k = len(a)//2
    return a[:k], a[k:]

l, r = div_conq(a)[0], div_conq(a)[1]
lists = [l, r]
arr = []
k = True

while k:
    for j in lists:
        if len(j) > 1:
            t1 = div_conq(j)[0]
            t2 = div_conq(j)[1]
            lists.append(t1)
            lists.append(t2)
        else:
            arr.append(j)
            k = False
        
j = 1

while j < len(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    j+=1

final_arr = []

for n in arr:
    final_arr.append(n[0])

print(lists)
print(final_arr)

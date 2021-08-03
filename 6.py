n = int(input('pls enter a number: '))

list_a = []

for i in range(n):

    if i == 0 or i == 1:
        list_a.append(1)
    
    else:
        fibo = list_a[i-1] + list_a[i-2]
        list_a.append(fibo)

print(list_a)
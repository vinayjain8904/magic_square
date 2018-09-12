
##magic square##
n = int(input(''))
a =  [ [ 0 for j in range(n) ]  for i in range(n) ]

i = int(0)
j = int(n/2)

for num in range(1,n*n+1):
    a[i][j] = num
    if num % n == 0 :
        i += 1
    else:
        i -= 1
        j += 1
        if i<0 : i = n-1
        if j==n : j = 0

for xx in a:
    print(xx)

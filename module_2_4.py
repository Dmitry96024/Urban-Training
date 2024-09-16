numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in range(2,int(len(numbers))+1):
    for j in range(2,i):
        if i % j == 0:
         not_primes.append(i)
    else:
        primes.append(i)
x=list(set(primes)-set(not_primes))
y=list(set(not_primes))
print('простые',x)
print('не простые',y)

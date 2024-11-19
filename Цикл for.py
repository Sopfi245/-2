primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in numbers:
    if i < 2:
        continue
    is_prime = True
    for k in range(2, int(i**0.5) + 1):
         if i % k == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)

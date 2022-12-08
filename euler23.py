import numpy as np
# from prime_sieve import gen_primes
from itertools import combinations,  chain

import numpy as np


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


def prod(l):
   return reduce(operator.mul, l, 1)
#
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


primes = primesfrom2to(28123)

def list_divisors(num):
    ''' Creates a list of all divisors of num
    '''

    prime_divisors = []
    primeindex = 0
    while num>1:
        p = primes[primeindex]
        while not num % p:
            prime_divisors.append(p)
            num = int(num / p)
        primeindex += 1


    list_divisors = []
    powersetje = powerset(prime_divisors)
    for i in powersetje:
        product = 1
        for j in i:

            product *= j
        list_divisors.append(product)
    return sorted(set(list_divisors))

    # return sorted(set(prod(fs) for fs in powerset(prime_divisors)))

limit = 28123




list_abundant_numbers = []

for i in range(1, limit):
    sum_of_divisors = sum(list_divisors(i))-i
    if sum_of_divisors > i:
        list_abundant_numbers.append(i)

print(list_abundant_numbers)
list_sum_abundant = []
for i in list_abundant_numbers:
    index = 0
    newnumber = list_abundant_numbers[index] + i
    while newnumber <= limit:
        list_sum_abundant.append(newnumber)
        index += 1
        newnumber = list_abundant_numbers[index] + i
total = sum(set(list_sum_abundant))
total1tolimit = int(limit*(limit+1)/2)
answer = total1tolimit-total
print(answer)


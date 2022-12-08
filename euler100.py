import math
notFound = True
N = 1000000000000
while notFound:
    N += 1
    B = math.ceil(math.sqrt(N*(N-1)/2))
    if N % 10000000 == 0:
        print(N, B)


    if 2*B*(B-1) == N*(N-1):
        notFound = False
        print("solution:", N, B)

% 1000930000000 707764390493
import numpy as np
import time
start_time = time.time()

length = 1000000
pathlist = np.zeros([length+1]).astype(int)
pathlist[1] = 1


def CollatzNext(n):
    if n%2 ==0:
        return int(n/2)
    else:
        return int(3*n+1)

index = 2



while index < length + 1:

    # print('---- ', index, ' ----')
    if pathlist[index] != 0:
        # print(index, "already done!", pathlist[index])
        pass
    else:
        templist = np.array([index]).astype(int)
        n = index
        while True:
            n = CollatzNext(n)
            # print(n)
            if n <= length and pathlist[n] != 0:

                break
            else:
                templist = np.append(templist, n)
        # print("templist", templist)
        for y in range(len(templist)):
            x = templist[y]
            if x < length+1:
                pathlist[x] = (len(templist)-y) + pathlist[n]
    index += 1
    # print("pathlist now", pathlist)
print(pathlist)
print("Max length of path for a number under one million is", pathlist.max())
print("it happens at index: " , pathlist.argmax())

print("Found in", (time.time() - start_time), "seconds")


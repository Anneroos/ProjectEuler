import math
from copy import deepcopy

def findCombinations(goal, coins, printCombinations=False):
    emptySet = dict([(coin, 0) for coin in coins])
    sets = [emptySet]
    for coin in reversed(coins):
        newSets = []
        for currentSet in sets:
            amountLeft = goal - sum([k*v for k,v in currentSet.items()])
            maxCoins = math.floor(amountLeft/coin)
            minCoins = 0 if coin != coins[0] else maxCoins
            for n in range(minCoins,maxCoins+1):
                newSet = deepcopy(currentSet)
                newSet[coin] = n
                newSets.append(newSet)
        sets = newSets
    sets = [ currentSet for currentSet in sets if sum([k * v for k, v in currentSet.items()]) == goal]
    finalCombos = ["-".join(["".join([str(k)]*combi[k]) for k in sorted(combi.keys())]) for combi in sets]
    if printCombinations:
        for f in sorted(finalCombos):
            print(f)
    return len(finalCombos)

print(findCombinations(200, [1, 2, 5, 10, 20, 50, 100, 200], printCombinations=True))
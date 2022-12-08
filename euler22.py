from string import ascii_lowercase
import numpy as np
text_file = open("euler22input.txt", "r")
input = text_file.read().split('\n')
text_file.close()
namelist = np.array( input[0].split(','))

print(namelist)

namelist2 =[ x.split("\"")[1] for x in  namelist]
print(namelist2)
namelist2 = np.sort(namelist2)
print(namelist2)

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def computeNameScore(name):
    score =0
    for i in range(len(name)):
        letterscore = int(LETTERS[name[i].lower()])
        # print(letterscore, 'ltscore')
        score += letterscore
        # print(score)
    return score

# print(LETTERS)

computeNameScore('GRAIN')

total = 0
for i in range(len(namelist2)):

    total += computeNameScore(namelist2[i])*(i+1)

print(total)
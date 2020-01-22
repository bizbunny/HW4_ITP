# collaborators: Linh Nguyen
# #### Problem 1 #######
# Answer

def indexes(wo, c):
    wordL = []
    for i, s in enumerate(wo):
        if c in s:
            wordL.append(int(i))
    return wordL


# #### Problem 2 #######
# Answer
def hasLetterCount(lst, numChar):
    wrd = []
    for h in lst:
        j = len(h)
        if j == numChar:
            wrd.append(h)
    return wrd


# #### Problem 3 #######
# Answer
def intersect(lst1, lst2):
    wrd = []
    for i in lst1:
        for j in lst2:
            if i == j:
                k = i = j
                if k not in wrd:
                    wrd.append(k)
    print(wrd)

# #### Problem 4 #######
# Answer
def describe(v):
	lst=[len(i) for i in v]
	if(len(set(lst))) > 1:
		return 'Invalid'
	if (len(lst)==lst[0]):
		return 'Square'
	else:
		return 'Rectangular'

# #### Problem 5 #######
# reference: https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# reference: https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540
# Answer
def identityMatrix(rank):
    sLst: List[List[int]] = [[0 for x in range(rank)] for y in range(rank)]
    for i in range(rank):
        sLst[i][i] = 1
    return sLst


if __name__ == '__main__':
    import doctest

    print(doctest.testfile('hw4_test.py', verbose=False))

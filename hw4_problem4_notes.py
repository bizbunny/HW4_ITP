Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def defmat(matrix):
    rCount = 0
    eCount = 0
    print('=====BEGIN MATRIX=====')
    for row in matrix:
        rCount += 1
        for element in row:
            if rCount < 2:
                eCount += 1
            print(element, end=" ")
        print("")
    print("=====END MATRIX=====")
    print('element ' + str(element))
    print('row ' + str(row))
    print('rCount ' + str(rCount))
    print('eCount ' + str(eCount))
    print('row1 ' + str(row[1]))
    print('row2 ' + str(row[2]))
    if len(row[1]) != len(row[2]):
        print('invalid')
    if rCount != eCount:
        if len(row[1]) == len(row[2]):
            print('Rectangular')
    if rCount == eCount:
        if len(row[1]) == len(row[2]):
            print('Square')

            
>>> '''Problem 4 notes: looks like the main problem I'm having is figuring out how to identify an invalid matrix.
The main thing figured out was comparing row1 and row2. Will have to change that to better identify what rows and
elements are in the fuction and using rows to single out invalid fucntions. ***ROWS!!!!!!!!!!!!!!'''

def defmat(matrix):
    rCount = 0
    eCount = 0
    print('=====BEGIN MATRIX=====')
    for row in matrix:
        if rCount>=1:
            print('len(row[rCount]): '+str(len(row[rCount])))
        rCount += 1
    for element in row:
        if rCount < 2:
            eCount += 1
        print(element, end=" ")
    print("")
    print("=====END MATRIX=====")
    print('element ' + str(element))
    print('row ' + str(row))
    print('rCount ' + str(rCount))
    print('eCount ' + str(eCount))

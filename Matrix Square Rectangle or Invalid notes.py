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
    n=0
    for r in matrix:
        if r[0]==r[n]:
            print('Rectangle')
        elif rCount==eCount:
            print('Square')
        elif r[0]!=r[n]:
            print('Invalid')
        n+=1

        
>>> tMSquare=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> tMRectangle=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
>>> tMNot=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14]]
>>> defmat(tMSquare)
=====BEGIN MATRIX=====
1 2 3 
4 5 6 
7 8 9 
=====END MATRIX=====
element 9
row [7, 8, 9]
rCount 3
eCount 3
Rectangle
Square
Square
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
    n=0
    for r in matrix:
        print(r[n])
        n+=1

        
>>> defmat(tMSquare)
=====BEGIN MATRIX=====
1 2 3 
4 5 6 
7 8 9 
=====END MATRIX=====
element 9
row [7, 8, 9]
rCount 3
eCount 3
1
5
9
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
    n=0
    for r in matrix:
        print(r[n-1])
        n+=1

        
>>> defmat(tMSquare)
=====BEGIN MATRIX=====
1 2 3 
4 5 6 
7 8 9 
=====END MATRIX=====
element 9
row [7, 8, 9]
rCount 3
eCount 3
3
4
8
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
    n=0
    for r in matrix:
        for e in r:
		e[n-1]++
		
SyntaxError: inconsistent use of tabs and spaces in indentation
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
    n=0
    for r in matrix:
        for e in r:
		e[n-1]+e[n]
		
SyntaxError: inconsistent use of tabs and spaces in indentation
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
    n=0
    for r in matrix:
	    for e in r:
		    print(e[n-1]+e[n])
		    n+=1

		    
>>> defmat(tMSquare)
=====BEGIN MATRIX=====
1 2 3 
4 5 6 
7 8 9 
=====END MATRIX=====
element 9
row [7, 8, 9]
rCount 3
eCount 3
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    defmat(tMSquare)
  File "<pyshell#23>", line 20, in defmat
    print(e[n-1]+e[n])
TypeError: 'int' object is not subscriptable
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
    n=0
    for r in matrix:
	    for e in r:
		    p=e[n-1]+e[n]
		    print(p)
		    n+=1

		    
>>> defmat(tMSquare)
=====BEGIN MATRIX=====
1 2 3 
4 5 6 
7 8 9 
=====END MATRIX=====
element 9
row [7, 8, 9]
rCount 3
eCount 3
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    defmat(tMSquare)
  File "<pyshell#26>", line 20, in defmat
    p=e[n-1]+e[n]
TypeError: 'int' object is not subscriptable
>>> def describe(tmp):
    lengths = [len(item) for item in tmp]

    if len(set(lengths)) > 1: 
        return 'Invalid'
    else:
        if len(lengths) == lengths[0]:
            return 'Squrare'
        else:
            return 'Rectangular'

        
>>> describe(tMSquare)
'Squrare'
>>> describe(tMRectangle)
'Rectangular'
>>> describe(tMNot)
'Invalid'
>>> 

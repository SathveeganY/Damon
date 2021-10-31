#To find transpose of given matrix
def transpose(X):
    Y = [[0 for x in range(rows)]for y in range(columns)]      #To store transpose result

    #Store transpose in list Y.
    for i in range(columns):
        for j in range(rows):
            Y[i][j] = X[j][i]
    X = Y
    return X

#To find Matrix A X Transpose(B):
def product(X,Y):
    Z = []                      #To store product of matrices in list
    for i in range(rows):
        p = []                  #To store product of each elements row wise in list.
        for j in range(rows):
            z = 0
            for k in range(columns):           #Find each elements in final result
                z += int(X[i][k])*int(Y[k][j])
            p.append(z)
        Z.append(p)                 #Store final result in list.

    #print Product of given matrices.
    for i in range(len(Z)):
        for j in range(len(Z[0])):
            print(Z[i][j],end=' ')
        print()

try:        #for error handling  
    #Input dimensions of matrices (Rows,Columns)        
    Enter_the_dimension = (input('Enter the dimension: ')).split(',')
    rows = int(Enter_the_dimension[0])
    columns = int(Enter_the_dimension[1])

    matrix = True
    elements_are_integers = True
    #Input matrix A
    print('Enter Matrix A: ')
    A = []
    for i in range(rows):
        if elements_are_integers == True:
            a = input().split()
            #for check input elements are integers.
            for k in a:
                if not k.isnumeric():
                    elements_are_integers = False
                    break
            A.append(a)
        else:break
    for j in A:
        if len(j) != columns:matrix = False

    if matrix == True and elements_are_integers == True:
        #Input matrix B
        print('Enter Matrix B: ')
        B = []
        for i in range(rows):
            if elements_are_integers == True:
                b = input().split()
                #for check input elements are integers.
                for k in b:
                    if k.isnumeric() == False:
                        elements_are_integers = False
                        break
                B.append(b)
        for j in B:
            if len(j) != columns:matrix = False
    
    if matrix == False:print('Invalid Matrix')
    elif elements_are_integers == False:print('Error')
    else:
        #Transpose of Matrix B
        B = transpose(B)

        #To print final result
        product(A,B)
        
except ValueError:                  #if code has any other errors.
    print('Error')
    
except IndexError:                  #if the entered matrix does not comply with the given dimensions
    print('Invalid Matrix')

# This function stores transpose of A[][] in B[][]
def transpose(A, B):
    for i in range(C):
        for j in range(R):
            B[i][j] = A[j][i]

#To store input
A = []

Result = 'Valid Matrix'
while True:
    m = input().split()
    if len(m) == 0:
        Result = 'Error'        #To avoid empty rows
        break
    elif m[0] == '-1':break
    else:A.append(m)
    
if Result != 'Error':
    
    #To handle errors
    Result = 'Valid Matrix'
    for i in range(len(A)-1):
        if len(A[i]) != len(A[i+1]):
            Result = 'Invalid Matrix'        #inconsistent number of elements
                
    if Result == 'Valid Matrix':
        R = len(A)                      #rows of given matrix
        C = len(A[0])                   #columns of given matrix

        # To store result
        B = [[0 for x in range(R)] for y in range(C)] 
          
        transpose(A, B)

        #To print transpose matrix
        for i in range(C):
            for j in range(R):
                print(B[i][j],end=' ')
            print()
    
    else:print(Result)

else:print(Result)          #print type of error

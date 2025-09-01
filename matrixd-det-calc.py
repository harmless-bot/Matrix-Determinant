#LETS GOOOOOOOOOOOOOOOOOOOOOOOO
import numpy as np


#minorgiver:


def minor(A,x,y):
    temp=np.delete(A,x,axis=0)
    minorf=np.delete(temp,y,axis=1)
    return np.array(minorf)

#minorsolver
def minorsolver(A):
    minorsolve=(np.array((A[1][1]*A[0][0])-(A[1][0]*A[0][1])))
    return minorsolve

#det
def dxd(X,G,g,u):
    det=minorsolver(g)*X[0][0]-X[0][1]*minorsolver(G)+X[0][2]*minorsolver(u)
    return(det)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#START

matrix=[]
for i in range(3):
    row = list(map(int,input(f"Row {i+1} :  ").split()))
    if len(row) != 3:

        exit()
    matrix.append(row)
mtrix=np.array(matrix)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#showwwwwwww
print("Your matrix:")
mat=np.array(mtrix)
rows = len(mat)
print("⎡", end=" ")
for j in range(len(mat[0])):
    print(mat[0][j], end=" ")
print("⎤")

for i in range(1, rows - 1):
    print("⎢", end=" ")
    for j in range(len(mat[0])):
        print(mat[i][j], end=" ")
    print("⎥")

print("⎣", end=" ")
for j in range(len(mat[0])):
    print(mat[rows-1][j], end=" ")
print("⎦")



#cofactor(top row)

a= minor(mtrix,0,0)
b= minor(mtrix,0,1)
c= minor(mtrix,0,2)


#det logic
det=minorsolver(a)*mtrix[0][0]-mtrix[0][1]*minorsolver(b)+mtrix[0][2]*minorsolver(c)
print("\nDeterminant =",det)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

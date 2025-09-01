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
#pretty matrix(taken ai help for this  bruh srry)
def format_minor(M):
    # assumes 2x2 minor
    top = f"⎡ {M[0][0]} {M[0][1]} ⎤"
    bot = f"⎣ {M[1][0]} {M[1][1]} ⎦"
    return top, bot




print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#START
while True:
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
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #det actual operation show for user
        A1, A2 = format_minor(a)
        B1, B2 = format_minor(b)
        C1, C2 = format_minor(c)

        lines = [
            f"{mtrix[0][0]} * {A1}",
            f"    {A2}",
            f"- {mtrix[0][1]} * {B1}",
            f"    {B2}",
            f"+ {mtrix[0][2]} * {C1}",
            f"    {C2}",
        ]
        print("\n".join(lines))

        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #det logic
        det=minorsolver(a)*mtrix[0][0]-mtrix[0][1]*minorsolver(b)+mtrix[0][2]*minorsolver(c)
        print("\nDeterminant =",det)

        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #giving ids to each element of 3*3 matrix:
        a=mtrix[0][0]
        b=mtrix[0][1]
        c=mtrix[0][2]
        d=mtrix[1][0]
        e=mtrix[1][1]
        f=mtrix[1][2]
        g=mtrix[2][0]
        h=mtrix[2][1]
        i=mtrix[2][2]
        #print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        # checks for matrices 1.2

        #print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #1. TRANSPOSE
        Tmatrix_manual = np.array([[a, d, g],
                                   [b, e, h],
                                   [c, f, i]])

        # Print the original and transposed matrices

        print(Tmatrix_manual,"=======================>Transpose of this matrix is:\n")

        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #logic===========>>>>>


        #symm logics
        if b==d and c==g and f==h:print("Your matrix is Symmteric Matrix")
        else:print("Your matrix is not Symmteric Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #SKEW SYMM logic
        if (b==-d and c==-g and f==-h) or (d==-b and g==-c and h==-f) :print("Your matrix is Skew Symmteric Matrix")
        else:print("Your matrix is not Skew Symmteric Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Upper Triangular logic:
        if d==0 and g==0 and h==0:
            print("Your matrix is Upper Triangular Matrix ")
        else:print("Your matrix is not Upper Triangular Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Lower Triangular logic:
        if b==0 and c==0 and f==0:
            print("Your matrix is Lower Triangular Matrix ")
        else:  print("Your matrix is not Lower Triangular Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Null matrix
        if a==0 and b==0 and c==0 and d==0 and e==0 and f==0 and g==0 and h==0 and i==0 :
            print("Your matrix is Null Matrix")
        else:print("Your matrix is not Null Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Identity Matrix
        if (a==1 and e==1 and i ==1 )and  (b==0 and c==0 and d==0 and f==0 and g==0 and h==0):
            print("Your matrix is Identity Matrix")
        else:print("Your matrix is not Identity Matrix")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        choice = input("\nDo you want to check another matrix? (y/n): ").strip().lower()
        if choice != "y":
            print("Exiting... Goodbye!")
            break
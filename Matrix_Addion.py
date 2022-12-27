mat1=[[1,2,3],
      [4,5,7],
      [7,8,9]]

mat2=[[9,8,7],
      [6,5,4],
      [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

def addition(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j]=m1[i][j]+m2[i][j]
    print("Addition of Matrix is :) ")
    for a in result:
        print(a)
print(addition(mat1, mat2))

def substraction(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j]=m1[i][j]-m2[i][j]
    print("Substraction of Matrix is :) ")
    for s in result:
        print(s)    
print(substraction(mat1, mat2))

def multiplication(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            result[i][j]=m1[i][j]*m2[i][j]
    print("Multiplication of Matrix is :) ")
    for m in result:
        print(m)
print(multiplication(mat1, mat2))

def transpose(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[j][i]=m1[i][j]
    print("Transpose of Matrix is :) ")
    for t in result:
        print(t)
    return ("Matrix Operation ")
print(transpose(mat1, result))
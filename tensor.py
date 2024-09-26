from numpy import array
from numpy import tensordot
A=array([
    [[1,2,3],[4,5,6],[7,8,9]],
     [[11,12,13],[14,15,16],[17,18,19]],
     [[21,22,23],[24,25,26],[27,28,29]]])
print(A.shape)
print("A matrix is:\n",A)
B=array([
    [[1,2,3],[4,5,6],[7,8,9]],
     [[11,12,13],[14,15,16],[17,18,19]],
     [[21,22,23],[24,25,26],[27,28,29]]])
print(B.shape)
print("B matrix is:\n",B)
print("tensor addition is:")
C=A+B
print(C.shape)
print("the addition of c is:\n",C)
print("tensor subtraction :")
S=A-B
print(S.shape)
print("the difference of s is:\n",S)
print("tensor multiplication:")
M=A*B
print(M.shape)
print("the multiplication of M:\n",M)
print("tensor division :")
DI=A/B
print(DI.shape)
print("the division is:\n",DI)
D=array([[3,4],[5,6]])
E=array([1,2])
F=tensordot(D,E,axes=0)
print("tensor when axes=0 is:\n",F)
F=tensordot(D,E,axes=1)
print("tensor when axes=1 is:\n",F)
f = open("date.txt", 'r')
A =f.readline().split()
B =f.readline().split()
C =f.readline().split()
D =f.readline().split()

A[0] = int(A[0])
A[1] = int(A[1])

B[0] = int(B[0])
B[1] = int(B[1])

C[0] = int(C[0])
C[1] = int(C[1])

D[0] = int(D[0])
D[1] = int(D[1])

def pct_min(Punct1, Punct2):
    if ( Punct1[0]  != Punct2[0]):
        if (Punct1[0] <= Punct2[0]):
            return Punct1
        return Punct2
    if (Punct1[1] <= Punct2[1]):
        return Punct1
    return Punct2

def pct_max(Punct1, Punct2):
    if ( Punct1[0]  != Punct2[0]):
        if (Punct1[0] >= Punct2[0]):
            return Punct1
        return Punct2
    if (Punct1[1] >= Punct2[1]):
        return Punct1
    return Punct2

#screim ecuatia punctelor

a1 = A[1] - B[1]
a2 = C[1] - D[1]
b1 = B[0] - A[0]
b2 = D[0] - C[0]
c1 = B[0] * A[1] - A[0] * B[1]
c2 = D[0] * C[1] - C[0] * D[1]
delta = a1 * b2 - b1 * a2       #det sistemului

#daca delta != 0 ;  Avem solutie UNICA --> Aplicam Cramer

if (delta != 0):
    x = ((B[0] * A[1] - A[0] * B[1]) * b2 - (D[0] * C[1] - C[0] * D[1]) * b1) / delta
    y = ((D[0] * C[1] - C[0] * D[1]) * a1 - (B[0] * A[1] - A[0] * B[1]) * a2) / delta
    if (x < min(A[0], B[0]) or x < min(C[0], D[0])):
        print("Intersectia este MULTIMEA VIDA")
        exit(0)
    if (x < max(A[0], B[0]) or x < max(C[0], D[0])):
        print("Intersectia este MULTIMEA VIDA")
        exit(0)
    print("Segmentele se intersecteaza in punctul:", x, " ", y)
    exit(0)

# Daca delta este egal cu 0, verificam daca rangul matricei este egal cu rangul extinsei
#Daca rangul extinsei este 2:
if (b1*c2 - b2*c1 != 0):
    print("Intersectia este MULTIMEA VIDA")
    exit(0)
if (a1*c2 - a2*c1 != 0):
    print("Intersectia este MULTIMEA VIDA")
    exit(0)

#daca rang extinsa == 1
#puncte colinare

min1 = pct_min(A, B)
min2 = pct_min(C, D)
max1 = pct_max(A, B)
max2 = pct_max(C, D)

if (min1 == min2 and max1 == max2):
    print("Segmentele sunt identice")
if (max2 < min1):
    print("Intersectia este MULTIMEA VIDA")
    exit(0)
if (max2 == min1):
    print("Segmentele se intersecteaza in punctul: (", min1[0],", ",  min1[1],")")
    exit(0)
if (min2 < min1):
    print("Segmentele se intersectaza in segmentul: (" , min1[0],", ",  min1[1],") , (", min(max1,max2)[0],", ", min(max1, max2)[1], ")")
    exit(0)
if (min1 == min2 and min2 == min(max1, max2)):
    print("Segmentele se intersecteaza in punctul (" , min1[0],", ",  min1[1],")")
    exit(0)
if (min2 < min(max1, max2)):
    print("Segmentele se intersectaza in segmentul: (" , min2[0],", ",  min2[1],") , (", min(max1, max2)[1], ", ", min(max1, max2)[1], ")")
    exit(0)
if (min2 == min(max1, max2)):
    print("Segmentele se intersecteaza in punctul (" , min2[0],", ",  min2[1],")")
    exit(0)

print("Intersectia este MULTIMEA VIDA")

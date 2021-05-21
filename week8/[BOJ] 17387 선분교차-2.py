# 17387 선분 교차 - 2
def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
A, B, C, D = [x1,y1], [x2,y2], [x3,y3], [x4,y4]

if ccw(A,B,C)*ccw(A,B,D) <= 0 and ccw(C,D,A)*ccw(C,D,B) <= 0:
    if ccw(A,B,C)*ccw(A,B,D) == 0 and ccw(C,D,A)*ccw(C,D,B) == 0:
        if (max(A[0],B[0]) >= min(C[0],D[0]) and max(C[0],D[0]) >= min(A[0],B[0])) and (max(A[1],B[1]) >= min(C[1],D[1]) and max(C[1],D[1]) >= min(A[1],B[1])):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
# 20149 - 선분교차 3
def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
A, B, C, D = [x1,y1], [x2,y2], [x3,y3], [x4,y4]

if ccw(A,B,C)*ccw(A,B,D) <= 0 and ccw(C,D,A)*ccw(C,D,B) <= 0:
    if ccw(A,B,C)*ccw(A,B,D) == 0 and ccw(C,D,A)*ccw(C,D,B) == 0:
        if (max(A[0],B[0]) >= min(C[0],D[0]) and max(C[0],D[0]) >= min(A[0],B[0])) and (max(A[1],B[1]) >= min(C[1],D[1]) and max(C[1],D[1]) >= min(A[1],B[1])):
            print(1)
            # 일직선 상일 경우 ( ccw가 모두 0 )
            if max(A[0],B[0]) == min(C[0],D[0]) and max(A[1],B[1]) == min(C[1],D[1]):
                print(min(C[0],D[0]),min(C[1],D[1])) # A-B // C-D 순서
            elif max(C[0],D[0]) == min(A[0],D[0]) and max(C[1],D[1]) == min(A[1],B[1]):
                print(min(A[0],B[0]),min(A[1],B[1])) # C-D // A-B 순서로 있을때
            # ㄱ자 형은?
            else:
                if ccw(A,B,D)*ccw(C,D,A)!=0 or ccw(A,B,C)*ccw(C,D,A)!=0:
                    print(*B)
                elif ccw(A,B,D)*ccw(C,D,B)!=0 or ccw(A,B,C)*ccw(C,D,B)!=0:
                    print(*A)

        else:
            print(0)
    else:
        print(1)
        if x2 != x1 and x4 != x3:
            g1, g2 = (y2 - y1) / (x2 - x1), (y4 - y3) / (x4 - x3)
            b1, b2 = -g1 * x1 + y1, -g2 * x3 + y3
            print((b1-b2)/(g2-g1),(g2*b1-g1*b2)/(g2-g1))
        elif x2 == x1 and x4 != x3:
            g2 = (y4-y3)/(x4-x3)
            print(x1,g2*(x1-x3)+y3)
        elif x4 == x3 and x2 != x1:
            g1 = (y2-y1) / (x2-x1)
            print(x3,g1*(x3-x1)+y1)
else:
    print(0)
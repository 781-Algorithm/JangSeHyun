# 11758 CCW 벡터의 외적 이용
points = []
for _ in range(3):
    points.append(list(map(int,input().split())))

def size(vector):
    return (vector[0]**2+vector[1]**2)**(1/2)

vec1 = [points[1][0]-points[0][0],points[1][1]-points[0][1]]
vec2 = [points[2][0]-points[1][0],points[2][1]-points[1][1]]
func = (vec1[0]*vec2[1]-vec1[1]*vec2[0])/(size(vec2)*size(vec1))

if func > 0:
    print(1)
elif func == 0:
    print(0)
else:
    print(-1)
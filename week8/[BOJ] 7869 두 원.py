# 7869 - 두 원
import math

x1,y1,r1,x2,y2,r2 = map(float,input().split())
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
answer = 0

if distance >= r1 + r2:
    answer = 0
elif distance <= abs(r1-r2) and r1>=r2:
    answer = math.pi*r2**2
elif distance <= abs(r1-r2) and r1<r2:
    answer = math.pi*r1**2
else:
    a = math.acos(((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))) * 2
    b = math.acos((r2**2+distance**2-r1**2)/(2*r2*distance))*2
    answer = 0.5*(r2**2)*(b-math.sin(b)) + 0.5*(r1**2)*(a-math.sin(a))

print("{:.3f}".format(answer))
import math

x,y,d,t=map(int,input().split())
distance=math.sqrt(x**2+y**2)

if distance>=d:
    jump=distance//d
    print("%.10f"%min(distance,jump*t+distance-(jump*d),(jump+1)*t))
else:
    print("%.10f"%min(distance,t+d-distance,2*t))
import math
AB = int(input())
BC = int(input())
hy = math.sqrt(AB**2+BC**2)
hy = hy/2.0
adj = BC/2.0
OP = int(round(math.degrees(math.acos(adj/hy))))
OP = str(OP)
print(OP+"°")

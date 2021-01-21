A  = set(input().split())
K = int(input())
subset = True
for i in range(K):
    s = set(input().split())
    if (s&A != s) or (s == A):
        subset = False
        break
print(subset)

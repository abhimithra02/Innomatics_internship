K = int(input())

for _ in range(K):
    x = input()
    X = set(input().split())
    y = int(input())
    Y = set(input().split())
    print(X.issubset(Y))

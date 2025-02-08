def solve():
    n = int(input(''))
    mat = []
    for i in range(n):
        zzz = list(map(int, input().split()))
        mat.append(zzz) 
    
    ans = 0

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                ans += mat[i][j]
                continue
            if i - j == 0:
                ans += mat[i][j]
                continue
            if j + i == n - 1:
                ans += mat[i][j]
                continue
            if i == (n - 1) // 2 or j == (n - 1) // 2:
                ans += mat[i][j]
        
    print(ans)
if __name__ == "__main__":
    t = 1
    # t = int(input().strip())
    for _ in range(t):
        solve()
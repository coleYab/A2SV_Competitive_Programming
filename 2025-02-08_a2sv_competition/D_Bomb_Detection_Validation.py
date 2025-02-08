def solve():
    n,m = map(int, input().split())

    inp = []
    for i in range(n):
        a = list(input())
        inp.append(a)
    
    # take each and validate then
    inbound = lambda i, j : 0 <= i < n and 0 <= j < m
    for i in range(n):
        for j in range(m):
            if inp[i][j] in [' ', "*" ]:
                continue 
            bmb_cnt = 0
            if inp[i][j] != ".":
                bmb_cnt = int(inp[i][j])
            if inbound(i - 1, j):
                if inp[i - 1][j] == "*":
                    bmb_cnt -= 1
            if inbound(i, j + 1):
                if inp[i][j + 1] == "*":
                    bmb_cnt -= 1
            if inbound(i + 1, j):
                if inp[i + 1][j] == "*":
                    bmb_cnt -= 1
            if inbound(i, j - 1):
                if inp[i][j - 1] == "*":
                    bmb_cnt -= 1
            if inbound(i + 1, j + 1):
                if inp[i + 1][j + 1] == "*":
                    bmb_cnt -= 1
            if inbound(i - 1, j - 1):
                if inp[i - 1][j - 1] == "*":
                    bmb_cnt -= 1
            if inbound(i + 1, j - 1):
                if inp[i + 1][j - 1] == "*":
                    bmb_cnt -= 1
            if inbound(i - 1, j + 1):
                if inp[i - 1][j + 1] == "*":
                    bmb_cnt -= 1
            if bmb_cnt != 0:
                print("NO")
                return
    
    print("YES")



if __name__ == "__main__":
    t = 1
    # t = int(input().strip())
    for _ in range(t):
        solve()
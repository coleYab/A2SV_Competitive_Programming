def solve():
    [n, m, k]  = list(map(int, input().split()))
    if m >= n and k >= n:
        print("Yes")
        return

    print("No")

if __name__ == "__main__":
    t = 1
    # t = int(input().strip())
    for _ in range(t):
        solve()
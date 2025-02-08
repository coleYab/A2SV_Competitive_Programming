def solve():
    _ = input()
    arr = list(map(int, input().split()))
    mins = min(map(abs, arr))
    print(mins)
if __name__ == "__main__":
    t = 1
    # t = int(input().strip())
    for _ in range(t):
        solve()
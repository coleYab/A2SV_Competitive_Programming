def solve():
    txt = input()

    if txt[0:len(txt) // 2] == txt[len(txt) // 2:]:
        print("YES")
        return

    print("NO")

if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()
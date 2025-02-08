def solve():
    # YourV code goes here
    _ = input()
    s = input()
    cypherd = []

    i = 0
    step = 1

    while i < len(s):
        cypherd.append(s[i])
        i += step 
        step += 1

    print("".join(cypherd))

if __name__ == "__main__":
    t = 1
    # t = int(input().strip())
    for _ in range(t):
        solve()
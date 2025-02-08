from collections import *

def solve():
    _ = input()
    s = input()
    c = Counter(s)
    rmed = set()
    ans = float("-inf")

    for i in range(len(s)):
        # check if it was in the dict
        if c[s[i]] == 1:  
            del c[s[i]]
        else:
            c[s[i]] -= 1

        rmed.add(s[i])
        a =len(c.keys()) + len(rmed)
        ans = max(ans,a )

    print(ans)

if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()
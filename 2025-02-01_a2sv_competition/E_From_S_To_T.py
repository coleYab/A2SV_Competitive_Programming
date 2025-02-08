import re

def solve():
    # Your code goes here
    s = input()
    t = input()
    p = input()

    freq = {}
    freq2 = {}
    for i in set(t):
        freq[i] = t.count(i)

    spt = s + p
    for i in set(spt):
        freq2[i] = spt.count(i)

    for k, v in freq.items():
        if k not in freq2 or v > freq2[k]:
            print("NO")
            return

    prev_idx = -1
    for i in s:
        next_idx = t.find(i, prev_idx + 1)
        if next_idx <= prev_idx or next_idx == -1:
            print("NO")
            return

        prev_idx = next_idx

    print("YES")


# axcb
# a next b next c


if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()

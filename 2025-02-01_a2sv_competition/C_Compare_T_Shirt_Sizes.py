def solve():
    [a, b] = list(map(str, input().split()))

    if compareLetter(a[-1], b[-1]) == 1:
        print(">")
        return

    if compareLetter(a[-1], b[-1]) == -1:
        print("<")
        return

    if a[-1] == "S" and len(a) < len(b):
        print(">")
        return

    if a[-1] == "S" and len(a) > len(b):
        print("<")
        return


    if a[-1] == "L" and len(a) < len(b):
        print("<")
        return

    if a[-1] == "L" and len(a) > len(b):
        print(">")
        return
    
    print("=")
        

def compareLetter(a , b):
    if a == b:
        return 0
    if a == "S":
        return -1
    if b == "S":
        return 1
    if b == "L":
        return -1
    if a == "L":
        return 1
    
    


if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()
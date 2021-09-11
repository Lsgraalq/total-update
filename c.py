import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
for i in range(5):
    (a, b, v) = [int(s) for s in input().split()]
    if 0<=a<=23:
        if 0<=b<60 and 0<=v<60:
                print("YES")
        else:
                print("NO")
    else:
            print("NO")

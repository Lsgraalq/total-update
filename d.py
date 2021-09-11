import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = int(input())
for i in range (1):
    if a <= 0:
        print("NO")
        print("2")
    if a > 0:
        if a%2 == 0:
            a += 2
            print('YES')
            print(a)
        else:
            a += 1
            print("NO")
            print(a)
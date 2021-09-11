import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = str(input())
a = [int(s) for s in input().split()]
print(sorted(a))
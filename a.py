import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(a, b, c) = [int(s) for s in input().split()]
(h, l,) = [int(s) for s in input().split()]
z = (a * b + a* c + b*c)*2-a*b
z = z - 0.15*z
x = h*0.001
p = l*0.001
c = x *p
c = c - 0.1 * c
u = z/c
print(math.ceil(u))
import math
import sys
# sys.stdin = open('sample.txt')
sys.stdin = open('input.txt')

# times
times = input().split()

# distances
distances = input().split()


def quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root, root
    else:
        return 0, 0


result = 1

for idx in range(1, len(times)):
    time = int(times[idx])
    distance = int(distances[idx])
    print('time:', time, 'distance:', distance)
    roots = quadratic_roots(-1, time, -distance)
    print('roots:', roots)
    if roots[1] - roots[0] > 0:
        left = math.ceil(roots[0]) if roots[0] < math.ceil(roots[0]) else math.ceil(roots[0]) + 1
        right = math.floor(roots[1]) if math.floor(roots[1]) < roots[1] else math.floor(roots[1]) - 1
        result *= right - left + 1
    print('current result:', result)

print('result:', result)

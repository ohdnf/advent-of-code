import math
import sys
# sys.stdin = open('sample.txt')
sys.stdin = open('input.txt')

# times
times = input().split()
time = int(''.join(times[1:]))

# distances
distances = input().split()
distance = int(''.join(distances[1:]))

print('time:', time, 'distance:', distance)


def get_range(time, distance):
    div = ((time ** 2) / 4 - distance) ** 0.5
    return time/2 - div, time/2 + div


result = 1
roots = get_range(time, distance)
print('roots:', roots)
if roots[1] - roots[0] > 0:
    left = math.ceil(roots[0]) if roots[0] < math.ceil(roots[0]) else math.ceil(roots[0]) + 1
    right = math.floor(roots[1]) if math.floor(roots[1]) < roots[1] else math.floor(roots[1]) - 1
    result *= right - left + 1

print('result:', result)

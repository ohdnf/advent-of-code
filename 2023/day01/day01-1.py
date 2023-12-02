import sys
sys.stdin = open('input1.txt')
result = 0

while True:
    try:
        line = input()
    except EOFError:
        break
    arr = []
    for char in line:
        if char.isdigit():
            arr.append(char)
    result += int(arr[0] + arr[-1])

print('result:', result)

import sys
sys.stdin = open('input2.txt')

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
result = 0


def find_digit(string, idx, length):
    if len(string) < idx + length or length > 5:
        return -1, 0
    if string[idx: idx + length] in digits:
        return digits[string[idx: idx + length]], length - 1
    else:
        return find_digit(string, idx, length + 1)


while True:
    try:
        line = input()
    except EOFError:
        break
    arr = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            arr.append(line[i])
            i += 1
            continue
        digit, length_of_letters = find_digit(line, i, 3)
        if digit > 0:
            arr.append(str(digit))
            i += length_of_letters
        else:
            i += 1
    result += int(arr[0] + arr[-1])

print('result:', result)

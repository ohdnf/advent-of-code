import sys

sys.stdin = open('input.txt')

result = 0


def process(subsets, counts):
    subsets = subsets.split(', ')
    for subset in subsets:
        amount, color = subset.split(' ')
        counts[color] = max(counts[color], int(amount))
    return counts


while True:
    try:
        game = input()
    except EOFError:
        break
    grabs = game.split('; ')
    game_id, first_grab = grabs[0].split(': ')
    grabs[0] = first_grab
    min_counts = {"blue": 0, "green": 0, "red": 0}
    for grab in grabs:
        min_counts = process(grab, min_counts)
    power = 1
    for val in min_counts.values():
        power *= val
    result += power

print('result: ', result)

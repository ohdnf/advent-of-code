import sys

sys.stdin = open('input.txt')

result = 0
max_cubes = {"blue": 14, "green": 13, "red": 12}


def is_passed(subsets):
    subsets = subsets.split(', ')
    for subset in subsets:
        amount, color = subset.split(' ')
        if max_cubes[color] < int(amount):
            return False
    return True


while True:
    try:
        game = input()
    except EOFError:
        break
    grabs = game.split('; ')
    game_id, first_grab = grabs[0].split(': ')
    grabs[0] = first_grab
    possible = True
    for grab in grabs:
        if not is_passed(grab):
            possible = False
            break
    if possible:
        result += int(game_id.split(' ')[-1])

print('result: ', result)

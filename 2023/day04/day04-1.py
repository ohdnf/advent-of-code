with open('input.txt', encoding='utf-8') as f:
    cards = f.readlines()
    result = 0
    for card in cards:
        _, numbers = card.split(': ')
        winning_numbers, rest_numbers = numbers.split('|')
        winning_numbers = set(winning_numbers.strip().split())
        rest_numbers = set(rest_numbers.strip().split())
        matches = winning_numbers & rest_numbers
        if len(matches):
            result += 2 ** (len(matches) - 1)
    print('result:', result)

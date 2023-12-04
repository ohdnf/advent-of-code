from collections import defaultdict

with open('input.txt', encoding='utf-8') as f:
    cards = f.readlines()
    num_of_instances = defaultdict(int)  # card_number: number_of_instances

    for card in cards:
        card, numbers = card.split(':')
        # get card number and init instance
        _, card_number = card.strip().split()
        card_number = int(card_number)
        num_of_instances[card_number] += 1
        # figure out card matches of winning number
        winning_numbers, rest_numbers = numbers.split('|')
        winning_numbers = set(winning_numbers.strip().split())
        rest_numbers = set(rest_numbers.strip().split())
        matches = len(winning_numbers & rest_numbers)
        # copy the cards
        if matches:
            end_number = card_number + matches
            for number in range(card_number + 1, end_number + 1):
                if number > len(cards):
                    break
                # cards will be copied as many as the current cards' instances exist
                num_of_instances[number] += num_of_instances[card_number]
    result = sum(num_of_instances.values())
    print('result:', result)

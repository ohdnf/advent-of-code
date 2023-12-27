import functools
from collections import Counter

STRENGTH = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}


def compare_strength(hand1, hand2):
    for i in range(5):
        if STRENGTH[hand1[0][i]] < STRENGTH[hand2[0][i]]:
            return 1
        elif STRENGTH[hand1[0][i]] > STRENGTH[hand2[0][i]]:
            return -1
    # never gonna happen
    return 0


# types = {
#     'five_card': [],
#     'four_card': [],
#     'full_house': [],
#     'triple': [],
#     'two_pair': [],
#     'one_pair': [],
#     'high_card': [],
# }
five_card = []
four_card = []
full_house = []
triple = []
two_pair = []
one_pair = []
high_card = []


def find_type(hand, bid):
    counter = Counter(hand).most_common(5)
    item = (hand, int(bid))
    # print(item, counter)
    if counter[0][1] == 5:
        # types['five_card'].append(item)
        five_card.append(item)
    elif counter[0][1] == 4:
        # types['four_card'].append(item)
        four_card.append(item)
    elif counter[0][1] == 3 and counter[1][1] == 2:
        # types['full_house'].append(item)
        full_house.append(item)
    elif counter[0][1] == 3 and counter[1][1] == 1:
        # types['triple'].append(item)
        triple.append(item)
    elif counter[0][1] == 2 and counter[1][1] == 2:
        # types['two_pair'].append(item)
        two_pair.append(item)
    elif counter[0][1] == 2 and counter[1][1] == 1:
        # types['one_pair'].append(item)
        one_pair.append(item)
    else:
        # types['high_card'].append(item)
        high_card.append(item)
    return


# with open('sample.txt', encoding='utf-8') as f:
with open('input.txt', encoding='utf-8') as f:
    hands = f.readlines()

    for hand in hands:
        hand, bid = hand.strip().split()
        find_type(hand, bid)

    five_card.sort(key=functools.cmp_to_key(compare_strength))
    four_card.sort(key=functools.cmp_to_key(compare_strength))
    full_house.sort(key=functools.cmp_to_key(compare_strength))
    triple.sort(key=functools.cmp_to_key(compare_strength))
    two_pair.sort(key=functools.cmp_to_key(compare_strength))
    one_pair.sort(key=functools.cmp_to_key(compare_strength))
    high_card.sort(key=functools.cmp_to_key(compare_strength))
    # print('five_card', five_card)
    # print('four_card', four_card)
    # print('full_house', full_house)
    # print('triple', triple)
    # print('two_pair', two_pair)
    # print('one_pair', one_pair)
    # print('high_card', high_card)


    def get_ranks(hands, result=0, start=0):
        rank = start
        for i in range(len(hands) - 1, -1, -1):
            rank += 1
            _, bid = hands[i]
            result += rank * bid
        return result, len(hands) + start

    result, start = get_ranks(high_card, 0, 0)
    print('high_card', result, start)
    result, start = get_ranks(one_pair, result, start)
    print('one_pair', result, start)
    result, start = get_ranks(two_pair, result, start)
    print('two_pair', result, start)
    result, start = get_ranks(triple, result, start)
    print('triple', result, start)
    result, start = get_ranks(full_house, result, start)
    print('full_house', result, start)
    result, start = get_ranks(four_card, result, start)
    print('four_card', result, start)
    result, start = get_ranks(five_card, result, start)
    print('five_card', result, start)

    print('result', result)

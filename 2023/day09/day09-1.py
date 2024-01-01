def extrapolate(sequence):
    if len(sequence) < 2:
        return sequence[-1]
    new_sequence = []
    all_zeroes = True
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        if diff:
            all_zeroes = False
        new_sequence.append(diff)
    if not all_zeroes:
        return sequence[-1] + extrapolate(new_sequence)
    return sequence[-1] + new_sequence[-1]


with open('input.txt') as f:
    histories = f.readlines()
    result = 0
    for history in histories:
        next_value = extrapolate(list(map(int, history.strip().split())))
        result += next_value
    print('result:', result)

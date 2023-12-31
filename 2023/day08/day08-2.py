from collections import Counter, defaultdict


def is_arrived(steps: list[int]):
    for step in steps:
        if not step:
            return False
    return True


def factorize(number):
    counter = Counter()
    max_prime = int(number ** 0.5)
    print(f'number: {number}, max_prime: {max_prime}')
    for prime in range(2, max_prime + 1):
        while number % prime == 0:
            counter[prime] += 1
            number /= prime
    return counter


def find_lcm(numbers):
    common_multiples = Counter()
    for number in numbers:
        print(factorize(number))
    return


with open('input.txt', encoding='utf-8') as f:
    directions = f.readline().strip()
    _ = f.readline()
    nodes = [e.strip().split(' = ') for e in f.readlines()]

    network = dict()
    curr_nodes = []
    for node, next_nodes in nodes:
        left, right = next_nodes.lstrip('(').rstrip(')').split(', ')
        network[node] = {'L': left, 'R': right}
        if node.endswith('A'):
            curr_nodes.append(node)
    print('network', network)
    print('curr_nodes', curr_nodes)
    arrived_steps = [0 for _ in range(len(curr_nodes))]
    print('arrived_steps', arrived_steps)
    LENGTH_OF_DIRECTIONS = len(directions)
    print('LENGTH_OF_DIRECTIONS', LENGTH_OF_DIRECTIONS)
    dir_idx = 0
    step = 0

    while not is_arrived(arrived_steps):
        if dir_idx == LENGTH_OF_DIRECTIONS:
            dir_idx = 0
        for node_idx, node in enumerate(curr_nodes):
            if node.endswith('Z'):
                arrived_steps[node_idx] = step
            curr_nodes[node_idx] = network[node][directions[dir_idx]]
        dir_idx += 1
        step += 1
        # print(f'step: {step}, idx: {dir_idx}, curr_nodes: {curr_nodes}')
    print('arrived_steps', arrived_steps)
    loops = [step // LENGTH_OF_DIRECTIONS for step in arrived_steps]
    print('loops', loops)
    # find_lcm(loops)
    print(f'curr: {curr_nodes}, step: {step}')
    result = LENGTH_OF_DIRECTIONS
    for loop in loops:
        result *= loop
    print('result', result)

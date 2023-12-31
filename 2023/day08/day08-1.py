with open('input.txt', encoding='utf-8') as f:
    directions = f.readline().strip()
    print('directions', directions)
    _ = f.readline()
    nodes = [e.strip().split(' = ') for e in f.readlines()]
    print(nodes)

    network = dict()
    for node, next_nodes in nodes:
        left, right = next_nodes.lstrip('(').rstrip(')').split(', ')
        network[node] = {'L': left, 'R': right}
    print(network)

    LENGTH_OF_DIRECTIONS = len(directions)
    curr = 'AAA'
    idx = 0
    step = 0

    while curr != 'ZZZ':
        if idx == LENGTH_OF_DIRECTIONS:
            idx = 0
        curr = network[curr][directions[idx]]
        idx += 1
        step += 1
    print(f'curr: {curr}, step: {step}')
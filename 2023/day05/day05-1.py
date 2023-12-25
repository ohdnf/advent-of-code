def find_destination(sources: list):
    visited = [False for _ in range(len(sources))]
    destinations = list()
    _ = f.readline()  # skip the map's name
    while True:
        line = f.readline().strip()
        if not line:
            break
        destination, start, length = map(int, line.split())
        for idx, source in enumerate(sources):
            if visited[idx]:
                continue
            if start <= source < start + length:
                destinations.append(destination + source - start)
                visited[idx] = True
    if len(destinations) != len(sources):
        for idx, source in enumerate(sources):
            if not visited[idx]:
                destinations.append(source)
    return destinations


with open('input.txt', encoding='utf-8') as f:
    seeds = set(map(int, f.readline().strip().removeprefix('seeds: ').split()))
    _ = f.readline()

    # print('seed_to_soil')
    seeds = find_destination(seeds)

    # print('soil_to_fertilizer')
    seeds = find_destination(seeds)

    # print('fertilizer_to_water')
    seeds = find_destination(seeds)

    # print('water_to_light')
    seeds = find_destination(seeds)

    # print('light_to_temperature')
    seeds = find_destination(seeds)

    # print('temperature_to_humidity')
    seeds = find_destination(seeds)

    # print('humidity_to_location')
    seeds = find_destination(seeds)

    print('the lowest location number:', min(seeds))

from collections import deque
import heapq as h


def find_destinations():
    result = list()
    _ = f.readline()  # skip the map's name
    while True:
        line = f.readline().strip()
        if not line:
            # exit if the line is empty
            break
        destination, source, length = map(int, line.split())
        result.append((source, source + length - 1, destination - source))
    result.sort(key=lambda e: e[0])
    return result


def relocate(sources, mappers):
    destinations = list()
    while len(sources):
        s_start, s_end = h.heappop(sources)
        for m_start, m_end, step in mappers:
            if s_end < m_start:
                # if the current source is not mapped
                h.heappush(destinations, (s_start, s_end))
                break
            if m_end < s_start:
                # move to the next mapping
                continue
            # find the remaining from both ends
            is_left_remain = s_start < m_start
            is_right_remain = m_end < s_end
            if is_left_remain and is_right_remain:
                h.heappush(destinations, (m_start + step, m_end + step))
                h.heappush(sources, (s_start, m_start - 1))
                h.heappush(sources, (m_end + 1, s_end))
            elif is_left_remain and not is_right_remain:
                h.heappush(destinations, (m_start + step, s_end + step))
                h.heappush(sources, (s_start, m_start - 1))
            elif not is_left_remain and is_right_remain:
                h.heappush(destinations, (s_start + step, m_end + step))
                h.heappush(sources, (m_end + 1, s_end))
            else:
                h.heappush(destinations, (s_start + step, s_end + step))
            # end iteration
            break
        else:
            # if the current source is not mapped
            h.heappush(destinations, (s_start, s_end))
    # push the rest of the sources
    return list(h.merge(sources, destinations))


with open('input.txt', encoding='utf-8') as f:
    # get seed numbers
    pairs = list(
        map(int, f.readline().strip().removeprefix("seeds: ").split())
    )  # start length
    seeds = [(pairs[i], pairs[i] + pairs[i + 1] - 1) for i in range(0, len(pairs), 2)]
    h.heapify(seeds)

    _ = f.readline()  # handle empty line

    seed_to_soil = find_destinations()
    soil = relocate(seeds, seed_to_soil)

    soil_to_fertilizer = find_destinations()
    fertilizer = relocate(soil, soil_to_fertilizer)

    fertilizer_to_water = find_destinations()
    water = relocate(fertilizer, fertilizer_to_water)

    water_to_light = find_destinations()
    light = relocate(water, water_to_light)

    light_to_temperature = find_destinations()
    temperature = relocate(light, light_to_temperature)

    temperature_to_humidity = find_destinations()
    humidity = relocate(temperature, temperature_to_humidity)

    humidity_to_location = find_destinations()
    location = relocate(humidity, humidity_to_location)

    print("the lowest location number:", min(location, key=lambda l: l[0])[0])

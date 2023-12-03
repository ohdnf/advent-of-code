import sys

sys.stdin = open('input.txt')
# sys.stdin = open('sample.txt')

schematic = []

while True:
    try:
        line = input()
        schematic.append(line)
    except EOFError:
        break

len_rows = len(schematic)
len_cols = len(schematic[0])
visited = [[False for _ in range(len_cols)] for _ in range(len_rows)]
result = 0

# explore the engine schematic
for row in range(len_rows):
    for col in range(len_cols):
        if visited[row][col]:
            continue
        elif schematic[row][col].isdigit():
            visited[row][col] = True
            end_col = col + 1
            # find whole part number
            while True:
                if end_col < len_cols and schematic[row][end_col].isdigit():
                    visited[row][end_col] = True
                    end_col += 1
                else:
                    break
            # find any symbols adjacent to the number
            is_symbol_found = False
            for new_row in range(row - 1, row + 2):
                if is_symbol_found:
                    break
                if 0 <= new_row < len_rows:
                    for new_col in range(col - 1, end_col + 1):
                        if is_symbol_found:
                            break
                        if 0 <= new_col < len_cols:
                            if not visited[new_row][new_col] and schematic[new_row][new_col] != '.':
                                is_symbol_found = True
                                break
            if is_symbol_found:
                # add number
                result += int(schematic[row][col:end_col])

print('result:', result)

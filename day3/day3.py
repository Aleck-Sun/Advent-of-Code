def find_adjacent_symbol(row, col, engine):
    def in_bounds(i, j):
        return 0 <= i < len(engine) and 0 <= j < len(engine[0])
    
    for x_off, y_off in [[0, -1], [0, 1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
        next_y, next_x = row + y_off, col + x_off
        if in_bounds(next_y, next_x) and engine[next_y][next_x] != '.' and not engine[next_y][next_x].isdigit():
            return True
    return False

def get_part_nums_part_one(row, line, engine):
    total = 0
    curr_num = 0
    has_adjacent_symbol = False
    for col, c in enumerate(line):
        if c.isdigit():
            if find_adjacent_symbol(row, col, engine):
                has_adjacent_symbol = True

            curr_num *= 10
            curr_num += int(c)
        else:
            if has_adjacent_symbol:
                total += curr_num

            has_adjacent_symbol = False
            curr_num = 0

    if has_adjacent_symbol:
        total += curr_num

    return total

def find_number(i, j, visited, engine):
    visited.add((i, j))
    curr_num = engine[i][j]

    left_scan = j - 1
    while left_scan >= 0 and engine[i][left_scan].isdigit():
        curr_num = engine[i][left_scan] + curr_num
        visited.add((i, left_scan))
        left_scan -= 1

    right_scan = j + 1
    while right_scan < len(engine[0]) and engine[i][right_scan].isdigit():
        curr_num = curr_num + engine[i][right_scan]
        visited.add((i, right_scan))
        right_scan += 1

    return int(curr_num)

def get_part_nums_part_two(row, line, engine):
    total = 0
    visited = set()
    for col, c in enumerate(line):
        if c == '*':
            part_numbers = []
            def in_bounds(i, j):
                return 0 <= i < len(engine) and 0 <= j < len(engine[0])
            
            for x_off, y_off in [[0, -1], [0, 1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
                next_y, next_x = row + y_off, col + x_off
                if (next_y, next_x) not in visited and in_bounds(next_y, next_x) and engine[next_y][next_x].isdigit():
                    part_numbers.append(find_number(next_y, next_x, visited, engine))

            if len(part_numbers) == 2:
                total += part_numbers[0] * part_numbers[1]
    return total

def load_engine():
    engine = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            engine.append([c for c in line.strip('\n')])
    return engine

def day3(get_part_nums):
    sum = 0
    engine = load_engine()
    for i, line in enumerate(engine):
        sum += get_part_nums(i, line, engine)
    return sum

if __name__ == "__main__":
    print(day3(get_part_nums_part_one))
    print(day3(get_part_nums_part_two))
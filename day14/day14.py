from heapq import heappush, heappop

CYCLES_SUBSET = 10000
BILLION = 1000000000

def move_north(grid):
    for j in range(len(grid[0])):
        periods = []
        for i in range(len(grid)):
            if grid[i][j] == '.':
                heappush(periods, i)
            elif grid[i][j] == '#':
                periods = []
            elif grid[i][j] == 'O' and periods:
                swap_i = heappop(periods)
                grid[i][j], grid[swap_i][j] = grid[swap_i][j], grid[i][j]
                heappush(periods, i)

def rotate_clockwise(grid):
    return list([list(e) for e in zip(*grid[::-1])])

def get_load(grid):
    return sum(grid[i].count('O') * (len(grid) - i) for i in range(len(grid)))

def day14_part_one():
    with open('test.txt', 'r') as f:
        grid = [list(line) for line in f.read().split('\n')]
        move_north(grid)
        return get_load(grid)

def day14_part_two():
    with open('input.txt', 'r') as f:
        grid = [list(line) for line in f.read().split('\n')]

        first_cycle_length = 0
        second_cycle_length, second_cycle = 0, []

        found = set()
        num_found, cycles = 0, []
        for _ in range(CYCLES_SUBSET):
            for _ in range(4):
                move_north(grid)
                grid = rotate_clockwise(grid)

            load = get_load(grid)
            cycles.append(load)

            if load in found:
                if not num_found:
                    first_cycle_length = len(cycles)
                elif num_found == 1:
                    second_cycle_length = len(cycles)
                    second_cycle = cycles

                num_found += 1
                if num_found == 3:
                    break

                found = set()
                cycles = []

            found.add(load)
            
        return (second_cycle + cycles)[(BILLION - first_cycle_length) % (len(cycles) + second_cycle_length) - 1]

if __name__ == '__main__':
    print(day14_part_two())

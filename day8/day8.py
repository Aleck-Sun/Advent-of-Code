import math

DIRECTION = { 'L':0, 'R':1 }

def generate_step_map(steps):
    mapping = {}
    for step in steps:
        start, neighbours = step.split('=')
        left, right = neighbours.split(',')
        mapping[start.strip()] = (left[2:], right[1:-1])
    return mapping

def day8_part_one():
    with open('input.txt', 'r') as f:
        input, steps = f.read().split('\n\n')
        mapping = generate_step_map(steps.split('\n'))
        
        steps = 0
        curr = 'AAA'
        while curr != 'ZZZ':
            curr = mapping[curr][DIRECTION[input[steps % len(input)]]]
            steps += 1
        return steps

def day8_part_two():
    with open('input.txt', 'r') as f:
        input, steps = f.read().split('\n\n')
        mapping = generate_step_map(steps.split('\n'))
        
        curr_starts = [start for start in mapping if start[2] == 'A']
        steps = [0] * len(curr_starts)

        for i, start in enumerate(curr_starts):
            while start[2] != 'Z':
                start = mapping[start][DIRECTION[input[steps[i] % len(input)]]]
                steps[i] += 1

        return math.lcm(*steps)

if __name__ == "__main__":
    print(day8_part_one())
    print(day8_part_two())
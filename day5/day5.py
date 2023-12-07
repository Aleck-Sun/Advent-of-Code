def get_seeds(line):
    return {int(seed):int(seed) for seed in line.split(':')[1].split()}

def day5_part_one():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        states = get_seeds(lines[0])
        for line in lines[1:]:
            if line.isspace():
                continue
            elif ":" in line:
                states = {int(next_state):int(next_state) for next_state in states.values()}
            else:
                start_next_state, start_state, range = line.split()
                for state in states:
                    if int(start_state) <= state < (int(start_state) + int(range)):
                        states[state] = int(start_next_state) + (state - int(start_state))
        return min(states.values())

def get_seeds_two(line):
    seed_map = []
    seeds = line.split(':')[1].split()
    for i in range(0, len(seeds), 2):
        seed, seed_range = int(seeds[i]), int(seeds[i+1])
        seed_map.append((seed, seed+seed_range-1))
    return seed_map

def build_state_map(line):
    state_map = {}
    states = line.split('\n')[1:]
    for state in states:
        next_start, start, num = state.split()
        next_start, start, num = int(next_start), int(start), int(num)
        state_map[(start, start+num-1)] = next_start-start
    return state_map

def day5_part_two():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n\n')
        states = get_seeds_two(lines[0])
        
        for line in lines[1:]:
            state_map = build_state_map(line)
            next_states = []

            for state in states:
                next_state = []
                curr_state = [state]
                while curr_state:
                    found = False
                    start, end = curr_state.pop()
                    for state_start, state_end in state_map:
                        difference = state_map[(state_start, state_end)]

                        if max(start, state_start) <= min(end, state_end):
                            new_start, new_end = max(start, state_start), min(end, state_end)
                            next_state.append((new_start + difference, new_end + difference))

                            if start < new_start:
                                curr_state.append((start, new_start-1))
                            if new_end < end:
                                curr_state.append((new_end+1, end))
                            found = True
                            break

                    if not found:
                        next_state.append((start, end))

                next_states += next_state
            states = next_states
        return min([state[0] for state in states])
    
if __name__ == "__main__":
    print(day5_part_one())
    print(day5_part_two())
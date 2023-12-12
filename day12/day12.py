def is_valid(schema, groups):
    schema_lengths = [len(group) for group in "".join(schema).split('.') if group]
    return schema_lengths == groups

def get_combinations(schema, groups, idx):
    if idx >= len(schema):
        return 1 if is_valid(schema, groups) else 0
    
    if schema[idx] != '?':
        return get_combinations(schema, groups, idx + 1)
    else:
        schema[idx] = '.'
        res = get_combinations(schema, groups, idx + 1)
        schema[idx] = '#'
        res += get_combinations(schema, groups, idx + 1)
        schema[idx] = '?'
        return res

def day12_part_one():
    with open('input.txt', 'r') as f:
        sum = 0
        input = f.read().split('\n')
        for line in input:
            schema = list(line.split()[0])
            groups = [int(x) for x in line.split()[1].split(',')]
            sum += get_combinations(schema, groups, 0)
        
        return sum

def day12_part_two():
    with open('test.txt', 'r') as f:
        sum = 0
        input = f.read().split('\n')
        for line in input:
            schema = list("?".join([line.split()[0]] * 5))
            groups = [int(x) for x in ",".join([line.split()[1]] * 5).split(',')]

            #sum += get_combinations(schema, groups, 0)
        
        return sum

if __name__ == "__main__":
    print(day12_part_two())
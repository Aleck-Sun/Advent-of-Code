TOTAL_CUBES = {'red':12, 'green':13, 'blue':14}

def get_id_value_part_one(line):
    game_header, games = line.split(':')
    game_id = game_header.split(' ')[1]
    games = games.split(';')

    for game in games:
        subsets = game.split(',')
        for i in range(len(subsets)):
            num, color = subsets[i].strip().split(' ')
            if int(num) > TOTAL_CUBES[color]:
                return 0
            
    return int(game_id)

def get_id_value_part_two(line):
    max_colors = {'red':0, 'green':0, 'blue':0}

    games = line.split(':')[1]
    games = games.split(';')

    for game in games:
        subsets = game.split(',')
        for i in range(len(subsets)):
            num, color = subsets[i].strip().split(' ')
            max_colors[color] = max(int(num), max_colors[color])
            
    return max_colors['red'] * max_colors['green'] * max_colors['blue']

def day2(get_id_value):
    sum = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            sum += get_id_value(line)

    return sum

if __name__ == "__main__":
    print(day2(get_id_value_part_one))
    print(day2(get_id_value_part_two))
def get_line_points(line):
    card_numbers = line.split(':')[1]
    winning_numbers_str, owned_numbers_str = card_numbers.split('|')
    winning_numbers = set(winning_numbers_str.split())
    
    total_matched = 0
    for num in owned_numbers_str.split():
        if num in winning_numbers:
            if not total_matched:
                total_matched += 1
            else:
                total_matched *= 2
    
    return total_matched

def day4_part_one():
    sum = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            sum += get_line_points(line)
    return sum

def get_card_matches(line):
    card_numbers = line.split(':')[1]
    winning_numbers_str, owned_numbers_str = card_numbers.split('|')
    winning_numbers = set(winning_numbers_str.split())
    
    total_matched = 0
    for num in owned_numbers_str.split():
        if num in winning_numbers:
            total_matched += 1
    
    return total_matched

def day4_part_two():
    card_matches = {}
    total_scratch_cards = 0
    with open('input.txt', 'r') as f:
        for card, line in enumerate(f.readlines()):
            matches = get_card_matches(line)
            card_matches[card+1] = matches

        num_scratch_cards = {card:1 for card in card_matches.keys()}
        for card in card_matches.keys():
            for obtained_card in range(card + 1, card + card_matches[card] + 1):
                if obtained_card not in num_scratch_cards:
                    break
                num_scratch_cards[obtained_card] += num_scratch_cards[card]

        total_scratch_cards = sum(num_scratch_cards.values())
    return total_scratch_cards
        

if __name__ == "__main__":
    print(day4_part_one())
    print(day4_part_two())
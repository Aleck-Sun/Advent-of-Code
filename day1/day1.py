def part_one_get_calibration(str):
    l, r = 0, len(str) - 1
    while not str[l].isdigit() or not str[r].isdigit():
        if not str[l].isdigit():
            l += 1
        if not str[r].isdigit():
            r -= 1

    return int(str[l] + str[r])

digits = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
def part_two_calibration(str):
    leftmost_num = [None, None]
    rightmost_num = [None, None]
    for digit, value in digits.items():
        idx = str.find(digit)
        if idx != -1 and (leftmost_num[0] is None or leftmost_num[0] > idx):
            leftmost_num = [idx, value]

        idx = str.rfind(digit)
        if idx != -1:
            idx += len(digit) - 1
            if (rightmost_num[0] is None or rightmost_num[0] < idx):
                rightmost_num = [idx, value]

    return leftmost_num[1] * 10 + rightmost_num[1]


def day1(get_calibration):
    sum = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            sum += get_calibration(line)

    return sum


if __name__ == "__main__":
    print(day1(part_one_get_calibration))
    print(day1(part_two_calibration))
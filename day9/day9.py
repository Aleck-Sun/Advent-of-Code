def find_next_part_one(nums):
    if sum(nums) != 0:
        next_nums = []
        for i in range(len(nums) - 1):
            next_nums.append(nums[i+1] - nums[i])
        nums.append(nums[-1] + find_next_part_one(next_nums))

    return nums[-1]

def find_next_part_two(nums):
    if sum(nums) != 0:
        next_nums = []
        for i in range(len(nums) - 1):
            next_nums.append(nums[i+1] - nums[i])
        nums.insert(0, (nums[0] - find_next_part_two(next_nums)))

    return nums[0]

def day9(find_next):
    with open('input.txt', 'r') as f:
        sum = 0
        lines = f.read().split('\n')
        for line in lines:
            sum += find_next([int(e) for e in line.split()])

        return sum

if __name__ == "__main__":
    print(day9(find_next_part_one))
    print(day9(find_next_part_two))
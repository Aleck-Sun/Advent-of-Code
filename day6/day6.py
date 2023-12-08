def day6_part_one():
    with open('input.txt', 'r') as f:
        times, distances = f.read().split('\n')
        times = times.split(':')[1].split()
        distances = distances.split(':')[1].split()
        
        ans = 1
        for race in range(len(times)):
            wins = 0
            for speed in range(0, int(times[race]) + 1):
                distance = int(times[race]) - speed
                if speed * distance >= int(distances[race]):
                    wins += 1
            ans *= wins
        
        return ans
    
def day6_part_two():
    with open('input.txt', 'r') as f:
        times, distances = f.read().split('\n')
        time = "".join(times.split(':')[1].split())
        distance = "".join(distances.split(':')[1].split())
        
        ans = 0
        for speed in range(0, int(time) + 1):
            distances = int(time) - speed
            if (speed * distances) >= int(distance):
                ans += 1
        return ans

if __name__ == "__main__":
    print(day6_part_one())
    print(day6_part_two())
def main():
    save = []

    with open('Dec2/ids.txt', 'r') as file:
        line = file.readlines()
        for l in line:
            # print(l.split(','))
            save = l.split(',')
        
    ranges = []
    for s in save:
        ranges.append(s.split('-'))
        
    sum_invalid_ids = 0

    # going to each pair with start and end ranges
    for i in range(len(ranges)):
        start = int(ranges[i][0]) 
        end = int(ranges[i][1])
        
        # if is_valid_range(len(str(end))): 
            # go through the numbers from start to end
        for num in range(start, end + 1):
            # if size of num is even, do something. If not, ignore it
            num_str = str(num)
            if is_valid_range(len(num_str)):
                half = len(num_str) // 2
                first_half = num_str[:half]
                last_half = num_str[half:]
                if first_half == last_half:
                    sum_invalid_ids += num
                    
    print("solution for Part 1:")
    print(sum_invalid_ids)
                
def is_valid_range(num):
    return num % 2 == 0 # if it is even returns true, otherwise it returns false

main()
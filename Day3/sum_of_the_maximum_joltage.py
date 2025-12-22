with open("Dec3/joltage.txt") as file:
    lines = file.readlines()
    jolts = 0
    total_jolts = 0
    
    for line in lines:
        
        """
        ALL THE SAME LINE WORK
        """
        biggest_number = -1
        second_biggest = -1

        index_biggest = -1
        index_second_biggest = -1
        
        list_number = list(line.strip()) # make the line a list
        
        for i in range(len(list_number) - 1):
            # find the biggest number and index
            if int(list_number[i]) > biggest_number:
                biggest_number = int(list_number[i])
                index_biggest = i
        
        # find the second biggest and index
        for i in range(index_biggest + 1, len(list_number)):
            if int(list_number[i]) > second_biggest:
                second_biggest = int(list_number[i])
                index_second_biggest = i
        
        jolts = str(biggest_number) + str(second_biggest)
        total_jolts += int(jolts)
        
    print("solution for Part 1:")
    print(total_jolts)
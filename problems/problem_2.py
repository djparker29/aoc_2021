with open('./sources/aoc_p2.txt', 'r') as f:
    lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))
    directions = {"down": 1, "up": -1, "forward": 1}
    
    position = [0, 0]
    for line in lines:
        direction, distance = line.split()

        if direction == 'forward' :
            position[0] += int(distance) * directions[direction]
        else:
            position[1] += int(distance) * directions[direction]
    
    updated_position = [0, 0, 0]
    for line in lines:
        direction, distance = line.split()

        if direction == 'forward' :
            updated_position[0] += int(distance) * directions[direction]
            updated_position[1] += int(distance) * updated_position[2] * directions[direction]
        else:
            updated_position[2] += int(distance) * directions[direction]

    print(f"Part one position is: {position[0] * position[1]}")
    print(f"Part two position is: {updated_position[0] * updated_position[1]}")

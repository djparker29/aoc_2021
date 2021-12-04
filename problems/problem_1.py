with open('./sources/aoc_p1.txt', 'r') as f:
    lines = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))
    count_one = sum([1 if lines[i] > lines[i - 1] else 0 for i in range(1, len(lines))])
    three_number_sums = []
    for i in range(2, len(lines)):
        three_number_sums.append(lines[i - 2] + lines[i - 1] + lines[i])
    
    count_two = sum([1 if three_number_sums[i] > three_number_sums[i - 1] else 0 for i in range(1, len(three_number_sums))])

    print(f"Part 1 count is: {count_one}")
    print(f"Part 2 count is: {count_two}")


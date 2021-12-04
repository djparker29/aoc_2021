def find_most_common(lines, position):
    zero_counts = 0
    one_counts = 0
    for line in lines:
        if line[position] == '0':
            zero_counts += 1
        else:
            one_counts += 1

    return 1 if one_counts >= zero_counts else 0


with open('./sources/aoc_p3.txt', 'r') as f:
    lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))

    gamma = ''
    epsilon = ''
    for i in range(len(lines[0])):
        most_common = find_most_common(lines, i)
        if most_common == 1:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    oxygen_generator_rating = lines[:]
    co2_scrubber_rating = lines[:]

    # Filter values for oxygen_generator_rating
    for i in range(len(lines[0])):
        if len(oxygen_generator_rating) == 1:
            break

        most_common = int(bool(find_most_common(oxygen_generator_rating, i)))
        if most_common == 1:
            oxygen_generator_rating = list(filter(lambda x: x[i] == '1', oxygen_generator_rating))
        else:
            oxygen_generator_rating = list(filter(lambda x: x[i] == '0', oxygen_generator_rating))

    # Filter values for co2_scrubber_rating
    for i in range(len(lines[0])):
        if len(co2_scrubber_rating) == 1:
            break

        most_common = int(not bool(find_most_common(co2_scrubber_rating, i)))
        if most_common == 1:
            co2_scrubber_rating = list(filter(lambda x: x[i] == '1', co2_scrubber_rating))
        else:
            co2_scrubber_rating = list(filter(lambda x: x[i] == '0', co2_scrubber_rating))

    print(f"Part 1 gamma rate: {int(gamma, 2) * int(epsilon, 2)}")
    print(f"Part 2 life support rating: {int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)}")

    
        
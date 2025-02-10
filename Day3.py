#Part 1
commands = [x.strip() for x in open('./day3input.txt')]
#print(commands)

gamma=""
epsilon=""

# Get the number of bits in each binary number
bit_count = len(commands[0])

for i in range(bit_count):
    bit_column = [command[i] for command in commands]
    count_0 = bit_column.count('0')
    count_1 = bit_column.count('1')
    if count_1 > count_0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)

power_consumption = gamma_decimal * epsilon_decimal

print("Part 1 Results:")
print(f"Gamma Rate (binary): {gamma}")
print(f"Epsilon Rate (binary): {epsilon}")
print(f"Gamma Rate (decimal): {gamma_decimal}")
print(f"Epsilon Rate (decimal): {epsilon_decimal}")
print(f"Power Consumption: {power_consumption}")

#Part 2
commands = [x.strip() for x in open('./day3input.txt')]

def find_rating(commands, criteria):
    filtered = commands[:]
    bit_count = len(commands[0])

    for i in range(bit_count):
        if len(filtered) == 1:
            break
        
        # Count occurrences of '0' and '1' at position `i`
        bit_column = [num[i] for num in filtered]
        count_0 = bit_column.count('0')
        count_1 = bit_column.count('1')

        # Determine the desired bit based on the criteria
        if criteria == "oxygen":
            desired_bit = '1' if count_1 >= count_0 else '0'
        elif criteria == "co2":
            desired_bit = '0' if count_0 <= count_1 else '1'
        
        # Filter the numbers based on the desired bit
        filtered = [num for num in filtered if num[i] == desired_bit]

    return int(filtered[0], 2)  # Convert the final binary number to decimal

# Calculate the ratings
oxygen_gen_rating = find_rating(commands, "oxygen")
co2_scrubber_rating = find_rating(commands, "co2")

# Calculate the life support rating
life_support_rating = oxygen_gen_rating * co2_scrubber_rating

print("Part 2 Results:")
print(f"Oxygen Generator Rating (decimal): {oxygen_gen_rating}")
print(f"CO2 Scrubber Rating (decimal): {co2_scrubber_rating}")
print(f"Life Support Rating: {life_support_rating}")
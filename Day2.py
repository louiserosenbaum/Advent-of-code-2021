#Part 1
commands = [x.strip() for x in open('./day2input.txt')]

horizontal_position = 0
depth = 0


for command in commands:
    direction, value = command.split()
    value = int(value)

    if direction == "forward":
        horizontal_position += value
    elif direction == "down":
        depth += value
    elif direction == "up":
        depth -= value

print(f"Final Horizontal Position1: {horizontal_position}")
print(f"Final Depth1: {depth}")
print(f"Product1: {horizontal_position * depth}")

#Part 2
commands = [x.strip() for x in open('./day2input.txt')]

horizontal_position = 0
depth = 0
aim = 0

for command in commands:
    direction, value = command.split()
    value = int(value)

    if direction == "forward":
        horizontal_position += value
        depth += aim * value  # Update depth based on aim
    elif direction == "down":
        aim += value  # Update aim instead of depth
    elif direction == "up":
        aim -= value  # Update aim instead of depth

print(f"Final Horizontal Position2: {horizontal_position}")
print(f"Final Depth2: {depth}")
print(f"Product2: {horizontal_position * depth}")
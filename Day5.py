#Part 1
'''with open('./day5input.txt') as f:
    commands = [line.strip() for line in f]

lines = []
for cmd in commands:
    start, end = cmd.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    lines.append(((x1, y1), (x2, y2)))

# Step 2: Initialize grid to count line overlaps
from collections import defaultdict
grid = defaultdict(int)

# Step 3: Process each line (horizontal, vertical, and diagonal)
for (x1, y1), (x2, y2) in lines:
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[(x1, y)] += 1
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[(x, y1)] += 1

# Step 4: Count points where at least two lines overlap
overlapping_points = sum(1 for count in grid.values() if count >= 2)

# Step 5: Print the result
print(overlapping_points)'''

#Part 2
with open('./day5input.txt') as f:
    commands = [line.strip() for line in f]

lines = []
for cmd in commands:
    start, end = cmd.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    lines.append(((x1, y1), (x2, y2)))

# Step 2: Initialize grid to count line overlaps
from collections import defaultdict
grid = defaultdict(int)

# Step 3: Process each line (horizontal, vertical, and diagonal)
for (x1, y1), (x2, y2) in lines:
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[(x1, y)] += 1
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[(x, y1)] += 1        
    else:  # Diagonal (45 degrees)
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        for i in range(abs(x2 - x1) + 1):
            grid[(x1 + i * dx, y1 + i * dy)] += 1

# Step 4: Count points where at least two lines overlap
overlapping_points = sum(1 for count in grid.values() if count >= 2)

# Step 5: Print the result
print(overlapping_points)
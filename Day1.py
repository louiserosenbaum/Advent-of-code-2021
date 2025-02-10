#Part 1
input = [int(x.strip()) for x in open('./day1input.txt')]
count = 0
prev = 0

for i in input:
    if prev < i:
        count += 1
    prev = i

print(count - 1)


#Part 2
count = 0
prev_sum = sum(input[:3])

for i in range(len(input) - 2):
    current_sum = sum(input[i:i+3])
    if current_sum > prev_sum:
        count += 1
    prev_sum = current_sum

print(count)
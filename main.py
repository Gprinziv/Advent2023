with open("input") as f:
    patterns = [pattern.splitlines() for pattern in f.read().split("\n\n")]

print(patterns)

cols, rows = 0, 0
for pattern in patterns:
    for j in range(1, len(pattern)):
        top, bot = j-1, j
        while pattern[top] == pattern[bot]:
            top -= 1
            bot += 1
            if top < 0 or bot >= len(pattern):
                rows += j
                print(f"Reflection between row {j-1} and {j}.")
                break
    for i in range(1, len(pattern[0])):
        left, right = i-1, i
        while all([line[left] == line[right] for line in pattern]):
            left -= 1
            right += 1
            if left < 0 or right >= len(pattern[0]):
                cols += i
                print(f"Reflection between column {i-1} and {i}.")
                break
print(f"Final Score: {100 * rows + cols}")
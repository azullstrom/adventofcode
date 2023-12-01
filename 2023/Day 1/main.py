input_file = 'input.txt'
data = open(input_file).read().split()

total_sum = 0

for text_row in data:
    first_digit = None
    last_digit = None

    for letter in text_row:
        if letter.isdigit():
            first_digit = letter
            break
    for letter in reversed(text_row):
        if letter.isdigit():
            last_digit = letter
            break
    total_sum += int(first_digit + last_digit)

print(total_sum)   
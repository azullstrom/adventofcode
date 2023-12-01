def normalize_text_row(text_row): 
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    for i, digit in enumerate(digits):
        if digit in text_row:
            replacement = digit[0] + str(i + 1) + digit[1:]
            text_row = text_row.replace(digit, replacement)

    return text_row

if __name__ == '__main__':
    input_file = 'input.txt'
    data = open(input_file).read().split()

    total_sum = 0

    for i, text_row in enumerate(data):
        first_digit = None
        last_digit = None

        text_row = normalize_text_row(text_row)
        print(text_row)

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


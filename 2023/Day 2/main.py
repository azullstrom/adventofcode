input_file = 'input.txt'
data = open(input_file).read().split('\n')

game_scores = []

for game in data:
    red_max = 0
    green_max = 0
    blue_max = 0
    red_temp = 0
    green_temp = 0
    blue_temp = 0
    for j, char in enumerate(game):
        if j < len(game) - 1 and char != ';':
            if char.isdigit() and not game[j-1].isdigit() and game[j+2] == 'r':
                red_temp += int(char)
            elif char.isdigit() and not game[j-1].isdigit() and game[j+2] == 'g':
                green_temp += int(char)
            elif char.isdigit() and not game[j-1].isdigit() and game[j+2] == 'b':
                blue_temp += int(char)
            elif char.isdigit() and game[j+1].isdigit() and game[j+3] == 'r':
                red_temp += int(char + game[j+1])
            elif char.isdigit() and game[j+1].isdigit() and game[j+3] == 'g':
                green_temp += int(char + game[j+1])
            elif char.isdigit() and game[j+1].isdigit() and game[j+3] == 'b':
                blue_temp += int(char + game[j+1])
        else:
            if red_temp > red_max:
                red_max = red_temp
            if green_temp > green_max:
                green_max = green_temp
            if blue_temp > blue_max:
                blue_max = blue_temp
            red_temp = 0
            green_temp = 0
            blue_temp = 0
    game_scores.append([red_max, green_max, blue_max])

cubes_rgb = [12, 13, 14]
part_one = 0
part_two = 0 

for i, game in enumerate(game_scores, 1):
    if all(c <= cubes for c, cubes in zip(game, cubes_rgb)):
        part_one += i
    part_two += game[0] * game[1] * game[2]
print(part_one, part_two)



# Hur många vänsterskor finns det? 8
# Hur många högerskor finns det? 5
# Det finns 5 par och 3 överblivna skor.

leftShoes = int(input("Hur många vänsterskor finns det? "))
rightShoes = int(input("Hur många högerskor finns det? "))
pairShoes = min(leftShoes, rightShoes)
neglectedShoes = max(leftShoes, rightShoes) - min(leftShoes, rightShoes)

print(f'Det finns {pairShoes} par och {neglectedShoes} överblivna skor.')
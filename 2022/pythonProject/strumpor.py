# Hur många strumpor finns det i tvättmaskinen? 19
# Det finns 9 par och 1 överbliven strumpa.

antalStrumpor = int(input("Hur många strumpor finns det i tvättmaskinen? "))
antalPar = antalStrumpor // 2
antalÖ9verblivna = antalStrumpor % 2
print(f'Det finns {antalPar} par och {antalÖverblivna} överbliven strumpa.')
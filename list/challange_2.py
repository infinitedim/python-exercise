numbers = [2,7,7,10,4,2,5,7,6,4,10,6,5]
uniques = []

for number in numbers:
  if number not in uniques:
    uniques.append(number)
    uniques.sort()
print(uniques)
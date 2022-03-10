phone_numbers = input("Your Phone Number: ")

numbers = {
  "0": "Zero",
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine"
}

output = ""
for ch in phone_numbers:
  output += numbers.get(ch, "!") + " "
print(output)
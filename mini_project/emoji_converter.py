message = input(">")
words = message.split(' ')

emojis = {
  ":-D": "😁",
  ":(": "☹️",
  ":|": "😐",
  ":/": "😕",
  "<3": "❤️",
  "<3_black": "🖤"
}

output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)
def emoji_converter(messege):
  words = messege.split(' ')
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
  return output


messege = input(">")
print(emoji_converter(messege))
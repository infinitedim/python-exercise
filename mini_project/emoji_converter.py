def emoji_converter(messege):
  words = messege.split(' ')
  emojis = {
  ":-D": "đ",
  ":(": "âšī¸",
  ":|": "đ",
  ":/": "đ",
  "<3": "â¤ī¸",
  "<3_black": "đ¤"
  }

  output = ""
  for word in words:
    output += emojis.get(word, word) + " "
  return output


messege = input(">")
print(emoji_converter(messege))
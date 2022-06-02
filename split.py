message = input('> ')
words = message.split(' ')

emojis = {
    ":)": "ahaha",
    ":(": "nuuu"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

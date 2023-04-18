sentense = input()
words = dict()
for word in sentense.split(" "):
  words[len(word)] = word

biggest_word = max(words)
print(biggest_word)
sentence = input("so'z kiritiing: ")
words = sentence.split()

for i in range(len(words)):
    if len(words[i]) % 2 != 0:
        words[i] = words[i][::-1]

result = ' '.join(words)
print(result)

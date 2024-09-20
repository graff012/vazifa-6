sentence = input("matn kiriting: ").lower()

words = sentence.split()

sorted_words = sorted(words)

sorted_sentence = ' '.join(sorted_words)

print(sorted_sentence)

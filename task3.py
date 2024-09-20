list1 = ['salom',123,True,'Hayr','world',3.14,'7214']

text = sorted([item for item in list1 if isinstance(item, str)])

other = sorted([item for item in list1 if item not in text], reverse=True)

print(text)
print(other)
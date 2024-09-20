data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_data = [t[:-1] + (100,) for t in data]

print(new_data)

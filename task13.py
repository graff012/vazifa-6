data = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]

new_data = [t for t in data if t]

print(new_data)

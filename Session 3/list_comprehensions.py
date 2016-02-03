array = [1, 2, 3]

result = []
for item in array:
	result.append(item * 2)

result = [item * 2 for item in array]
result = [item * 2 for item in array if item % 2]

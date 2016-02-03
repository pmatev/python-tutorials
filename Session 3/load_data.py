import csv

data = []
with open('../data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		data.append(row)


data.append(['x', 'y', 'z'])
print(data)

with open('data2.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	for row in data:
		writer.writerow(row)


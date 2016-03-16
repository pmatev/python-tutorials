import ipdb

def main():
	print(1)
	print(2)
	x = 10
	ipdb.set_trace()
	x += 10
	x += 10

if __name__ == '__main__':
	main()

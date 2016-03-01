
def blah():
	raise Exception()

try:
	blah()
	print('wont print')
except:
	# do somehting



class EvenNumberException(Exception):
	pass

try:
	raise Exception()
except EvenNumberException as err:
	pass
except OddNumberException as err:
	pass
finally:
	pass

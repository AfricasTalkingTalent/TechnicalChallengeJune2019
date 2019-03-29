#define a method finddocs that reads and applies the lambda function to each value in the list.

def finddocs(wfiles):
	return list(filter(lambda x:'a' in open(x, 'r').read(), wfiles))

print(finddocs(['README.md']))

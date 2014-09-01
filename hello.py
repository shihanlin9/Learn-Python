# 2014-9-1

#print 'hello world'

#name = raw_input('Please input your name: ')
#print 'Hello, ', name
#i = 0
arr = []
#arr.insert(-1, 'a')
#arr.insert(-1, 'b')
#arr.insert(-1, 'c')
#arr.insert(-1, 'd')

arr.insert(0, 'a')
arr.insert(0, 'b')
arr.insert(0, 'c')
arr.insert(0, 'd')

#arr.append('a')
#arr.append('b')
#arr.append('c')
#arr.append('d')

#print(len(arr))
for i in arr:
	print(i)
for i in range(len(arr)):
	arr.pop(0)

score = {'Peter':100, 'Mary':50}
#print(score['Peter'])
print(score.get('Petera', 1))


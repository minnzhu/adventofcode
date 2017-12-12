f = open('input11.txt')

dic = {}
for line in f:
	line = line.strip('\n')
	m,n = line.split(' <-> ')
	n = n.split(', ')
	dic[m] = n
	print (type(m),type(n))

while dic:
	L = []
	for j in dic.keys():
		tot = set(dic[j])
		l = len(tot)
		c = 0 
		while l != c:
			for i in dic.keys():
				if i in tot:
					for j in dic[i]:
						tot.add(j)
			c = l
			l = len(tot)
		L.extend(tot)
		li = list(tot)
		for i in li:
			del dic[i]

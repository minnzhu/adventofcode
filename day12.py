f = open('input11.txt')

dic = {}
for line in f:
	line = line.strip('\n')
	m,n = line.split(' <-> ')
	n = n.split(', ')
	dic[m] = n

count = 0
lis = list(dic.keys())
while lis:
	L = []
	LL = []
	for j in lis:
		if j in LL:
			pass
		else:
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
			LL.append(tot)
			li = list(tot)
			count += 1
			for i in li:
				del lis[lis.index(i)

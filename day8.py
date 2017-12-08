f = open('or.txt')
reg = {}
maxi = 0
for l in f:
	l = l.strip('\n')
	l = l.split(' ')
	if l[0] not in reg.keys():
		reg[l[0]] = 0
	if l[4] not in reg.keys():
		reg[l[4]] = 0
	stp = 'reg[l[4]]'
	st = ' '.join(l[5:])
	st = stp+' '+st
	if eval(st):
		if l[1] == 'dec':
			reg[l[0]] -= int(l[2])
		else:
			reg[l[0]] += int(l[2])
	if max(reg.values()) > maxi:
		maxi = max(reg.values())
print(max(reg.values()))
print(maxi)
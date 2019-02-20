
def g(a,b):
	k=0
	o=''
	p=0
	q=0
	for i in range(len(a)):
		if len(a)<len(b):
			if a[i]==b[i]:
				o+=a[i]
				k=k+1
		else :
			q=1
			break
	i=0
	if q==1:
		while(True):
			if a[i]==b[i]:
				o+=a[i]
			else :
				o+=b[i]
				p=p+1
			if i==3:
				break
			i=i+1
		return p

	for i in range(k,len(b)):
		o+=b[i]
		p=p+1
	return p
 
 def main():
	a=input()
	b=input()
	print(g(a,b))
try:
 	 main()
expept:
 	 print('invalid')

n = 4
x = [0 for i in range(n+1)]
mark = [False for v in range(n+1)]

def check(v,k):
	return mark[v] == False

def solution():
	print(x[1:])
	
def Try(k):
	for v in range(1,n+1):
		if check(v,k):
			x[k] = v
			mark[v] = True
			if k == n:
				solution()
			else:
				Try(k+1)
			mark[v] = False
			
Try(1)	

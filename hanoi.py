n = 4
array = [ [i for i in xrange(1, n+1)], [0 for i in xrange(n)], [0 for i in xrange(n)] ]
disque = [ "" for i in xrange(n+1) ]

def initialize():
	for i in xrange(n+1):
		disque[i] += " " * (n+2-i)
		disque[i] += "_" * i
		disque[i] += "|"
		disque[i] += "_" * i
		disque[i] += " " * (n+2-i)

"""	while (1):
		display()
	 	start = int(raw_input("From: "))
	 	end = int(raw_input("To: "))
	 	if licit(start, end):
			move(start, end)"""

def licit(start, end):
	return True

def move(start, end):
	depth_start = 0
	while depth_start < n and array[start][depth_start]==0:
		depth_start += 1

	depth_end = 0
	while depth_end < n and array[end][depth_end]==0:
		depth_end+=1
	depth_end-=1

	array[end][depth_end] = array[start][depth_start]
	array[start][depth_start] = 0
	display()

def other(n1, n2):
	if n1==0:
		if n2==1:
			return 2
		elif n2==2:
			return 1
	elif n1==1:
		if n2==0:
			return 2
		elif n2==2:
			return 0
	elif n1==2:
		if n2==0:
			return 1
		elif n2==1:
			return 0

def demo(n, start, end, inter):
	if n==1:
		move(start, end)
		return
	demo(n-1, start, inter, other(start, inter))
	move(start, end)
	demo(n-1, inter, end, other(end, inter))
		
def single_line(i):
	column1 = disque[array[0][i]]
	column2 = disque[array[1][i]]
	column3 = disque[array[2][i]]
	print column1, column2, column3

def display():
	for i in xrange(n):
		single_line(i)
	print disque[0]

initialize()
demo(n, 0, 2, 1)

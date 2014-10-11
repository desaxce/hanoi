n = 3
array = [ [i for i in xrange(1, n+1)], [0 for i in xrange(n)], [0 for i in xrange(n)] ]
empty = "     |     "
disk1 = "    _|_    "
disk2 = "   __|__   "
disk3 = "  ___|___  "

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
		

def main():
	demo(n, 0, 2, 1)
"""	while (1):
		display()
	 	start = int(raw_input("From: "))
	 	end = int(raw_input("To: "))
	 	if licit(start, end):
			move(start, end)"""

def disk(i):
	if i==1:
		return disk1
	if i==2:
		return disk2
	if i==3:
		return disk3
	return empty

def single_line(i):
	column1 = disk(array[0][i])
	column2 = disk(array[1][i])
	column3 = disk(array[2][i])
	print column1, column2, column3

def display():
	for i in xrange(3):
		single_line(i)
	bottom_line()


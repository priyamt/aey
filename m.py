def fib(n)
    if n<2: return n
    else:
	if a[n]!=0:
		a[n]=fib(n-1) +fib(n-2)
        else:
		return a[n]
a=[0]*50
print fib(40)











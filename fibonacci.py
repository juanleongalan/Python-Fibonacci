def fib(n):
	"""Escribe la serie de Fibonacci hasta n."""
	a, b = 0, 1
	while a < n:
		print (a, end=' ')
		a, b = b, a+b
	print()
	
	#Ahora se llama a la funcion que acabamos de definir
	     
fib(2000)

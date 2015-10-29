def add_2(x,y, mult_by = 1):
	return mult_by * (x + y)
	
def optional_args_test(a,b, *rest):
	print("A: " + str(a))
	print("B: " + str(b))
	print("Rest: " + str(rest))
	
	
def my_filter_1(criteria_f, elements):
	return [x for x in elements if criteria_f(x)] #list comprehension (like a for loop)

def my_filter_2(criteria_f, elements):
	combiner = lambda elts, elt: elts + [elt] if criteria_f(elt) else elts	
	return reduce(combiner, [[]] + elements)
	
	
	
#recursion: so that you don't have to use a loop
#SumRange(1,5)= 1 + 2 + 3 + 4 + 5 = 15
#SR(1,3) = 1 + 2 + 3
#SR(1,2) = 1 +2

#SR(Begin, End) = Begin if Begin==End
#SR(Begin, End-1) + End

def sum_range(begin, end):
	if begin == end:
		return begin
	else: 
		return sum_range(begin, end -1) + end
		
		
def factorial(n):
	if n == 0:
		return 1
	else:
		return factorial (n-1) * n
		
def rev(list):
	x = list[len(list)]
	y = list[len(list) - 1]
	z = list[len(list) - 2]
	new_list = [x,y,z]
	return new_list
	
def rev(list):
	new_list[0] = list(len(list))
	new_list[1] = list(len(list) -1 )
	new_list[2] = list(len(list) -2 )
	new_list[3] = list(len(list) -3 )
	return new_list


# rev([]) = []
# rev([A,B,C,D,....,Z]) = [Z] + rev([A,B,C,...,Y])
#recursively defined list reversal	
def rev(list):
	if len(list) <= 1:
		return list
	else:
		return [list[len(list) -1]] + rev(list[:len(list) -1])
		
#Towers of hanoi solver		
def hanoi (n, start, other, end):
	if n == 1:
		print("Move disk from " + str(start) + " to " + str(end))
	else:
		hanoi(n-1, start, end, other)
		print("Move disk from " + str(start) + " to " + str(end))
		hanoi(n-1, other, start, end)
		
		#2,3,5,8,13,21
		#2,      3,    6(index of list)
def fib(first, second, n, cache = {}):
	if n==1:
		return first
	elif n==2:
		return second
	if not (cache.has_key(n)):
		cache[n] = fib(first,second,n-1, cache) + fib(first,second,n-2, cache)
	return cache[n]
	
	#return fib(second, first+second, n-1)
	#return fib(first,second,n-1) + fib(first,second,n-2)
	
		
#Cartesian product	
#A = {a,b,c}
#B = {d,e,f}
#A x B = {(a,d), (a,e), {a,f), (b,d), (b,e), (b,f), (c,d), (c,e), (c,f)}

#cart_prod for 2
def CP (a,b):
	pairs = []
	for i in a:
		for j in b:
			pairs.append((i,j))
	return pairs		
			
#cart prod for 3
def CP (a,b,c):
	pairs = []
	for i in a:
		for j in b:
			for k in c:
				pairs.append((i,j,k))
	return pairs		

#cart prod any number of sets	
def cart_prod(*sets):
	if len(sets) == 0:
		return []
	if len(sets) == 1:
		return map(lambda x: [x], sets[0])
	rest = cart_prod(*sets[1:])
	add_front = lambda x: map(lambda y: [x] + y, rest)
	return reduce(lambda x, y: x+y, map(add_front, sets[0]))


#given n objects, how many combinations are there if you choose k at a time
#(n)
#(k)
#All_combs([1,2,3,4,5,6],3)

#Get all combinations from items, taken k at a time.
def all_combs(items, k):
		if k == len(items):
			return [items]
		if k == 1:
			return map(lambda X: [X], items)
		rest = all_combs(items[1:],k-1)
		return map(lambda x: [items[0]] + x, rest) + all_combs(items[1:],k)
	
	
	
	
	
	
	





	
	

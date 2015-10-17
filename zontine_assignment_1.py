#Hannah Zontine
#Assignment 1

def flatten(list):
	if list == []:
		return list
	if type(list[0]) != type([]):
		return [list[0]] + flatten(list[1:])
	else:
		return flatten(list[0]) + flatten(list[1:])
		
def powerset(elems):
	if elems == []:
		return elems
	else:
		rest = powerset(elems[1:])
		return map(lambda x: (([elems[0]] + x), rest), + rest)
		
def il(x, elems):
	l = []
	nperms= list(elems)
	for i in len(elems):
		for j in len(elems):
			if (j == i):
				nperms = nperms.append(x)
	return nperms	
				
def all_perms(list):
	if list == [[]]:
		return list
	else:
		rest = all_perms(list[1:])
		first_added = map(lambda x: il(elms[0], x), rest)
		return reduce(lambda x, y: x+y, first_added)
		
def spiral(n, end_corner):
	curr_num = n**2 -1
	dist_to_go = n
	steps_walked = 0
	if (end_corner == 1):
		curr_pos = (0,0)
		direction = [(1, 0),(0,1),(-1,0), (0,-1)]
	else:
		if (end_corner == 2):
			curr_pos = (0,n-1)
			direction = [(0,-1),(1,0),(0,1), (-1,0)]
		else:
			if (end_corner == 3):
				curr_pos = (n-1,0)
				direction = [(0,1),(-1,0),(0,-1), (1,0)]
			else:
				if (end_corner == 4):
					curr_pos = (n-1,n-1)
					direction = [(-1,0),(0,-1),(1,0), (0,1)]
				else:
					print ("You can't do a spiral with an end corner that equal to 0 or is greater than 4.")

	spiral_array = [[0 for x in range(n)] for x in range(n)] 
	spiral_array[curr_pos].append(curr_num)
	direction_headed = direction[1]
	directions_changed = 0
	while (curr_num >= 0):
		curr_pos = curr_pos[0] + direction_headed #no
		steps_walked = steps_walked + 1
		curr_num = curr_num - 1
		dist_to_go = n-1
		if (dist_to_go == 0):
			direction_headed = direction_headed + 1
			directions_changed = directions_changed + 1
			if (directions_changed == 3):
				direction_headed = direction[1]	
	for row in array:
		print row

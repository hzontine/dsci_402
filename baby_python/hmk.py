def histogram(elements):
	printed = []
	for i in elements:
		value= elements.count(i)
		if (i not in printed):
			printed= printed + i
			print(i+ ": " + value)

			
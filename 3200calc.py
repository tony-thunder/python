for x in range(0, 7):
	for y in range(0, 10):
		for z in range(0, 19):
			a = 411 * x + 295 * y + 161 * z
			if a == 3200:
				print "%a %a %a" (x, y, z)
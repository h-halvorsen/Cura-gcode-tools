#Checks last G0/G1 command that effects extruder. outputs expected filament use in cm

import sys

l_total = 0.0

def findLength(path):
	global l_total

	if path[0] == '\"' or path[0] == '\'':
		path = path[1:-1]
	f_name = path[::-1]
	idx = f_name.index("\\")
	f_name = f_name[:idx]
	f_name = f_name[::-1]
	print(f_name)
	
	with open(path) as file:
		val = 0.0
		for line in reversed(file.readlines()):
			if "G0" in line or "G1" in line:
				if "E" in line:
					idx = line.index('E')
					substr = line[idx+1:]
					try:
						tmp = float(substr)
					except:
						continue
					
					if tmp > val:
						val = tmp

		l_total += val

		val = val/10
		val = round(val, 3)
		
		print("Filament length: {}cm".format(val))

if len(sys.argv) < 2:
	findLength(input("File path: "))
else:
	for i in range(1, len(sys.argv)):
		findLength(sys.argv[i])
		print()	
	total = round((l_total/10),3)
	print("Total: {}cm".format(total))



input()

#Checks last G0/G1 command that effects extruder. outputs expected filament use in cm

import sys

l_total = 0.0

def filenameFromPath(path):
	if (path[0] == '&'):
		path= path[2:-1]
	if (path[0] == '\"' or path[0] == '\''):
		path = path[1:-1]
	f_name = path[::-1]
	idx = f_name.index("\\")
	f_name = f_name[:idx]
	f_name = f_name[::-1]
	print(f_name)

def findLength(path):
	with open(path) as file:
		val = 0.0
		length = 0.0
		m107Occ = False
		for line in file:
			line = line.strip()
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
			if "G92 E0" in line:
				length += val
			if "M107" in line:
				if m107Occ == True:
					length +=val
					break
				m107Occ = True
				
		
		length_raw = length
		length = length/10
		length = round(length, 3)
	return("Filament length: {}cm".format(length), length_raw)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		path = input("File path: ")
		filenameFromPath(path)
		out, length = findLength(path)
		print(out)
	else:
		for i in range(1, len(sys.argv)):
			path = sys.argv[i]
			filenameFromPath(path)
			out, length = findLength(path)
			l_total += length
			print(out)
			print()	
		total = round((l_total/10),3)
		print("Total: {}cm".format(total))
	input()

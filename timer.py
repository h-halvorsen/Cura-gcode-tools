#Get last instance of ";TIME_ELAPSED:" from file, converts it from seconds to hh:mm:ss time format.  If multiple files are analyzed at the same time, it will add together the times and display a total print time

import sys

word = ';TIME_ELAPSED:'

s_total = 0.0

def sec_to_hhmmss(val):
	hh = val/3600 - ((val/3600)%1)
	mm = (val/60)-((val/60)%1) - (hh*60)
	ss = val - mm*60 - hh * 3600

	hh = int(hh)
	mm = int(mm)
	ss = int(ss)

	out = "{}h {}m {}s".format(hh,mm,ss)

	return out

def findTime(path):
	global s_total
	
	if path[0] == '\"' or path[0] == '\'':
		path = path[1:-1]
	f_name = path[::-1]
	idx = f_name.index("\\")
	f_name = f_name[:idx]
	f_name = f_name[::-1]
	print(f_name)

	with open(path) as file:
		for line in reversed(file.readlines()):
			if word in line:
				idx = line.index(':')
				substr = line[idx+1:-1]

				val = float(substr)
				s_total += val
				val = round(val, 2)

				return(sec_to_hhmmss(val), val)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		out, length = findTime(input("File path: "))
		print(out)
	else:
		for i in range(1, len(sys.argv)):
			out, length = findTime(sys.argv[i])
			print(out)
			print()			#separator line
		total = sec_to_hhmmss(s_total)
		print("Total: {}".format(total))
	input()

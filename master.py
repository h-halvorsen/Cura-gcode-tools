# Temporary solution for combined file, will make a "real" master file when all tools are done
import timer as tm, length as lgt, sys

length_total = 0
time_total = 0

def getData(path):
	global length_total
	global time_total

	if path[0] == '\"' or path[0] == '\'':
		path = path[1:-1]
	f_name = path[::-1]
	idx = f_name.index("\\")
	f_name = f_name[:idx]
	f_name = f_name[::-1]
	print(f_name)

	timer_output, time = tm.findTime(path)
	length_output, length = lgt.findLength(path)

	time_total += time
	length_total += length

	print(timer_output)
	print(length_output)

	



if __name__ == "__main":
	if len(sys.argv) < 2:
			getData(input("File path: "))
	else:
		for i in range(1, len(sys.argv)):
			getData(sys.argv[i])
			print()
		print("Total time: {}".format(time_total))
		print("Total length: {}".format(length_total))
	input()


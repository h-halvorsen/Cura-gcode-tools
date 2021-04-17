# Temporary solution for combined file, will make a "real" master file when all tools are done
import timer as tm, length as lgt, sys

length_total = 0
time_total = 0

def getData(path):
	tm.filenameFromPath(path)

	global length_total
	global time_total

	timer_output, time = tm.findTime(path)
	length_output, length = lgt.findLength(path)

	time_total += time
	length_total += length

	print(timer_output)
	print(length_output)

if __name__ == "__main__":

	if len(sys.argv) < 2:
		getData(input("File path: "))
	else:
		for i in range(1, len(sys.argv)):
			getData(sys.argv[i])
			print()
		length_total = length_total/1000
		length_total= round(length_total, 2)
		print("Total time: {}".format(tm.sec_to_hhmmss(time_total)))
		print("Total length: {}m".format(length_total))
	input()


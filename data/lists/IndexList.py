#create and fill path list
def movements():
	path = ["Move forward", 10, "Move backward", 5, "Move left", 3, "Move right", 1]
	return path

#print path
def run():
	print("Moving...")
	print("{0} for {1} steps\n{2} for {3} steps\n{4} for {5} steps\n{6} for {7} steps".format(*movements()))

run()
def directions():
	directions = ["Move forward", "Move backward", "Turn left", "Turn right"]
	return directions

def menu():
	print("Please select a direction:")
	direction = directions()
	for x in range(len(direction)):
		print("{index}: {facing}".format(index = x, facing = direction[x]))

def run():
	menu()

run()
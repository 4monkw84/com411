def directions():
	directions = ["Move forward", "Move backward", "Turn left", "Turn right"]
	return directions

def menu():
	print("Please select a direction:")
	direction = directions()
	for x in range(len(direction)):
		print("{index}: {facing}".format(index = x, facing = direction[x]))
	usrInput = input()
	print("{index}: {facing}".format(index = usrInput, facing = direction[int(usrInput)]))
	return direction[int(usrInput)]

def run():
	route = []
	print("Working out an escape route...")
	for x in range(5):
		route.append(menu())
	print(route)

run()
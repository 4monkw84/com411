def directions():
	directions = ["Move forward", "Move backward", "Turn left", "Turn right"]
	return directions

def menu():
	print("Please select a direction:")
	#store directions as local var
	direction = directions()
	#iterate through directions
	for x in range(len(direction)):
		#print directions and indicies
		print("{index}: {facing}".format(index = x, facing = direction[x]))
	#get user input
	usrInput = input()
	#display user choice
	print("{index}: {facing}".format(index = usrInput, facing = direction[int(usrInput)]))
	#return user choice
	return direction[int(usrInput)]

def run():
	route = []
	print("Working out an escape route...")
	for x in range(5):
		#get and store user input into route list 5 times
		route.append(menu())
	#print list contents
	print("Escape route: ", route)

run()
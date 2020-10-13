print("Program Started!\nPlease enter a letter: ");
character = input();
if(len(character) == 1):
  print("The ASCII code for " + character + " is: ", ord(character));
else:
  print("Invalid length");
print("Program Ended!");
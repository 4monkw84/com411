print("Program Started!\nPlease enter an ASCII code: ");
asciiValue = input();
character = abs(int(asciiValue));
if(character in range(32, 126)):
  print("The character represented by the ASCII code", asciiValue, "is", chr(character));
else:
  print("Invalid value")
print("Program Ended!")
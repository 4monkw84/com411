def identify():
  if(seenObj == "a large boulder"):
    print("It's time to run!");
  else:
    print("We will be fine");

print("What lies before us?");
seenObj = input();
identify();
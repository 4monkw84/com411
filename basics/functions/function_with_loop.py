def cross_bridge(steps):
  for x in range(steps):
    print("Crossed step.");
    if(x >= 5):
      print("The bridge is collapsing!");
      break;
    elif(x == steps):
      print("We must keep going!");


cross_bridge(3);
print("\n\n\n")
cross_bridge(6);
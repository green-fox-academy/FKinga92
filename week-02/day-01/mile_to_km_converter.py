# Write a program that asks for an integer that is a distance in kilometers,
# then it converts that value to miles and prints it

distance = input("Please enter an integer! ")
distanceInMiles = float(distance) * 0.621371192
if int(distance) <= 1:
  print(str(distance) + " km is equal to " + str(distanceInMiles) + " miles.")
else:
  print(str(distance) + " kilometers are equal to " + str(distanceInMiles) + " miles.")
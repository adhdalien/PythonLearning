f = 57

print(float(f))

b = 125.0
c = 390.8

print(int(b))
print(int(c))

# When converting floats to integers with the int() function, 
# Python cuts off the decimal and remaining numbers of a float to create an integer.
# Even though we may want to round 390.8 up to 391, Python will not do this through the int() function.

a = 5 / 2
print(a)

user = "Sammy"
lines = 50

# The following line errors out because you can't concatenate strings and ints by themselves
# print("Congratulations, " + user + "! You just wrote " + lines + " lines of code.")
# You first have to convert the lines variable into a string
print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code.")

# We can test to make sure it’s right by concatenating with a string:
f = 5524.53
print("Sammy has " + str(f) + " points.")

# Converting strings to integers
lines_yesterday = "50"
lines_today = "108"

lines_more = int(lines_today) - int(lines_yesterday)
print(lines_more)

# Converting strings to floats
total_points = "5524.53"
new_points = "45.30"

new_total_points = total_points + new_points
print(new_total_points)

new_total_points = float(total_points) + float(new_points)
print(new_total_points)

# Converting between lists and tuples
print(tuple(['pull request', 'open source', 'repository', 'branch']))

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp']
print(tuple(sea_creatures))

# Converting a string into a tuple of characters
print(tuple('Sammy'))

# Converting to lists
coral = ('blue coral', 'staghorn coral', 'pillar coral')
list(coral)

# Strings can be converted to lists as well
print(list('shark'))
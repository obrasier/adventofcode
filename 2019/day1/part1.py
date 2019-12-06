
#masses = [14, 1969, 10756, 100756]
modules = [int(line.rstrip('\n')) for line in open('input.txt')]

total_fuel = 0
for mass in modules:
  fuel = mass//3 - 2
  total_fuel += fuel
print(total_fuel)

#print(total_fuel)

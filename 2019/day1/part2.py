
#masses = [14, 1969, 10756, 100756]
masses = [int(line.rstrip('\n')) for line in open('input.txt')]

total_fuel = 0
for module in masses:
  module_fuel = 0
  fuel = module//3 - 2
  while fuel > 0:
    module_fuel += fuel
    fuel = fuel//3 - 2
  total_fuel += module_fuel
print(total_fuel)

#print(total_fuel)

with open('input.txt') as f:
  memory = f.read().replace('\n', '').split(',')
memory = [int(i) for i in memory]
memory[1] = 12
memory[2] = 2

p1 = [1,0,0,0,99]
p2 = [2,3,0,3,99]
p3 = [2,4,4,5,99,0]
p4 = [1,1,1,4,99,5,6,0,99]

for i in range(0, len(memory), 4):
  operation = memory[i]
  if operation == 1:
    memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
  elif operation == 2:
    memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
  elif operation == 99:
    break
  else:
    raise EnvironmentError
print(memory[0])
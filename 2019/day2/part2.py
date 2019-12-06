import sys
for noun in range(100):
  for verb in range(100):
    with open('input.txt') as f:
      memory = f.read().replace('\n', '').split(',')
    memory = [int(i) for i in memory]
    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory), 4):
      operation = memory[i]
      if operation == 1:
        memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
      elif operation == 2:
        memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
      elif operation == 99:
        break
      else:
        print('Something went wrong...')
        sys.exit(0)
    if memory[0] == 19690720:
      print(100 * noun + verb)
      sys.exit(0)
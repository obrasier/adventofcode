from collections import defaultdict

def add_wire_to_grid(grid, turns, wire):
  x = 0
  y = 0
  steps = 0
  for turn in turns:
    direction = turn[0]
    distance = int(turn[1:])
    for _ in range(distance):
      steps += 1
      if direction == 'R':
        x += 1
      elif direction == 'U':
        y += 1
      elif direction == 'L':
        x -= 1
      elif direction == 'D':
        y -= 1
      if (x, y) in grid.keys() and grid[(x,y)][0] == wire:
        continue
      grid[(x, y)].append((wire, steps))
  return grid

def wire_distance(point):
  values = point[1]
  return values[0][1] + values[1][1]

inputs = [line.rstrip('\n') for line in open('input.txt')]

one = inputs[0].split(',')
two = inputs[1].split(',')

# test
#one = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
#two = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
grid = defaultdict(list)

grid = add_wire_to_grid(grid, one, '1')
grid = add_wire_to_grid(grid, two, '2')

intersections = [(coord, value) for coord, value in grid.items() if len(value) == 2 and value[0][0] != value[1][0]]
#print(intersections)
min_point = min(intersections, key=wire_distance)
print(wire_distance(min_point))

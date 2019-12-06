from collections import defaultdict

def add_wire_to_grid(grid, turns, wire):
  x = 0
  y = 0
  for turn in turns:
    direction = turn[0]
    distance = int(turn[1:])
    for _ in range(distance):
      if direction == 'R':
        x += 1
      elif direction == 'U':
        y += 1
      elif direction == 'L':
        x -= 1
      elif direction == 'D':
        y -= 1
      grid[(x, y)].add(wire)
  return grid

def manhattan_distance(coord):
  return abs(coord[0]) + abs(coord[1])

inputs = [line.rstrip('\n') for line in open('input.txt')]

one = inputs[0].split(',')
two = inputs[1].split(',')
grid = defaultdict(set)

grid = add_wire_to_grid(grid, one, '1')
grid = add_wire_to_grid(grid, two, '2')

intersections = [coord for coord, value in grid.items() if len(value) == 2]
min_point = min(intersections, key=manhattan_distance)
print(manhattan_distance(min_point))

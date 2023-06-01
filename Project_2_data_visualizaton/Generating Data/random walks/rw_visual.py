import matplotlib.pyplot as plt

from random_walk import RandomWalk

# KEEP MAKING NEW WALKS WHEN PROGRAM IS ACTIVE
while True:

  #MAKE A RANDOM WALK
  rw = RandomWalk(50_000)
  rw.fill_walk()

  #PLOT THE POINTS IN THE WALK
  plt.style.use('classic')
  fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

  # EMPHASIZE THE FIRST AND LAST VALUE
  ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors  = 'none', s = 100)

  # REMOVE THE AXES 
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)

  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break
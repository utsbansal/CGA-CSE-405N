#importing necessary libraries
import matplotlib.pyplot as plt
#defining DDA function
def DDA(x1, y1, x2, y2):
  #Calculating change in both directions
  dx = x2-x1
  dy = y2-y1
  x_point = [x1]
  y_point = [y1]
  steps = 0
  #Deciding the number of steps to move
  if abs(dx)>abs(dy):
    steps = abs(dx)
  else:
    steps = abs(dy)
  #Calculating the amount of change per step in both directions
  xinc = dx/steps
  yinc = dy/steps
  for i in range(0, steps):
    #Calculating the new points and rounding them off
    x_point.append(x_point[-1]+xinc)
    y_point.append(y_point[-1]+yinc)
    x_point[-2] = round(x_point[-2])
    y_point[-2] = round(y_point[-2])
  #Rounding off the last found points
  x_point[-1] = round(x_point[-1])
  y_point[-1] = round(y_point[-1])
  #Plotting the calculated points and labelling the axis
  plt.plot(x_point, y_point, "ko-")
  plt.title("DDA Line from ("+str(x_point[0])+", "+str(y_point[0])+") to ("+str(x_point[-1])+", "+str(y_point[-1])+")")
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
  plt.show()
DDA(20, 18, 30, 10)

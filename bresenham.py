#Importing required library
import matplotlib.pyplot as plt
#Bresenham Function
def Bresenham(x1, y1, x2, y2):
  #initializing required variables
  x = 0
  y = 0
  x_points = []
  y_points = []
  #Calculating variables which won't change their values throughout execution
  dx = abs(x2-x1)
  dy = abs(y2-y1)
  twodx = 2*dx
  twody = 2*dy
  #Making sure slope is not 0
  if x2-x1 != 0:
    slope = (y2-y1)/(x2-x1)
    #Working for slope between -1 and 1
    if slope>=-1 and slope<=1:
      #Finding the left point
      if x2>x1:
        x = x1
        y = y1
      else:
        x = x2
        y = y2
      x_points.append(x)
      y_points.append(y)
      #Initial decision parameter
      p = twody - dx
      #Finding next points according to the algorithm
      for k in range(0, dx):
        if p<0:
          p = p + twody
          x_points.append(x_points[-1]+1)
          y_points.append(y_points[-1])
        else:
          p = p + twody - twodx
          x_points.append(x_points[-1]+1)
          if slope>=0:
            y_points.append(y_points[-1]+1)
          else:
            y_points.append(y_points[-1]-1)
    else:
      #For slope <-1 and slope>1 but slope != infinity
      if y2>y1:
        x = x1
        y = y1
      else:
        x = x2
        y = y2
      x_points.append(x)
      y_points.append(y)
      #Initial decision parameter
      p = twodx - dy
      #Finding next points according to the algorithm
      for k in range(0, dy):
        if p<0:
          p = p + twodx
          x_points.append(x_points[-1])
          y_points.append(y_points[-1]+1)
        else:
          p = p + twodx - twody
          if slope>1:
            x_points.append(x_points[-1]+1)
          else:
            x_points.append(x_points[-1]-1)
          y_points.append(y_points[-1]+1)
  else:
    #For slope = infinity
    if y2>y1:
      y = y1
      x = x1
    else:
      y = y2
      x = x2
    x_points.append(x)
    y_points.append(y)
    #Only change is the change in y. x remains same
    for k in range(0, dy):
      x_points.append(x_points[-1])
      y_points.append(y_points[-1]+1)
  #Plotting the calculated points
  plt.plot(x_points, y_points, "ko-")
  plt.title("Bresenham Line from ("+str(x_points[0])+", "+str(y_points[0])+") to ("+str(x_points[-1])+", "+str(y_points[-1])+")")
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
  plt.show()
Bresenham(5, 11, 7, 4)

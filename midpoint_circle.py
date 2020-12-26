import matplotlib.pyplot as plt
def plot_symmetric_points(xc, yc, x, y):
  plt.plot(xc+x, yc+y, "ko")
  plt.plot(xc-x, yc+y, "ko")
  plt.plot(xc+x, yc-y, "ko")
  plt.plot(xc-x, yc-y, "ko")
  plt.plot(xc+y, yc+x, "ko")
  plt.plot(xc-y, yc+x, "ko")
  plt.plot(xc+y, yc-x, "ko")
  plt.plot(xc-y, yc-x, "ko")
def midpoint(xc, yc, r):
  x = 0
  y = r
  p = 1 - r
  plot_symmetric_points(xc, yc, x, y)
  while x<y:
    x += 1
    if p<0:
      p = p + 2*x +1
    else:
      y = y-1
      p = p + 2*(x-y) + 1
    plot_symmetric_points(xc, yc, x, y)
  plt.show()  
midpoint(0,0,5)

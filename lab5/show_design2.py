def show_design2(x, y):
    panel = DrawingPanel(x, y)

    dx = x/10
    dy = y/10
  
    for i in range(4):
      panel.draw_rect((i+1)*dx, (i+1)*dy, x-(i+1)*2*dx, y-(i+1)*2*dy)
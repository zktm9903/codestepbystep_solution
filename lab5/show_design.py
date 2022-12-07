def show_design():
    panel = DrawingPanel(200, 200)

    for i in range(20, 100, 20):
      panel.draw_rect(i, i, 200-2*i, 200-2*i)
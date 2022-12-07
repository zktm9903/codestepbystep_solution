def mickey_box():
    panel = DrawingPanel(220, 150)
    panel.set_background("yellow")
    panel.fill_oval(50, 25, 40, 40, "blue")      
    panel.fill_oval(130, 25, 40, 40, "blue")
    panel.fill_rect(70, 45, 80, 80, "red")    
    panel.draw_line(70, 85, 150, 85)
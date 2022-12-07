def main():
    panel = DrawingPanel(450, 150)
    draw_figure(panel, 50, 25)
    draw_figure(panel, 250, 45)

def draw_figure(panel, x, y):
    panel.set_background("yellow")
    
    panel.fill_oval(x, y, 40, 40, "blue")      
    panel.fill_oval(x+80, y, 40, 40, "blue")
    panel.fill_rect(x+20, y+20, 80, 80, "red")    
    panel.draw_line(x+20, y+60, x+100, y+60)

main()
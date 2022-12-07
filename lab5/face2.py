def drawFace(panel, x, y):
    panel.draw_oval(x, y, 100, 100, "black")   # face outline
    panel.fill_oval(x+20, y+30, 20, 20, "blue")      # eyes
    panel.fill_oval(x+60, y+30, 20, 20, "blue")
    panel.draw_line(x+30, y+70, x+70, y+70, "red")     # mouth

def main():
    panel = DrawingPanel(520, 180)
    for i in range(10, 510, 100):
        drawFace(panel,i,30)

main()
def drawFace(panel, x, y):
    panel.draw_oval(x, y, 100, 100, "black")   # face outline
    panel.fill_oval(x+20, y+30, 20, 20, "blue")      # eyes
    panel.fill_oval(x+60, y+30, 20, 20, "blue")
    panel.draw_line(x+30, y+70, x+70, y+70, "red")     # mouth

def main():
    panel = DrawingPanel(320, 180)
    drawFace(panel, 10, 30)
    drawFace(panel, 150, 50)

main()
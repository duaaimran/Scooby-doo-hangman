from graphics import *
from button import Button

def homescreen():
  win1 = GraphWin("Hangman", 550, 390)
  win1.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 40.0), "Webp.net-resizeimage (2).png")
  image0.draw(win1)
  intro1 = Text(Point(50.0, 70.0), "Welcome to Duaa's Hangman!")
  intro1.setSize(16)
  intro1.setTextColor("white")
  intro1.setStyle("bold")
  intro1.draw(win1)
  intro2 = Text(Point(50.0, 60.0), "Click anywhere to play.")
  intro2.setTextColor("white")
  intro2.setStyle("bold")
  intro2.draw(win1)
  image = Image(Point(70.0, 30.0), "Webp.net-resizeimage.png")
  image.draw(win1)
  image1 = Image(Point(15.0, 30.0), "Webp.net-resizeimage (1).png")
  image1.draw(win1)
  win1.getMouse()
  win1.close()

def buttons(win2):
  #First Button
  l1 = Rectangle(Point(5, 60), Point(25, 40))
  l1.setFill('darkblue')
  l1.draw(win2)
  l1c = l1.getCenter()
  lx1 = l1c.getX()
  ly1 = l1c.getY()
  l1t = Text(Point(lx1, ly1), "GHOST")
  l1t.setTextColor('white')
  l1t.draw(win2)
  #Second Button
  l2 = Rectangle(Point(28, 60), Point(48, 40))
  l2.setFill('darkblue')
  l2.draw(win2)
  l2c = l2.getCenter()
  lx2 = l2c.getX()
  ly2 = l2c.getY()
  l2t = Text(Point(lx2, ly2), "WITCH")
  l2t.setTextColor('white')
  l2t.draw(win2)
  #Third Button
  l3 = Rectangle(Point(51, 60), Point(71, 40))
  l3.setFill('darkblue')
  l3.draw(win2)
  l3c = l3.getCenter()
  lx3 = l3c.getX()
  ly3 = l3c.getY()
  l3t = Text(Point(lx3, ly3), "ZOMBIE")
  l3t.setTextColor('white')
  l3t.draw(win2)
  #Fourth Button
  l4 = Rectangle(Point(74, 60), Point(94, 40))
  l4.setFill('darkblue')
  l4.draw(win2)
  l4c = l4.getCenter()
  lx4 = l4c.getX()
  ly4 = l4c.getY()
  l4t = Text(Point(lx4, ly4), "DRACULA")
  l4t.setTextColor('white')
  l4t.draw(win2)
  
def pickLevel():
  win2 = GraphWin("Hangman", 550, 390)
  win2.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 40.0), "Webp.net-resizeimage (2).png")
  image0.draw(win2)
  inst = Text(Point(50.0, 80.0), "Pick a level.")
  inst.setSize(16)
  inst.setTextColor("white")
  inst.setStyle("bold")
  inst.draw(win2)
  image1 = Image(Point(15.0, 2.0), "Webp.net-resizeimage (1).png")
  image1.draw(win2)
  image2 = Image(Point(35.0, 2.0), "Webp.net-resizeimage (3).png")
  image2.draw(win2)
  image3 = Image(Point(50.0, -3.0), "Webp.net-resizeimage (4).png")
  image3.draw(win2)
  image4 = Image(Point(75.0, -1.0), "Webp.net-resizeimage (5).png")
  image4.draw(win2)
  buttons(win2)
  x = True
  file = ""
  while x == True:
    p = win2.getMouse()
    if  5 <= p.getX() <= 25 and 40 <= p.getY() <= 60:
      x = False
      file = "ghost1.txt"
    if  28 <= p.getX() <= 48 and 40 <= p.getY() <= 60:
      x = False
      file = "witch2.txt"
    if  51 <= p.getX() <= 71 and 40 <= p.getY() <= 60:
      x = False
      file = "zombie3.txt"
    if  74 <= p.getX() <= 94 and 40 <= p.getY() <= 60:
      x = False
      file = "dracula4.txt"
  return file

def grid(win):
  l1a = Line(Point(0.0, 0.0), Point(0.0, 100.0)).draw(win)
  l2a = Line(Point(10.0, 0.0), Point(10.0, 100.0)).draw(win)
  l3a = Line(Point(20.0, 0.0), Point(20.0, 100.0)).draw(win)
  l4a = Line(Point(30.0, 0.0), Point(30.0, 100.0)).draw(win)
  l5a = Line(Point(40.0, 0.0), Point(40.0, 100.0)).draw(win)
  l6a = Line(Point(50.0, 0.0), Point(50.0, 100.0)).draw(win)
  l7a = Line(Point(60.0, 0.0), Point(60.0, 100.0)).draw(win)
  l8a = Line(Point(70.0, 0.0), Point(70.0, 100.0)).draw(win)
  l9a = Line(Point(80.0, 0.0), Point(80.0, 100.0)).draw(win)
  l10a = Line(Point(90.0, 0.0), Point(90.0, 100.0)).draw(win)
  l11a = Line(Point(100.0, 0.0)), Point(100.0, 100.0).draw(win)

def keyboard(win):
  a = Button(win, Point(7, 30), 5, 10, 'A')
  a.activate()
  b = Button(win, Point(14, 30), 5, 10, 'B')
  b.activate()
  c = Button(win, Point(21, 30), 5, 10, 'C')
  c.activate()
  d = Button(win, Point(28, 30), 5, 10, 'D')
  d.activate()
  e = Button(win, Point(35, 30), 5, 10, 'E')
  e.activate()
  f = Button(win, Point(42, 30), 5, 10, 'F')
  f.activate()
  g = Button(win, Point(49, 30), 5, 10, 'G')
  g.activate()
  h = Button(win, Point(56, 30), 5, 10, 'H')
  h.activate()
  i = Button(win, Point(63, 30), 5, 10, 'I')
  i.activate()
  j = Button(win, Point(73, 30), 5, 10, 'J')
  j.activate()
  k = Button(win, Point(80, 30), 5, 10, 'K')
  k.activate()
  l = Button(win, Point(87, 30), 5, 10, 'L')
  l.activate()
  m = Button(win, Point(94, 30), 5, 10, 'M')
  m.activate()
  

def ghostgame(file):
  win = GraphWin("Hangman", 550, 390)
  win.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 55.0), "Webp.net-resizeimage (6).png")
  image0.draw(win)
  keyboard(win)

def witchgame(file):
  win = GraphWin("Hangman", 550, 390)
  win.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 40.0), "Webp.net-resizeimage (10).png")
  image0.draw(win)

def zombiegame(file):
  win = GraphWin("Hangman", 550, 390)
  win.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 40.0), "Webp.net-resizeimage (9).png")
  image0.draw(win)

def draculagame(file):
  win = GraphWin("Hangman", 550, 390)
  win.setCoords(0.0, 0.0, 100.0, 100.0)
  image0 = Image(Point(50.0, 40.0), "Webp.net-resizeimage (11).png")
  image0.draw(win)

def main():
  homescreen()
  file = pickLevel()
  print(file)
  if file == "ghost1.txt":
    ghostgame(file)
  if file == "witch2.txt":
    witchgame(file)
  if file == "zombie3.txt":
    zombiegame(file)
  if file == "dracula4.txt":
    draculagame(file)
  
  
main()
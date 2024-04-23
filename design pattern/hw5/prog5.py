class Shape:
    def setLocation(self): pass
    def getLocation(self): pass
    def display(self): pass
    def fill(self): pass
    def setColor(self): pass
    def undisplay(self): pass

# XXCircle class (existing, to be adapted)
class XXCircle:
    def setLocation(self): print("XXCircle setLocation")
    def getLocation(self): print("XXCircle getLocation")
    def displayIt(self): print("XXCircle displayIt")
    def fillIt(self): print("XXCircle fillIt")
    def setItsColor(self): print("XXCircle setItsColor")
    def undisplayIt(self): print("XXCircle undisplayIt")

# CircleAdapter class
class CircleAdapter(Shape):
    def __init__(self, xx_circle):
        self.xx_circle = xx_circle

    def display(self):
        self.xx_circle.displayIt()

    def fill(self):
        self.xx_circle.fillIt()

    def setColor(self):
        self.xx_circle.setItsColor()

    def undisplay(self):
        self.xx_circle.undisplayIt()

def main():
    shapes = [CircleAdapter(XXCircle())] # Add other shapes as needed
    for shape in shapes:
        shape.display()
        shape.fill()
        shape.setColor()
        shape.undisplay()

if __name__ == "__main__":
    main()
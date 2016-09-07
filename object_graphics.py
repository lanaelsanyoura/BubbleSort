
def tub(startButton):
    """
    Draw the tub
    @param str startButton
    @return None
    """
    #tub
    noStroke()
    stroke(0)
    fill(250,250,250)
    rect(100,495, 620, 100, 6, 6, 50, 50)
    stroke(0)
    rect(105,497, 610, 55, 6, 6, 50, 50)
    fill("#E3EAEA")
    rect(105,497, 610, 50, 6, 6, 50, 50)
    
    noFill()
    for i in range(500, 543):
        inter = map(i, 497, 547, 0, 1)
        c = lerpColor(color(250, 250, 250),color(191,193,193), inter)
        stroke(c)
        line(112, i, 707, i)
            
    stroke(0)
    line(115,497,125,547)
    line(705,497,690,547)
    
    fill(250,250,250)
    #SHOWER
    stroke("#ADABAB")
    
    #bottom shower circle
    fill("#B8D6D2")
    noStroke()
    fill("#ADABAB")
    setGradient(105,305, 5, 205, color(173,171,171), color(134,133,133), "Y_AXIS")
    setGradient(105,305, 45, 5, color(173,171,171), color(152,150,150), "X_AXIS")
    noStroke()
    
    #Top grey 
    fill(170,170,170)
    arc(200,312,100,70, -PI, 0, OPEN)
    fill("#B8D6D2")
    ellipse(200,312,100,20)
    fill("#9ABCB7")
    for y in range(3):
        for i in range(-4,5):
            if y == 0:
                ellipse(i*10 + 200, 304 + ( abs(i)**1.5) + y*10 ,5,5)
            elif y== 1:
                ellipse(i*10 + 200, 304 - ( abs(i)**1.5) + y*20 ,5,5)
            else:
                ellipse(i*10 + 200, 315 ,5,5)
                  
    fill("#ADABAB")
    stroke(0)
    fill(43, 149, 201, 100)
    rect(390,558, 70, 30)
    line(394,581,456,581)
    noStroke()
        
def water(waterH):
    """
    Draw the water in the tub
    
    @param int waterH: The height of the water
    @return None
    """
    #WATER
    fill("#2B95C9")
    noStroke()
    rect(107, 500, 715 - 107, 50,6,6,50,50)
    pushMatrix()
    translate(0,waterH) #translationg depends on water level
    fill("#2B95C9")
    rect(105,505, 610, 35, 6, 6, 50, 50)
    stroke(33,139,300)
    stroke("#248BB2")
    #fill("#248BB2")
    for x in range(59):
        for y in range(4):
            ellipse(120 + x*10, 502 + (y* 10), 20, 20)    
            triangle(120+(x*10),502+(y*10), 118+(x*10), 495+(y*10),125+(x*10), 513+(y*10))
    popMatrix()

    
def clouds(x,y, diameter, widths = 5, lengths = 2, transperancy = 100):
    """
    Draw the clouds
    
    @param int x
    @param int y
    @param int diameter
    @param int widths
    @param int lengths
    @param int transperanct
    @return None
    """
    if diameter < 60:
        fill(250,250,250,transperancy)
    else:
        fill(250,250,250,150)
    noStroke()
    #stroke("#C7DFE3")
    for m in range(widths):
        for n in range(lengths):
            ellipse(x + 25*m, y + 25*n, diameter, diameter)
    noStroke()

def pause():
    """
    Draw the pause button
    
    @return None
    """
    fill("#5D5656")
    rect(5, 5, 5,15)
    rect(15, 5, 5,15)
    textSize(20)
    text("PAUSE", 25, 20)

def sun(theme):
    """
    Draw the sun
    
    @param str theme: Theme of the game, either "NOON", "SUNSET", or "SUNRISE"
    @return None
    """
    if theme == "NOON":
        fill(240,132,24, 150)
        ellipse(0,0,150,150)
        fill(247,214,47,90)
        triangle(80,0, 72, 25, 230, 80)
        triangle(70, 30, 60, 55, 220, 120)    
        triangle(52, 54, 35, 75, 210, 160)    
        triangle(25, 75, -5, 75, 160, 200)    
    elif theme == "SUNRISE":
        fill(240,132,24, 150)
        ellipse(400,520,150,150)
    else:
        pass

def setGradient(x, y, w, h, c1, c2, axis):
        """
        From Processing.org examples 
        """
        noFill()
        if axis == "Y_AXIS":  # Top to bottom gradient
            for i in range(y, y + h + 1):
                inter = map(i, y, y + h, 0, 1)
                c = lerpColor(c1, c2, inter)
                stroke(c)
                line(x, i, x + w, i)
        elif axis == "X_AXIS":  # Left to right gradient
            for i in range(x, x + w + 1):
                inter = map(i, x, x + w, 0, 1)
                c = lerpColor(c1, c2, inter)
                stroke(c)
                line(i, y, i, y + h)
                
class TextBox():
    """
    A text box 
    
    === Attributes ===
    @param tuple[int, int, int, int] rect_digits: parameters of the rect 
    @param str rect_stroke: stroke of the rect
    @param tuple[int, int, int, int = 200] rect_fill: Color of the rectangle
    @param str text_box : text in the box
    @param int text_size: size of the text 
    @param bool selected: True iff the text_box is selected
    @param str text_fill: the fill of the text
    """
    def __init__(self, rect_digits, rect_fill, text_fill, text_size, texts, selected, default):
        """
        @param textBox self
        @param tuple[int, int, int, int] rect_digits: parameters of the rect 
        @param str rect_stroke: stroke of the rect
        @param tuple[int, int, int, int = 200] rect_fill: Color of the rectangle
        @param int text_size: size of the text 
        @param str text_fill
        @param str texts
        @param str selected_stroke: stroke for when the box is selected
        @param str default_stroke: stroke for when the box is not selected
        @return None
        """
        self.selected = False
        self.x = rect_digits[0]
        self.y = rect_digits[1]
        self.widths = rect_digits[2]
        self.heights = rect_digits[3]
        self.rect_fill = rect_fill
        self.rect_stroke = default
        self.text_box = texts
        self.text_size = text_size
        self.text_fill = text_fill
        self.selected_stroke = selected
        self.default_stroke = default
        
        
    def draw_box(self):
        """
        Draw the text box
        
        @param TextBox self
        @param str texts: Text written
        """
        
        if len(self.rect_fill) == 3:
            transperancy = 200
        else:
            transperancy = self.rect_fill[3]
        fill(self.rect_fill[0], self.rect_fill[1], self.rect_fill[2], transperancy)
        if self.selected:
            self.rect_stroke = self.selected_stroke
        else:
            self.rect_stroke = self.default_stroke
        stroke(self.rect_stroke)
        rect(self.x, self.y, self.widths, self.heights)

        fill(self.text_fill)
        textSize(self.text_size)
        text(self.text_box, self.x + 5, self.y + 25)
        
    
    
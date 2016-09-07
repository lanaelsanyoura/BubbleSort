"""
Created by Lana El Sanyoura on 9/4/16.
Copyright © 2016 Lana El Sanyoura. All rights reserved.

"""


add_library('sound')

import object_graphics as g
import random


class Player():
    """
    Player object with name and score
    
    === Attributes ===
    @param str name: Name of player 
    @param int score: Player's score
    @param bool game: True iff game hasn't ended yet    
    @param str win: State of winning, either "NO", "YES", or "ULTIMATE"
    @param int lives: Player's current lives     
    @param bool play_again: Whether the player is playing again
    @param bool new_player: True iff this player has never played before
    """
    def __init__(self):
        """
        Create an instance of Player object
        
        @param Player self
        @return: None 
        """
        
        self.name=""
        self.score=0
        self.game=True #game hasn't ended yet    
        self.win="NO"
        self.lives=3    
        self.play_again = False
        self.scores = [] # all the score the player has made
        self.new_player = True
  
class BubbleGame():
    
    """
    Game object
    
    === Attributes ===
    @param Player player: The player of this game 
    @param int mode: screen we are currentlt on
    @param num_to_screen: number to screen 
    @param list[Bubble] emptyBub: list of empty bubbles
    @param int level: current level  
    @param str ans: answer
    @param int numB : number of bubbles drawn
    @param list[Drops] drops
    @param int startButton
    @param list[Button] one: Play
    @param list[Button] two: Instructions
    @param list[Button] three: Mode
    @param list[Button] four: Scores
    @param list[Button] five: Settings 
    @param list[Button] multiplication: List of multiplication table buttons 
    @param Soap soap
    @param Button backB : Back button on instruction screen
    @param Button playB: Play button on instruction screen
    @param Button playA: Game over screen Play Again button
    @param Button scoresW: Winning screen score button
    @param Button scoresA: Game over screen scores button
    @param Button main: Game over screen main menu button
    @param Button mainW: Game over screen main menu button 
    @param Button mainS: Score screen main menu button
    @param Button playS: Score screen play again button
    @param Button on_music: The on music button
    @param Button off_music:  The off music button 
    @param Button noon: Noon button
    @param Button sunset
    @param Button sunrise 
    @param int waterH: water level in g.tub 
    @param bool printing: True iff numbers are printed on screen, False otherwise
    @param Player player: The current player
    @param str name: Inputted name of the player
    @param int mode: The Screen Number
    @param int scoresTranslate: Scrolling of scores on high score screen 
    @param str playerInfo: Information of player
    @param bool paused: Whether the game is paused 
    @param Button main_menu
    @param Button restart
    @param Button mode_restart: The restart button for the mode
    @param Button instr
    @param Button resume
    @param int rounds: The round of the multiplication game
    @param list[int] list_modes: List of modes visited 
    @param str background_theme: Either NOON, SUNSET or NIGHT
    @param str background_colour
    @param Button instruction_pause: Whether the instructions are pressed while game is paused
    @param erase = False
    @param Button yes: Yes button for erasing high scores
    @param Button no: No button for erasing high scores 
    @param did_restart: True iff player has restarted the game
    @param int window_trans: The translation of the scores in the window
    @param TextBox new: textbox for new players
    @param TextBox returning : textbox for returning players
    @param list[list[str name, int score]] infoList: List of scores and names
    @param list[str] filteredList: list of the filtered names 
    """
    
    def __init__(self):
        """
        Create the BubbleGame
        
        @param BubbleGame self
        @return: None
        """
        self.emptyBub = []
        self.colourful = []
        self.infoList = []
        self.filtered_list = []
        self.new = g.TextBox((266,150,310, 35),(43, 149, 201, 100), "#A09999", 20, "Type your name & press ENTER","#26DB48","#3583BC")
        self.returning = g.TextBox((266,290,310, 35),(43, 149, 201, 100), "#A09999", 20, "Type & select your name", "#26DB48","#3583BC")
        self.shirt = shirt #loadShape("clothes.svg")
        self.pants = pants #loadShape("pantsR.svg")
        self.clips = clips #loadShape("clips.svg")
        self.play_mode = "CLASSIC"
        self.paused = False
        self.erase = False
        self.int_multi = random.shuffle([x for x in range(1,13)])
        self.one=[] #first button
        self.two=[] #second button
        self.three=[] #third button
        self.four = [] #Fourth Button
        self.five = [] # Settings Button
        self.clicked_button = 1 # Main menu clicked
        self.multiplication = [] # List of multiplication buttons 
        self.startButton = 0
        self.rounds = 1 
        self.instr_bub = []
        self.play_again_button = False
        self.level = 1 #starts off as level 1
        self.list_modes = [0]# List of modes visited 
        self.backB = Button(500,50,"BACK",22,"#3583BC") #back button
        self.back_paused = Button(400,400,"BACK",22,"#3583BC") #back button 
        self.playB = Button(500,700,"PLAY",22,"#3583BC") #play button on instruction screen
        self.scoresTranslate=0 #scrolling of scores on high score screen 
        self.window_trans = 0 # Scrolling of the names 
        self.mainS=Button(275,50,"MAIN MENU",20,"#3583BC")
        self.playA = Button(500,100,"PLAY AGAIN",20,"#FFFFFF") #game over screen play again button
        self.main=Button(500,580,"MAIN MENU",20,"#FFFFFF") #game over screen main menu button
        self.scoresA=Button(400,340,"HIGH SCORES",20, "#FFFFFF") # winning scores button
        self.scoresW=Button(500,100,"HIGH SCORES",20,"#3583BC") #game over score button
        self.mainW=Button(500,550,"MAIN MENU",20,"#3583BC") #game over screen main menu button 
        self.playS = Button(375,50,"PLAY AGAIN",20,"#3583BC")
        self.classicB = Button(80,150,"CLASSIC",20,"#3583BC")
        self.classicB.clicked = True
        self.on_music = Button(200,400,"ON",22,"#3583BC") #music button 
        self.on_music.clicked = True
        self.off_music = Button(200,490,"OFF",22,"#3583BC") #music off button 
        self.noon = Button(300,400,"NOON",22,"#3583BC") #noon button
        self.noon.clicked = True
        self.sunset = Button(300,500,"SUNSET",22,"#3583BC") #sunset button
        self.sunrise = Button(300,620,"SUNRISE",22,"#3583BC")
        self.yes = Button(385, 575,"YES",20,"#3583BC")
        self.window_yes = Button(510, 260,"YES, I WANT TO ERASE THESE SCORES",20,"#3583BC")
        self.window_no = Button(450, 260,"NO, I WANT TO KEEP THESE SCORES",20,"#3583BC")
        self.window_no.clicked = True
        self.no = Button(385,485," NO",20,"#3583BC")
        self.no.clicked = True
        self.multiplicationB = Button(180, 150,"General Multiplication", 20,"#3583BC")
        self.multiplication_table = Button(290,150,"MULTIPLICATION TABLE",20,"#3583BC")
        self.player = Player()
        self.instruction_paused = False
        self.name_found = False
        self.background_theme = "NOON"
        self.terms = [x for x in range(0, 13)]
        self.triangle_one = "#3583BC" # colour of triangles
        self.triangle_two = "#3583BC" # colour of triangles
        self.name = ""
        self.playerInfo = ""
        self.mode = 0
        self.num_to_mode = {0: self.main_screen(), 1: self.game_screen(), 2: self.instruction_screen(), 3: self.score_screen(), 4: self.game_over(), 5: self.winning_screen()}
        self.drops = [Drop(x*25, random.randint(0,3)) for x in range(6)]
        self.soap = Soap() 
        self.main_menu = Button(255,350,"MAIN MENU",22,"#3583BC") # MAIN MENU
        self.restart = Button(435,350, "RESTART", 22, "#3583BC")
        self.mode_restart = Button(500,700, "RESTART", 22, "#3583BC")
        self.mode_resume = Button(500,50,"RESUME",22,"#3583BC") #resume at mode of paused
        self.instr = Button(195, 350, "INSTRUCTIONS", 22, "#3583BC")
        self.resume = Button(375,350,"RESUME",22, "#3583BC") #back button
        self.pause_play_mode = Button(315, 350,"CHANGE MODE",22, "#3583BC") #back button
        self.ans = ""
        self.numB = 3 #number of bubbles drawn
        self.waterH=5 #water in g.tub 
        self.printing = False #no numbers are printed on screen
        self.int_to_coord = {}
        self.bubbles = []
        self.shower_played = False
        self.shampoo_played = False
        self.did_restart = False
        self.num_to_button = {1: self.one, 2: self.two, 3: self.three, 4: self.four, 5: self.five}
        self.instruction_bubbles()
        self.add_empty() #adds empty bubbles to list 
        self.add_colourful() # add colourful bubble
        self.table_initiation()
        self.button_initiation()
    
    def change_overlap(self, bubble, index):
        """
        Check if there is an overlap between the bubbles and change it if there is on
        
        @param BubbleGame self
        @param Bubble bubble: The bubble being created
        @param int index: The index of the bubble in the list
        @return None
        """
        bubble_length = len(self.bubbles)
        for i in range(bubble_length):
            if i != index:
                if abs(bubble.x - self.bubbles[i].x) <= 50:
                    if self.bubbles[i].x + 50 >= 700:
                        self.bubbles[i].x -= 50
                    else:
                        self.bubbles[i].x += 50
                        
    def instruction_bubbles(self):
        """
        Create the graphics for the bubbles that have equations at the instruction screen
        
        @param self BubbleGame
        @return None
        """
        
        b1 = Bubble(Equation(1, []))
        b1.x = 700
        b1.y = 200
        
        b2 = Bubble(Equation(3, []))
        b2.x = 100
        b2.y = 300
        
        b3 = Bubble(Equation(1, [], "MULTIPLICATION_ALL"))
        b3.x = 300
        b3.y = 400
        
        b4 = Bubble(Equation(3, []))
        b4.x = 160
        b4.y = 140
        
        b5 = Bubble(Equation(2, []))
        b5.x = 650
        b5.y = 400
        
        self.instr_bub = [b1, b2, b3, b4, b5]
        
    def draw_background(self):
        """ 
        Draw the background: The grass and sky
        
        @param BubbleGame self
        @return None
        """
        background("#C7F2FA")
        if self.background_theme == "NOON":
             g.setGradient(0,0,800,600,color(199,242,250),color(73,207,242), "Y_AXIS")
        elif self.background_theme == "SUNSET":
             g.setGradient(0, 0, 800, 600,color(178,148,203),color(240, 179, 99), "Y_AXIS")
        elif self.background_theme == "SUNRISE":
             g.setGradient(0,0,800,600, color(127,213,229),color(240,129,24), "Y_AXIS")
        
        
        #GRASS
        fill("#26DB48")
        noStroke()
        rect(0,550,800,600)
        fill("#2DC945")
        stroke("#2DC945")
        noStroke()
        for x in range(-10, 100):
            for y in range(5):
                triangle((x*10),560+(y*10), 28+(x*10), 545+(y*10),36+(x*10), 560+(y*10))
                
    def reset(self):
        """
        Reset the game.
        
        @param BubbleGame self
        @return None
        """        
        if not self.player.play_again: #if a new player is playing 
            self.player=Player() #reset player object, a new player shall play
            self.name="" #reset name
            self.play_mode = "CLASSIC"
            self.new.selected = False
            self.returning.selected = False
            
        self.terms = [x for x in range(0, 13)]
        self.bubbles = []
        if self.play_mode == "CLASSIC" or self.play_mode == "MULTIPLICATION_ALL":
            for i in range(3):
                self.bubbles.append(Bubble(Equation(1, self.terms, self.play_mode)))
                self.change_overlap(self.bubbles[i], i)
        self.level =  1
        self.rounds = 1
        self.instruction_paused = False
        self.paused = False
        self.drops=[]
        self.waterH=5 #water in g.tub 
        self.numB=3
        if self.did_restart:
            self.startButton = 1
            self.did_restart = False
        else:
            self.startButton = 0
        self.printing=False #no numbers are printed on screen
        self.add_drops()
        self.soap=Soap()
        self.player.win="NO"
        self.player.score=0 #score is 0
        self.player.lives=3 #lives are 3
        self.ans=""
        self.player.game=True
        self.shower_played = False
        self.shampoo_played = False
        self.returning.text_fill = "#A09999"
    
        
    ######################### Main Screen: Mode 0 ################### Helper Functions ####################################
    def button_initiation(self):
        """
        Create button bubble objects
        
        @param BubbleGame self
        @return None
        """
        for word in ["PLAY", "INSTRUCTIONS", "SCORES", "MODE", "SETTINGS"]:
            for x in range(len(word)):
                if word == "PLAY":
                    self.one.append(Button(200,(6+x)*50,"PLAY"[x],30,"#156395")) #each bubble has a letter
                elif word == "INSTRUCTIONS":
                    self.two.append(Button(270,(2+x)*50,"INSTRUCTIONS"[x],30,"#156395"))
                elif word =="SCORES":
                    self.four.append(Button(410,(5+x)*50,"SCORES"[x],30,"#156395"))
                elif word == "MODE":
                    self.three.append(Button(340,(6+x)*50,"MODE"[x],30,"#156395"))
                elif word == "SETTINGS":
                    self.five.append(Button(480,(4+x)*50,"SETTINGS"[x],30,"#156395"))
        self.one[0].pointed_at = True

                        
    def bubble_warp(self, bubble_list):
        """
        Move and draw emppty bubbles on the screen
        
        @param BubbleGame self
        @param list[Bubble]: Empty bubbles being drawn 
        @return None
        """
        #drawing bubbles 
        for bub in bubble_list:
            bub.drawing_bubbles()
            bub.move_y()
            bub.move_x()
        #wrapping of bubbles 
            if bub.x>800:
                bub.x=bub.x-800
            if bub.x<0:
                bub.x=bub.x+800
            if bub.y>600:
                bub.y=bub.y-600
            if bub.y<0:
                bub.y=bub.y+600
                
    def draw_buttons(self):
        """
        Draws buttons on home screen
        
        @param BubbleGame self
        @return None
        """
        for lists in [self.one, self.two, self.three, self.four, self.five]:
            for button in lists:
                button.draw_buttons()
    
    def main_screen(self):
        """
        Draw the main screen
        
        @param BubbleGame self
        @return None
        """
        global myFont
        #title
        fill("#3583BC")
        textFont(myFont)
        text("Bubble Sort", 150,100)
        self.bubble_warp(self.emptyBub)
        pushMatrix()
        translate(0,25)
        self.draw_buttons()
        self.mouse_over_main()
        popMatrix()
        textFont(default)
        text("There's too much water in the tub and any drop will cause a flood!",100,150)
        
        noFill()
        textSize(10)
        stroke("#086C1B")
        stroke("#077C1D")
        ellipse(11, 591, 10, 10)
        noStroke()
        fill("#077C1D")
        text("c",8, 595)
        text("Lana El Sanyoura", 20, 595)
        
    def mouse_over_main(self):
        """
        Highlight all the buttons on the main screen if one of the bubbles is pointed at
        
        @param BubbleGame self
        @return None
        """
        
        if 195 <= mouseY <= 245 and self.one[0].x - 25 <= mouseX <= self.one[-1].x + 25: # Play game
            for x in self.one:
                x.pointed_at = True

        elif 265 <= mouseY <= 315 and self.two[0].x - 25 <= mouseX <= self.two[-1].x + 25:
            for x in self.two:
                x.pointed_at = True
                
        elif 413 <= mouseY <= 460  and self.four[0].x - 25 <= mouseX <= self.four[-1].x + 25:
            for x in self.four:
                x.pointed_at = True
            
        elif 335 <= mouseY <= 385 and self.three[0].x - 25 <= mouseX <= self.three[-1].x + 25:
            for x in self.three:
                x.pointed_at = True
            
        elif 484 <= mouseY <= 533 and self.five[0].x - 25 <= mouseX <= self.five[-1].x + 25:
            for x in self.five:
                x.pointed_at = True
               
        else:
            for lists in [self.one, self.two, self.three, self.four, self.five]:
                for button in lists:
                    button.pointed_at = False

    def add_empty(self):
        """
        Create Bubbles for the screen designs 
        
        @param BubbleGame self
        @return None
        """
        for x in range(10): #bubbles for design 
                self.emptyBub.append(Bubble(""))
                self.emptyBub[x].y=random.randrange(0,600, 55)
                
                
    def add_colourful(self):
        """
        Colorful empty Bubbles for the Winning screen
        
        @param BubbleGame self
        @return None
        """
        for x in range(20): #bubbles for design 
                bubble = Bubble("", (random.randint(0,250), random.randint(0,250), random.randint(100,250), 150))
                bubble.speed = 2
                self.colourful.append(bubble)
                self.colourful[x].y=random.randrange(0,600, 55)

########################### Game Screen : Mode 1 ######################## Helper Functions #################################
    def draw_input(self, new,x,y):
        """
        Draw the input on the screen
        
        @param BubbleGame self
        @param str new: The new text
        @param int x: x-coordinate
        @param int y: y-coordinate
        @return None
        """
        fill(0,0,0)
        textSize(20)
        textFont(default)
        text(new,x,y)
    
    def add_drops(self):
        """
        Add drops for the shower 
        
        @param BubbleGame self
        @return None
        """
        for x in range (6):
            self.drops.append(Drop(x*25, random.randint(0,3)))
    


    def draw_score(self, points):
        """
        Draw the current score on the screen
        
        @param BubbleGame self
        @return None
        """
        
        fill(0,0,0)
        textSize(20)
        textFont(default)
        text("Score: " + str(points),5,45)
    
    def draw_lives(self, life):
        """
        Draw the text of how many lives there are
        
        @param BubbleGame self
        @param int life: The lives of the player
        @return None
        """
        
        fill(0,0,0)
        textSize(20)
        textFont(default)
        text("Lives: " + str(life), 5,65)
         
    def bubble_burst(self, bubble):
        """
        Draw the answers and a bursting animation whenever a Bubble reaches the clothing line
        
        @param BubbleGame self
        @param Bubble bubble
        @return None
        """
        bubX = bubble.x
        bubY = bubble.y        
        x= bubble.x
        y = bubble.y
        lx=bubble.x
        ly=bubble.y
        text_time = 0
        while x < bubX+150 and lx>bubX-150 and text_time < 4000:
            if x >= bubX+150 and lx <= bubX-150:
                text_time += 0.25
            else:
                lx=lx-(1*10)
                x=x+(1*10)
                y=y+(1*10)
                ly=ly-(1*10)
            
            fill("#2B95C9")
            noStroke()
            ellipse(x,y,5,5)
            ellipse(x+2,y,5,5)
            ellipse(x-2,y,5,5)
            ellipse(x+1,y,5,5)
            ellipse(x-1,y,5,5)
            ellipse(x,y+1,5,5)
            ellipse(x+2,y-1,5,5)
            ellipse(x-2,y+2,5,5)
            ellipse(x+1,y-2,5,5)
            ellipse(x-1,y+2,5,5)
            ellipse(lx,y,5,5)
            ellipse(lx+2,y-1,5,5)
            ellipse(lx-2,y-2,5,5)
            ellipse(lx+1,y+1,5,5)
            ellipse(lx-1,y+2,5,5)
            ellipse(lx,y+1,5,5)
            ellipse(lx+2,ly-1,5,5)
            ellipse(lx-2,ly+2,5,5)
            ellipse(lx+1,ly-2,5,5)
            ellipse(lx-1,ly+2,5,5)
            ellipse(x,ly,5,5)
            ellipse(x+2,ly,5,5)
            ellipse(x-2,ly,5,5)
            ellipse(x+1,ly,5,5)
            ellipse(x-1,ly,5,5)
            ellipse(x,ly+1,5,5)
            ellipse(x+2,ly-1,5,5)
            ellipse(x-2,ly+2,5,5)
            ellipse(x+1,ly-2,5,5)
            ellipse(x-1,ly+2,5,5)
            
            textSize(100)
            fill("#1BD125")
            text(bubble.equation.answer, bubX - 50, 100)
        stroke(0)
        textSize(20) 
        
        
    def paused_instructions(self):
        """
        Draw the instruction screen in the paused window
        
        @param BubbleGame self
        @return None
        """
        self.back_paused.draw_buttons()
        textSize(40)
        text("INSTRUCTIONS",280, 170)
        
        textFont(default)
        textSize(18)
        text("Solve the equations to pop the bubbles", 245,220)
        text("Pop the bubbles before they reach the line",245,260)
        text("Type the answers then press ENTER", 245, 300)
        text("3 bubbles will cause the tub to flood", 245,340)
            
    def score_window(self):
        """
        Draw the pause window
        
        @param BubbleGame self
        @return None
        """
        self.bubble_warp(self.emptyBub)
        g.clouds(250, 90, 40, 15, 5, 190)
        g.clouds(250, 260, 40, 15,11, 190)
        new_color = "#3583BC"
        returning = "#3583BC"
        returning_stroke = "#3583BC"
        new_stroke = "#3583BC"
        textSize(40)
            
        if 77 <= mouseY <= 207 and 230 <=  mouseX <= 620: # Mouse over new player
            self.new.selected = True
            self.returning.selected = False
            
            if self.name == "" and not (self.returning.x <= mouseX <= self.new.x + self.new.widths and self.new.y <= mouseY <= self.new.y + self.new.heights):
                self.returning.text_fill = "#A09999"
                self.returning.text_box = "Type & select your name"
            else:
                self.new.text_fill =  "#16527C" 
                self.new.text_box = self.name
                
        elif  207 < mouseY < 246: # In between
            self.new.selected = False
            self.returning.selected = False
            
            self.name = ""
            self.returning.text_fill = "#A09999"
            self.new.text_fill = "#A09999"
            self.returning.text_box = "Type & select your name"
            self.new.text_box = "Type your name & press ENTER"
            
        elif 246 <= mouseY <= 527 and 230 <=  mouseX <= 620: # Mouse over returning player
            self.new.selected = False
            self.returning.selected = True
        
            if self.returning.x <= mouseX <= self.returning.x + self.returning.widths and  246  <= mouseY <= self.returning.y + self.returning.heights:
                self.returning.text_fill = "#16527C" 
                if self.name != "":
                    self.returning.text_box = self.name
                else:
                    if self.returning.y <= mouseY <= self.returning.y + self.returning.heights:
                        self.returning.text_box = " "
                    else:
                        self.returning.text_fill = "#A09999" 
                        self.returning.text_box =  "Type & select your name"
                self.new.text_box = "Type your name & press ENTER"
                                
        fill(self.new.rect_stroke)
        textSize(40)
        text("New Player", 300, 130)

        textSize(40)
        fill(self.returning.rect_stroke)
        text("Returning Player", 265, 280)    

            
        # New
        self.new.draw_box()
        
        # Returning
        self.returning.draw_box()

        
        self.infoList = self.bubble_sort(self.reading_parcing()) #list of all players 
        pushMatrix()
        translate(0, self.window_trans) #moves the scores up and down 
        y = 10 #y position of names without filter
        filteredY = 10
        self.filtered_list = []

        for info in self.infoList: #prints out all lists
            textFont(default)
            fill("#3583BC")
            textSize(20)
            if self.new.selected:
                 if 349 <= y * 35 + self.window_trans <= 515:
                     text(info[0], 266, y * 35)
            else:
                if 331 <= mouseY <= 527 and 230 <=  mouseX <= 620: # Under returning textbox
                    if (y * 35) - 10 + self.window_trans  <= mouseY <= (y * 35)+ 10 + self.window_trans:            
                        if self.name == "": # Nothing is typed
                            if mouseX < 510: # Before the triangles
                                fill("#26DB48")
                            self.select_name(info[0], y, "Type & select your name")
                    else:
                        fill("#3583BC")
                        textSize(20)
                     
                if 349 <= y * 35 + self.window_trans <= 515 and self.name == "":
                    self.name = ""
                    text(info[0], 266, y * 35)
                
                elif self.name != "" and self.returning.selected and not self.new.selected:
                    input = self.name.lower()
                    name = info[0].lower()
                    
                    if input in name:
                        self.filtered_list.append(info[0])
                        # selecting text
                        if (filteredY * 35) - 10  + self.window_trans  <= mouseY <= (filteredY * 35) + 10  + self.window_trans:
                            if mouseX < 510: # Before the triangles
                                fill("#26DB48") # highlight the text
                            self.select_name(info[0], filteredY, self.name)
                        else:
                            fill("#3583BC")
                            textSize(20)
                        if 349 <= filteredY * 35 + self.window_trans <= 515:
                            text(info[0], 266, filteredY * 35)
                        filteredY += 1 

                        
            y += 1
        popMatrix()
        
        stroke("#3583BC")        
        if (510 <= mouseX <= 546 and 240 + 125 <= mouseY <= 275 + 125) and self.window_trans < 0:
            self.triangle_one = "#26DB48"
            self.triangle_two = "#3583BC"
    
        elif (510 <= mouseX <= 636 - 90 and 345 + 105 <= mouseY <= 380 + 105):
            self.triangle_two = "#26DB48"
            self.triangle_one= "#3583BC"
        else: 
            self.triangle_one= "#3583BC"
            self.triangle_two= "#3583BC"  
             
        fill(self.triangle_one)
        triangle(510, 275 + 125, 528, 240 + 125, 546, 275 + 125) #top triangle 
        fill(self.triangle_two)
        triangle(580 - 70, 345 + 105, 608 - 80, 380 + 105, 636 - 90, 345 + 105) #bottom triangle 
        fill("#3583BC")
        text("OR",400, 230)
    
    def select_name(self, name, y, default):
        """
        Select the name for the text box
        
        @param BubbleGame self
        @param str name
        @param int y: Position of the names
        @param str default: default name
        @return None
        """
        self.returning.text_fill =  "#16527C" 
        self.returning.text_box = name
        if mouseX <= 510:
            self.returning.text_box = name
        else:
            if default != self.name:
                self.returning.text_fill =  "#A09999" 
            self.returning.text_box = default
            

        if ((mousePressed or (keyPressed and key == ENTER)) and  (y * 35) - 10 + self.window_trans  <= mouseY <= (y * 35) + 10 + self.window_trans) and mouseX < 480:
            if self.filtered_list != [] or self.name == "":
                self.name = name
                fill("#0A6C1B")
                textSize(25)
                self.player.name = self.name
                self.bubbles = []
                for i in range(3):
                    self.bubbles.append(Bubble(Equation(1, self.terms, self.play_mode)))
                    self.change_overlap(self.bubbles[i], i)
                self.player.play_again = True
                self.player.new_player = False
                self.startButton = 1 #game starts
                self.window_trans = 0
        
    
    def pause_window(self):
        """
        Draw the pause window
        
        @param BubbleGame self
        @return None
        """
        g.clouds(250, 110, 40, 15, 15, 190)
        self.bubble_warp(self.emptyBub)
        if self.instruction_paused:
            self.paused_instructions()
        else:
            textSize(50)
            fill("#3583BC")
            text("PAUSE GAME", 270, 155)
            self.main_menu.draw_buttons()
            self.instr.draw_buttons()
            self.pause_play_mode.draw_buttons()
            self.resume.draw_buttons()
            if self.startButton == 2:
                self.restart.draw_buttons()
                 
    def game_strategy(self):
        """
        Game screen strategy
        
        @param BubbleGame self
        @return None
        """
        waterH = self.waterH
        level = self.level
        numB = self.numB
        clothing_line = 99.5

        length_list = len(self.bubbles)
            
        for l in range (length_list): #the bubbles in the list
            new_len = len(self.bubbles)
            if  0 <= new_len <= 2 and l == new_len:
                bubble = self.bubbles[new_len - 1]
                
            else:
                bubble = self.bubbles[l]
            
            if bubble.y> clothing_line and not bubble.equation.solve: #If the equation hasn't been solved and it's before the line 
                bubble.drawing_bubbles() #bubbles are drawn 
                if not self.paused:
                    bubble.move_y()            
            if  bubble.equation.solve or bubble.y <= clothing_line:
                
                if bubble.equation.solve:
                    pop.play()
                    self.player.score += 100
    
                elif bubble.y == clothing_line:
                    clothes_pop.play()
                    self.player.score -= 50
                    self.player.lives -= 1 #Player loses 1 life 
                    self.waterH -= 3 #water level rises
                    self.terms.append(bubble.equation.t2) 
                    self.bubble_burst(bubble)
                
                self.bubbles.pop(l)
                if not (self.play_mode == "MULTIPLICATION_ALL" or self.play_mode == "CLASSIC"):
                    if not self.terms == []:
                        self.bubbles.append(Bubble(Equation(self.level, self.terms, self.play_mode)))
                        self.change_overlap(self.bubbles[-1], len(self.bubbles) - 1)
                    elif self.bubbles == [] and self.terms == [] and self.rounds == 1:
                        self.rounds = 2
                        self.startButton = 0
                    elif self.bubbles == [] and self.terms == [] and self.rounds == 2:
                        self.player.game=False
                        self.rounds = 1
                        self.player.scores.append(self.player.score)
                        self.player.win="ULTIMATE"
                        claps.play()
                        
                    self.numB += 1
                    self.printing=False
                    bubble.equation.solve=False

                else:
                    self.bubbles.append(Bubble(Equation(self.level, self.terms, self.play_mode)))
                    self.change_overlap(self.bubbles[-1], len(self.bubbles) - 1)
                    self.numB += 1
                    self.printing=False
                    bubble.equation.solve=False
            
            if self.printing:
                self.draw_input(self.ans,400,580)
            self.draw_score(self.player.score)
            self.draw_lives(self.player.lives)
                
            if  self.player.lives==0:#lives are lost
                self.player.scores.append(self.player.score)
                self.player.win="LOST" #the g.tub has flooded
                self.player.game=False
                self.level = 1
            if self.play_mode == "CLASSIC" or self.play_mode == "MULTIPLICATION_ALL":
                if 0 <= numB < 12:
                    self.level = 1
                elif numB == 12:
                    self.level = 2
                    self.player.game=False
                    self.player.win="YES"
                elif 12 < numB < 21:
                    self.level = 2
                elif numB == 21:
                    self.level = 3
                    self.player.game=False
                    self.player.win="YES"
                
                elif 21 < numB < 42:
                    self.level = 3
                elif numB == 42:
                    self.player.game=False
                    self.player.scores.append(self.player.score)
                    self.player.win="ULTIMATE"
                    claps.play()
                    
    def game_screen(self):
        
        """ 
        Draw the game screen graphics
        
        @param BubbleGame self
        @return None
        """
        g.sun(self.background_theme)
        g.tub(self.startButton) #draws g.tub


        g.pause()

        fill(53,131,188,150)
        strokeWeight(3)
        stroke(53,131,188,150)
        noFill()
        ellipse(400, -100, 1700, 400)
        strokeWeight(1)
        fill(53,131,188,150)
        textSize(20)
        
        g.clouds(150,5, 60)
        g.clouds(400,20, 60)
        g.clouds(650,20, 60)
        g.clouds(400, 120, 50)
        g.clouds(180,150,50)
        g.clouds(0,100,50)
        g.clouds(680,150,50)
        
        shape(self.shirt, -40, 44)
        shape(self.pants, 620, 32)
        
        shape(self.clips, 45, 70, 70, 50)
        shape(self.clips, 115, 75, 70, 50)
        
        shape(self.clips, 695, 70, 70, 50)
        shape(self.clips, 750, 72, 72, 50)
        
        shape(self.clips, 245, 80, 70, 50)
        shape(self.clips, 315, 85, 70, 50)
        
        shape(self.clips, 445, 80, 70, 50)
        shape(self.clips, 515, 85, 70, 50)
        

            
        if self.startButton == 0: #before intro, button to initiate
            
            if self.level==1 and self.rounds == 1:                
                self.score_window()
                
            else:
                fill("#A6CEE8")
                bubble = Bubble("",(250,250,250, 100), 100)
                bubble.x = 410
                bubble.y = 305
                bubble.drawing_bubbles()
                fill(250,250,250)
                fill("#3583BC")
                textSize(26)
                if (self.play_mode == "CLASSIC" or self.play_mode == "MULTIPLICATION_ALL"):
                    if 1 < self.level:
                        text("LEVEL {}".format(self.level), 360,240)
                        text("PRESS ENTER", 330,400)
                        g.water(self.waterH)
                else:
                    if 1 < self.rounds:
                        text("ROUND ", 350,240)
                        text(self.rounds,450,240)
                        text("PRESS ENTER", 320,400)
                        g.water(self.waterH)
    
            
        elif self.startButton==1: #intro
            len_drops = len(self.drops)
            for l in range(len_drops): #drop of water falling down 
                drop = self.drops[l]
                if drop.y < 152: #when it's over the g.tub
                    drop.drop_move() #the drops move towards the g.tub 
                    drop.draw_drops()
                    
                if drop.y >= 152:
                    if not self.shower_played:
                        shower.play()
                        self.shower_played = True
                    g.water(self.waterH)
                    if self.soap.widths >= 10 and self.soap.yd != 501: #if water reaches max
                        self.soap.draw_soap() 
                        self.soap.squeeze()
                        fill(250,0,0)
                        self.soap.draw_soapd()
                        self.soap.move_soapd()
                    
                    
                if self.soap.yd >=501: #soap drops
                    if not self.shampoo_played:
                        self.shampoo_played = True 
                        shampoo_bubbles.play()
                    self.startButton=2 #start game 
                        
                        
        elif self.startButton == 2: #game starts
            g.water(self.waterH)
            if self.player.game: #no one has won
                self.game_strategy()
                
            else: #game has ended or levels change
                if self.player.win == "YES": # Moving to a different level
                    self.startButton=0
                    
                else: # Game ends
                    max_score = max(self.player.scores)
                    self.playerInfo = (self.player.name + "," + str(max_score)+"\n") #score and name of player
                    self.write_info(self.playerInfo)

                    if self.player.win=="LOST":
                        self.mode = 7 #game over screen
                        self.list_modes.append(self.mode)
                    elif self.player.win=="ULTIMATE":
                        self.list_modes.append(self.mode)
                        self.mode = 6 #winning screen 
        if self.paused:
            self.pause_window()

                    
                
################################################ Instruction Screen, Mode 2 ######################################## Helper Functions ############################################

    def instruction_screen(self):
        """
        Draw the instruction screen
        
        @param BubbleGame self
        @return None
        """
        global myFont,default
        
        shape(self.shirt, -40, 44)
        shape(self.pants, 620, 32)
        
        pushMatrix()
        translate(-20,0)
        g.tub(2)
        g.water(5)
        popMatrix()
        
        self.backB.draw_buttons()
        self.playB.draw_buttons()
        fill("#3583BC")
        textFont(myFont)
        textSize(70)
        text("INSTRUCTIONS",160,80)
        textFont(default)
        text("Solve the equations to pop the bubbles", 220,190)
        text("Type the answers then press ENTER",220,240)
        text("Pop the bubbles before they reach the clothing line!", 220, 290)
        text("3 bubbles will cause the tub to flood", 220,340)
        
        strokeWeight(3)
        stroke(53,131,188,150)
        noFill()
        ellipse(400, -100, 1700, 400)
        strokeWeight(1)
        
        shape(self.clips, 45, 70, 70, 50)
        shape(self.clips, 115, 75, 70, 50)
        
        shape(self.clips, 695, 70, 70, 50)
        shape(self.clips, 750, 72, 70, 50)
        
        shape(self.clips, 245, 90, 70, 50)
        shape(self.clips, 315, 90, 70, 50)
        
        shape(self.clips, 445, 90, 70, 50)
        shape(self.clips, 515, 90, 70, 50)
        
        for bub in self.instr_bub:
            bub.drawing_bubbles()
        if self.instr_bub:
            self.draw_input(self.instr_bub[0].equation.answer, 400, 580)
        
        

################################# Mode of Play, Mode 3 ################# Helper Functions ############
    def table_initiation(self):
        """
        Create the buttons of the multiplication table
        
        @param BubbleGame self
        @return None
        """
        numbers = ["1","5", "9", "2","6","10", "3", "7", "11" ,"4", "8", "12"]
        i = 0
        for x in range(4):
            for y in range(3):
                self.multiplication.append(Button((360 + 80*y),(230+ 80*x),numbers[i],30,"#156395"))
                self.int_to_coord[numbers[i]] = (230+ 80*x, 360 + 80*y)
                i += 1
        
                
    def multiplication_screen(self):
        """
        Drawt the multiplication mode buttons 

        @param BubbleGame self
        @return None
        """
        
        fill("#3583BC")
        textSize(50)
        text("Game Mode", 250, 50)
        textSize(30)
        self.classicB.draw_buttons()
        text("Classic mode allows you to add, subtract and", 200, 125)
        text(" multiply all numbers and grows more difficult by level.", 195, 150)
        
        self.multiplicationB.draw_buttons()
        text("General Multiplication mode lets you practice your", 200, 225)
        text("multiplication skills with any numbers from 0 to 12", 200, 250)
        self.multiplication_table.draw_buttons() 
        for x in self.multiplication:
            x.draw_buttons()
        if self.paused:
            if self.startButton == 0 and self.level == 1 and self.rounds == 1: # choosing names 
                self.backB.draw_buttons()
            else:
                self.mode_restart.draw_buttons()
                self.mode_resume.draw_buttons()
        else:
            self.playB.draw_buttons()
            self.backB.draw_buttons()
    
########################################################################### SCORE SCREEN, Mode 4 ############################### Helper Functions #######################################################################################################################        

    def score_screen(self):
        """Draw the high Score Screen
        
        @param BubbleGame self
        @return None
        """
        global myFont
        
        self.infoList = self.bubble_sort(self.reading_parcing()) #list of all players 
        pushMatrix()
        translate(0, self.scoresTranslate) #moves the scores up and down 
        y=1.5 #y position of names and scores
        ranking=1
        fill("#3583BC")
        for info in self.infoList: #prints out all lists
            textFont(default)
            textSize(20)
            if 120 <= y * 100 + self.scoresTranslate <= 600:
                textSize(20)
                text(ranking,200,y*100)
                text(info[0], 300, y *100)
                text(info[1], 600,y * 100)
            y += 1
            ranking += 1

        popMatrix()

        #Title and graphics 
        
        if self.background_theme == "NOON":
             g.setGradient(0,0,800,120,color(73,207,242),color(167, 236, 247), "Y_AXIS")
        elif self.background_theme == "SUNSET":
             g.setGradient(0, 0, 800, 120,color(240, 179, 99),color(191,154,193), "Y_AXIS")
        elif self.background_theme == "SUNRISE":
             g.setGradient(0,0,800,120,color(240,129,24),color(158,193,198), "Y_AXIS")

        textFont(myFont)
        fill("#3583BC")
        textSize(70)
        text("Scores",300,100)
        
        if ((680 <= mouseX <= 736 and 220 <= mouseY <= 275) or (keyCode == UP)) and self.scoresTranslate<0:
            self.triangle_one = "#26DB48"
            self.triangle_two= "#3583BC"
    
        elif (680 <= mouseX <= 736 and 345 <= mouseY <= 400) or keyCode == DOWN:
            self.triangle_two = "#26DB48"
            self.triangle_one= "#3583BC"
        else: 
            self.triangle_one= "#3583BC"
            self.triangle_two= "#3583BC"  
             
        fill(self.triangle_one)
        triangle(680, 275, 708, 220, 736, 275) #top triangle 
        fill(self.triangle_two)
        triangle(680, 345, 708, 400, 736, 345) #bottom triangle 
        textFont(default)
        self.mainS.draw_buttons() #main menu button
        if self.play_again_button:
            self.playS.draw_buttons()
        
    def write_info(self, player_):
        """
        Write the player information for theh high score screen
        
        @param BubbleGame self
        @return None
        """
        superList = self.reading_parcing()
        if (self.player.play_again and not self.did_restart) or not self.player.new_player:
            length_names = len(superList)
            highscore= open("scores.txt",'w') # over writes 
            highscore.write("")
            highscore.close() 
            
            highscore= open("scores.txt",'ab') # over writes 
 
            for y in range(length_names):
                if superList[y][0] == self.player.name:
                    if int(superList[y][1]) <= max(self.player.scores) and len(self.player.scores) >= 2:
                        superList[y][1] = str(max(self.player.scores))
                highscore.write(superList[y][0] + "," + str(superList[y][1]) + "\n")

        else: 
            highscore= open("scores.txt",'ab') # over writes
            highscore.write(player_)
        highscore.close()
        self.did_restart = False
        return
        
    def reading_parcing(self):
        """
        Read the score file and turn it into an array of names and scores
        
        @param BubbleGame self
        @return list[(str name: Player's name, int score: Player's score)]
        """
        highscore= open("scores.txt") #opens file 
        superList = highscore.readlines() #reads file
        for y in range(len(superList)): #for each line in the list
            superList[y]=superList[y].strip() #remove "/n"
            superList[y]=superList[y].split(',') #split name and score
            superList[y][1]=int(superList[y][1]) #turn score into int for sorting                
        return superList
    
    def bubble_sort(self, lists):
        """
        Sort the scores from the greatest to the least
        
        @param BubbleGame self
        @return list[(str name: Player's name, int score: Player's score)]
        """
        sort=False
        while sort==False:
            sort=True
            for x in range((len(lists)-1)):
                if lists[x][1] < lists[x+1][1]: 
                    sort=False
                    lists[x],lists[x+1]=lists[x+1],lists[x]
    
        if sort==True:
            return lists
    
########################################################### Game Over : Mode 5 #####################################################################################################################################################################
        
    def game_over(self):
        """
        Draw the game over screen
        
        @param BubbleGame self
        @return None
        """
        global default

        player = self.player
        g.setGradient(0,0,800,600, color(13,185,172),color(9,44,129), "Y_AXIS")
        fill(250,250,250)
        textFont(myFont)
        textSize(90)
        text("GAME OVER",150,100)
        textSize(30)
        textFont(default)
        text("THE TUB OVERFLOWED!",280, 130)
        textSize(50)
        text("Your score is {}".format(player.score),200,300)
        self.playA.draw_buttons() #play again
        textFont(default)
        self.main.draw_buttons() #main menu
        self.scoresA.draw_buttons()
        self.bubble_warp(self.emptyBub)
        
##################################################### Winning Screen : Mode 6 ################################# Helper Functions ################################################
    def winning_screen(self):
        """
        Draw the Winning score Screen
        
        @param BubbleGame self
        @return None
        """
        global default
        
        player = self.player
        fill(250,250,250)
        fill("#3583BC")
        textFont(myFont)
        textSize(90)
        text("YOU WON!",190,100)
        textSize(40)
        textFont(default)
        text("YOU SAVED THE DAY!!", 300, 130)
        textSize(50)
        fill("#26DB48")
        # 200 for 8 letters , y = 232
        text("AMAZING WORK",220, 200)
        len_name = len(player.name)
        fill("#26DB48")
        text(player.name, 350 - ((len_name - 4)*10), 260) # 4 is the ultimate
        textSize(30)
        fill("#3583BC")
        text("Your score is {}".format(player.score),260,310)
        textFont(default)
        self.playA.draw_buttons()
        self.main.draw_buttons()
        self.scoresA.draw_buttons()
        self.bubble_warp(self.colourful)
    
################################### SETTINGS SCREEN, MODE 7 ############ Helper Functions #######
    
    def erase_window(self):
        """
        Draw the "Are You Sure You Want to Erase the Scores" window
        
        @param BubbleGame self
        @return None
        """
        g.clouds(230, 150, 40, 16, 17, 240)
        textSize(40)
        fill("#AA1A1A")
        text("ARE YOU SURE", 290, 185 )
        textSize(20)
        text("\n YOU WANT TO ERASE ALL SCORES?".format(), 250, 185)
        textSize(20)
        fill("#3583BC")
        text(" Erasing all scores means that the \ncurrent score screen will be cleared.",260, 270)
        textSize(30)
        fill("#AA1A1A")
        text("DO YOU STILL WANT TO\n   ERASE ALL SCORES?",250, 363)
        
        self.window_yes.draw_buttons()
        self.window_no.draw_buttons()
        

    def settings_screen(self):
        """
        Draw the settings  screen
        
        @param BubbleGame self
        @return None
        """
        
        global myFont,default
        fill("#3583BC")
        self.bubble_warp(self.emptyBub)
        self.backB.draw_buttons()
        self.playB.draw_buttons()
        textFont(myFont)
        textSize(70)
        text("SETTINGS",250,100)
        textFont(default)
        textSize(35)
        text("MUSIC:", 210,210)
        textSize(10)
        text("Little Idea by Bensound", 210, 230)
        textSize(35)
        
        text("COLOURS:",200,310)
        text("ERASE SCORES:", 200, 400)
        
        for button in [self.noon, self.sunset, self.sunrise, self.on_music, self.off_music, self.yes, self.no]:
            button.draw_buttons()
        
        if self.erase:
            self.erase_window()
#########################################################################################        

class Equation():
    """
    Equation object with two terms and an operator
    
    === Attributes ===
    @param dict{int level: list[str operator] } operator_to_list
    @param int level: Current level of the BubbleGame
    @param list[int] terms: List of the terms from 0 to 12 to be used for multiplication mode
    @param str play_mode: The play mode, either "CLASSIC", "MULTIPLICATION_ALL", or "MULTIPLICATION(any number from 0 to 12)"
    @param int t1: First term
    @param int t2: Second term
    @param int answer: Answer of the equation
    @param str formula: The formula of the equation that is drawn in the bubbles
    @param bool solve: True iff the equation has been solved 
    """
    def __init__(self, l, terms, play_mode = "CLASSIC"):
        
        """
        Create an instance of Equation
        
        @param int l: Current level of the BubbleGame
        @param list[int] terms: List of the terms to be used for multiplication mode
        @param str play_mode: The play mode, either "CLASSIC", "MULTIPLICATION_ALL", or "MULTIPLICATION(any number from 0 to 12)"
        @return None
        """
        
        operator_to_list = {1: ["+","-"], 2:["+","-","x"], 3: ["+", "x"]}
        self.level=l
        self.terms = terms
        if play_mode == "CLASSIC":
            if self.level==1:
                self.operator=random.choice(operator_to_list[1])
                self.t1=random.randint(0,9)
                self.t2=random.randint(0,9)
            elif self.level==2:
                self.operator=random.choice(operator_to_list[2])
                self.t1=random.randint(0,9)
                self.t2=random.randint(0,16)
            elif self.level==3:
                self.operator= random.choice(operator_to_list[3])
                self.t1=random.randint(5,16)
                self.t2=random.randint(5,16)
                
        elif play_mode == "MULTIPLICATION_ALL":
            self.operator = "x"
            if self.level==1:
                self.t1=random.randint(0,5)
                self.t2=random.randint(0,7)
            elif self.level==2:
                self.t1=random.randint(0,7)
                self.t2=random.randint(0,12)
            elif self.level==3:
                self.t1=random.randint(5,12)
                self.t2=random.randint(5,12)
                
        elif "MULTIPLICATION" in play_mode and 15 <= len(play_mode) <= 16: # play_mode = MULTIPLICATIONx
            self.operator = "x"
            integer = int(play_mode[14:])
            self.t1= integer
            random.shuffle(self.terms)
            self.t2 = self.terms.pop()
        self.formula = self.sort_eq()
        self.answer = self.find_answer()
        self.solve = False #whether the equation has been solved 
        
                
            
    def sort_eq(self): 
        """
        Return an equation the produces a positive solution
        
        @param Equation self
        @return str
        """
        if self.operator=="-" and self.t2>self.t1: #If subtraction was taking place, the answer can't be negative 
            self.t1,self.t2=self.t2,self.t1 #swap numbers 
            
        self.formula=str(self.t1)+self.operator+str(self.t2) #formula that is written is in form of a string 
        return self.formula 
    
    def find_answer(self): 
        """
        Return the answer to the equation
        
        @param Equation
        @return int 
        """
        if self.operator=="+":
            self.answer=self.t1+self.t2
            
        elif self.operator=="x":
            self.answer=self.t1*self.t2
            
        elif self.operator=="-":
            self.answer=self.t1-self.t2
        
        return self.answer

    
class Bubble():
    """
    Bubble object
    
    === Attributes ===
    @param int x: X-coordinate of the Bubble
    @param int y: Y-coordinate of the Bubble
    @param int diameter
    @param Equation equation
    @param int speed: Speed of the bubble
    @param tuple(int, int, int, int(optional)) fills: The fill of the colors 
    """
    def __init__(self,eq, fills = (250,250,250,150), diameter = 55):
        """
        Create an instance of Bubble object
        
        @param Equation eq: equation
        @param tuple(int, int, int, int(optional)) fills: The fill of the colors
        @param int diameter
        @return None
        """
        self.x= random.randrange(150,700, 60)
        self.y= 500
        self.diameter= diameter
        self.equation=eq
        self.speed= 1.5
        self.fills = fills

    def drawing_bubbles(self):
        """
        Draw a bubble object 
        
        @param Bubble self
        @return None
        """
        fill(self.fills[0], self.fills[1], self.fills[2], self.fills[3])
        stroke("#538B95")
        ellipse(self.x,self.y,self.diameter, self.diameter)
        pushMatrix()
        translate(-40,-30)
        noStroke()
        if self.diameter >= 100:
            fill(83,139,149,20)
            arc(self.x + 40, self.y + 60, 55, 18, QUARTER_PI, PI + QUARTER_PI, CHORD)
    
            fill(283,139,149,50)
            arc(self.x + 46, self.y + 5, 55, 20, PI + PI/2, 2*PI + PI/8, CHORD)
        else:
            fill(83,139,149,20)
            arc(self.x + 40, self.y + 48, 30, 10, QUARTER_PI, PI + QUARTER_PI, CHORD)
    
            fill(283,139,149,50)
            arc(self.x + 46, self.y + 20, 30,15, PI + PI/2, 2*PI + PI/8, CHORD)
        
        popMatrix()
        fill(200,200,250,150)
        fill("#084976")
        stroke(0,0,0)
        textSize(13)
        if self.equation!="":
         text(self.equation.formula,self.x-20,self.y)
        
    def move_y(self):
        
        """
        Move the Bubble downwards 
        
        @param Bubble self
        @return None
        """
        self.y -= (1*self.speed)

    def move_x(self):
        """
        Move the Bubble sideways to the right 
        
        @param Bubble self
        @return None
        """
        self.x += 1

class Drop():
    """
    Drop object
    
    === Attributes ===
    @param int x: x-coordinate
    @param int y: y-coordinate
    """
    def __init__(self,x, y):
        """
        Create an instance of Drop object
        
        @param int x: x-coordinate
        @param int y: y-coordinate
        @return None
        """
        self.x=x
        self.y= y
        
    def drop_move(self):
        """
        Move the drop downwards
        @param Drop self
        @return None
        """
        self.y += 4
        
    def draw_drops(self):
        """
        Draw the drops 
        @param Drop self
        @return None
        """
        fill("#248BB2")
        pushMatrix()
        translate(150,350)
        ellipse(self.x,self.y+15,15,15)
        triangle(self.x-8,self.y+15, self.x, self.y, self.x+8, self.y+15)
        popMatrix()

class Soap():
    """
    Soap bottle oject
    
    === Attributes ===
    @param int x: x-coordinate
    @param int y: y-coordinate
    @param int widths: width of the shampoo bottle
    @param int heights: height of the shampoo bottle
    @param int xd: x-coordinate of the ellipse on the shampoo
    @param int yd: y-coordinate of the ellipse on the shampoo
    """
    def __init__(self, x = 509, y = 350, widths = 50, heights = 55):
        """
        Create an insrance of self Soap
        
        @param self Soap
        @param int x: x-coordinate
        @param int y: y-coordinate
        @param int widths: width of the shampoo bottle
        @param int heights: height of the shampoo bottle
        @return None
        """
        self.x= x
        self.y= y
        self.widths= widths
        self.heights= heights
        self.xd=self.x+(17)
        self.yd=self.y+43
        
    def draw_soap(self):
        """
        Draw the soap object
        
        @param Soap self
        @return None
        """
        fill("#F7A711")
        stroke("#DE4802")
        rect(self.x,self.y, self.widths,self.heights, 6, 6, 50, 50)
        fill(222,72,2,50)
        rect(self.x+15,self.y+43, self.widths-30,self.heights-35, 6, 6, 50, 50)
        fill(250,250,250)
        rect(self.x+2,self.y+2, self.widths-5,self.heights-5, 6, 6, 50, 50)
        fill("#DE4802")

    def squeeze(self):
        """
        Draw the graphics for the squeezing action
        
        @param Soap self
        @return None
        """
        self.widths -= 1 #squeeze
    
    def draw_soapd(self):
        """
        Draw the soap drop
        """
        
        fill("#F7A711")
        noStroke()
        ellipse(self.xd,self.yd+15,15,15)
        triangle(self.xd-8,self.yd+15, self.xd, self.yd, self.xd+8, self.yd+15)
    
    def move_soapd(self):
        self.yd += 3
        
class Button():
    """Buttons on main screen
    @param int x
    @param int y
    @param str written: what is written on the bubble 
    @param int tSize: text_size 
    @param int diameter
    @param str default_fill: To be the general go-to
    @param str used: The fill currently in use
    @param bool pointed_at: True iff button is pointed at
    @param bool clicked : True iff button is clicked 
    @param str selected_fill: The fill if the button has been selected
    """
    
    def __init__(self, y, x,texts, text_size, fills):
        self.x=x
        self.y=y
        self.written=texts #what is written on the bubble 
        self.tSize= text_size 
        self.diameter=50
        self.default_fill = fills
        self.used = fills
        self.pointed_at = False
        self.clicked = False
        self.selected_fill = "#26DB48"
        
    def draw_buttons(self):
        global default
        fill(250,250,250,150)
        stroke("#538B95")
        ellipse(self.x,self.y,self.diameter, self.diameter)
        pushMatrix()
        translate(-40,-30)
        noStroke()

        fill(283,139,149,50)
        arc(self.x + 46, self.y + 20, 30, 15, PI + PI/2, 2*PI + PI/8, CHORD)

        popMatrix()
        self.mouse_over()
        fill(self.used)
        stroke(0,0,0)
        textFont(default)
        textSize(self.tSize)
        text(self.written,self.x-4,self.y+15)
        fill(self.default_fill)
                
    def mouse_over(self):
        """
        Return True iff the mouse is over the button
        """
        radius = self.diameter/2
        default_size = self.tSize
        if self.written != "MULTIPLICATION TABLE":
            if ((self.y - radius <= mouseY <= self.y + radius)\
                    and (self.x - radius <= mouseX <= self.x + radius)) or self.pointed_at :
                        self.used = self.selected_fill
                        
            elif self.clicked:
                self.used = self.selected_fill
                        
            else:
                self.used = self.default_fill

def setup():
    global shirt, pants, clips, claps, myFont, default, bubble_game, file, pop, shower, clothes_pop, shampoo_bubbles
    size(800,600)
    myFont = createFont("DefinitelyMaybe",95) #bubble
    default=createFont("ACaslonPro-Bold-48",20)
    file = SoundFile(this, "bensound-littleidea.mp3")
    pop = SoundFile(this, "Pop_2-Texavery-8930_hifi.mp3")
    claps = SoundFile(this, "applause-5.mp3")
    clothes_pop = SoundFile(this,"idg-plun-intermed-824_hifi2.wav")
    shower = SoundFile(this, "Splash-Texavery-8929_hifi-2.mp3")
    shampoo_bubbles = SoundFile(this,"51745__erkanozan__bubbles.wav")
    shirt = loadShape("clothes.svg")
    pants = loadShape("pantsR.svg")
    clips = loadShape("clips.svg")
    bubble_game = BubbleGame()
    if bubble_game.on_music.clicked:
        file.loop()
    
def draw():  
    bubble_game.draw_background() 
 
    if bubble_game.mode == 0:
        #main screen
        bubble_game.main_screen()
        
    elif bubble_game.mode == 1:#play game 
        bubble_game.game_screen()

    elif bubble_game.mode == 2: #go to instruction screen
        bubble_game.instruction_screen() 
        
    elif bubble_game.mode == 3:
        bubble_game.multiplication_screen()
        
    elif bubble_game.mode == 4:
        bubble_game.score_screen()   
        
    elif bubble_game.mode == 5: #settings
        bubble_game.settings_screen()
        
    elif bubble_game.mode == 6:
        bubble_game.winning_screen()
    
    elif bubble_game.mode == 7:
        bubble_game.game_over()

    
def keyPressed():
    global bubble_game    
    if bubble_game.mode==1: #game screen
        if bubble_game.startButton==0 and key!=CODED:            
            if bubble_game.level == 1 and bubble_game.rounds == 1: 
                if key==BACKSPACE:
                        bubble_game.name= bubble_game.name[:-1] #erase last character
                        bubble_game.name = bubble_game.name.strip()
                elif key!=BACKSPACE and key!=" " and key!=ENTER and str(key) != ",":
                        bubble_game.name = bubble_game.name+str(key) #concatinate key ans
                        bubble_game.printing = True
                elif key==ENTER and bubble_game.name != "" and bubble_game.new.selected:
                        bubble_game.player.name = bubble_game.name
                        bubble_game.bubbles = []
                        for i in range(3):
                            bubble_game.bubbles.append(Bubble(Equation(1, bubble_game.terms, bubble_game.play_mode)))
                            bubble_game.change_overlap(bubble_game.bubbles[i], i)
                        bubble_game.startButton = 1 #game starts
            elif bubble_game.level!=1 or bubble_game.rounds != 1:
                if bubble_game.play_mode == "CLASSIC" or bubble_game.play_mode == "MULTIPLICATION_ALL":
                    if key == ENTER:
                        bubble_game.startButton = 2 #start game again 
                        bubble_game.numB += 1
                        bubble_game.player.game = True
                        bubble_game.player.win = "NO"
                else:
                    if key==ENTER:
                        bubble_game.terms = [x for x in range(0,13)]
                        for i in range(3):
                            bubble_game.bubbles.append(Bubble(Equation(1, bubble_game.terms, bubble_game.play_mode)))
                            bubble_game.change_overlap(bubble_game.bubbles[i], i)
                        bubble_game.player.game = True
                        bubble_game.player.win = "NO"
                        bubble_game.startButton = 2 #start game again
                        
                        
            
        if key!= ENTER and key!= CODED and bubble_game.startButton!=0:
            if key==BACKSPACE:
                bubble_game.ans = bubble_game.ans[:-1] #erase last character
                bubble_game.ans = bubble_game.ans.strip()
            elif key!=BACKSPACE:
                bubble_game.ans = bubble_game.ans+str(key) #concatinate key ans
                bubble_game.printing = True
        elif key==ENTER: #when enter key is pressed 
            final= bubble_game.ans #final answer is stored 
            bubble_game.ans="" #answer taken back to blank for next concatination 
            if bubble_game.mode==1:
                bubbles_len = len(bubble_game.bubbles)
                for n in range(bubbles_len): #Checks if answer matches any answers of equations 
                    if final==str(bubble_game.bubbles[n].equation.answer):
                        bubble_game.bubbles[n].equation.solve = True
    if bubble_game.mode == 4:
        
            if key == CODED:
                if keyCode == UP and bubble_game.scoresTranslate < 0:

                        bubble_game.triangle_one = "#118325"
                        bubble_game.triangle_two= "#3583BC"
                        bubble_game.scoresTranslate += 100
            
                elif keyCode == DOWN:
                    bubble_game.triangle_two = "#118325"
                    bubble_game.triangle_one= "#3583BC"
                    bubble_game.scoresTranslate -= 100
                    
                    if - bubble_game.scoresTranslate == (int(len(bubble_game.infoList)*100)):
                        bubble_game.scoresTranslate = 0
                else:
                    bubble_game.triangle_one= "#3583BC"
                    bubble_game.triangle_two= "#3583BC" 
                    
def mousePressed():
    global bubble_game    

    playerInfo = bubble_game.playerInfo
    player = bubble_game.player
    
################################## MAIN SCREEN, MODE 0 ##########################################                 


    if bubble_game.mode == 0: # Main menu screen
        bubble_game.play_again_button = False
        bubble_game.level=1
        bubble_game.startButton=0
        
        # Play Game        
        if 195 <= mouseY <= 245 and bubble_game.one[0].x - 25 <= mouseX <= bubble_game.one[-1].x + 25: # Play game
            bubble_game.mode = 1
            bubble_game.list_modes.append(bubble_game.mode)

        # Instructions 
        elif 265 <= mouseY <= 315 and bubble_game.two[0].x - 25 <= mouseX <= bubble_game.two[-1].x + 25:
            bubble_game.mode = 2
            bubble_game.list_modes.append(bubble_game.mode)
         
        # Mode       
        elif 335 <= mouseY <= 385 and bubble_game.three[0].x - 25 <= mouseX <= bubble_game.three[-1].x + 25:
            bubble_game.mode = 3
            bubble_game.list_modes.append(bubble_game.mode)
            
        # Scores        
        elif 413 <= mouseY <= 460  and bubble_game.four[0].x - 25 <= mouseX <= bubble_game.four[-1].x + 25:
            bubble_game.mode = 4
            bubble_game.list_modes.append(bubble_game.mode)
        
        # Settings
        elif 484 <= mouseY <= 533 and bubble_game.five[0].x - 25 <= mouseX <= bubble_game.five[-1].x + 25: 
            bubble_game.mode = 5
            bubble_game.list_modes.append(bubble_game.mode)
            
       
################################## GAME SCREEN, MODE 1 ##########################################                 
    
    elif bubble_game.mode == 1: # Game screen
        if bubble_game.instruction_paused:
            if bubble_game.back_paused.y - 50  <= mouseY <= bubble_game.back_paused.y + 50 \
                and bubble_game.back_paused.x - 50  <= mouseX <= bubble_game.back_paused.x + 50:
                    bubble_game.instruction_paused = False
                        
        else:
            if bubble_game.startButton == 0:
                
                if bubble_game.new.x <= mouseX <= bubble_game.new.x + bubble_game.new.widths and bubble_game.new.y <= mouseY <= bubble_game.new.y + bubble_game.new.heights:
                    bubble_game.name = ""
                    
                elif bubble_game.returning.x <= mouseX <= bubble_game.returning.x + bubble_game.returning.widths and bubble_game.returning.y <= mouseY <= bubble_game.returning.y + bubble_game.returning.heights:
                    bubble_game.name = ""
                
                
                
                if 510 <= mouseX <= 636 - 80 and 265 <= mouseY <= 400 and bubble_game.window_trans < 0:
                    bubble_game.triangle_one = "#118325"
                    bubble_game.triangle_two= "#3583BC"
            
                    bubble_game.window_trans += 175
            
                elif 510 <= mouseX <= 636 - 80 and 450 <= mouseY <= 485:
                    bubble_game.triangle_two = "#118325"
                    bubble_game.triangle_one= "#3583BC"
                    bubble_game.window_trans -= 175
                
                number_of_pages =  (len(bubble_game.infoList)/5)    
                if bubble_game.name != "": # No name is typed:
                    number_of_pages =  (len(bubble_game.filtered_list)/5)
                    
                if - bubble_game.window_trans/175 > number_of_pages:
                    bubble_game.window_trans = 0
                
                    
            if 5 <= mouseX <= 40 and 0 <= mouseY <= 40:
                bubble_game.paused = True
                
            if bubble_game.paused == True:
                if bubble_game.main_menu.y - 20 <= mouseY <= bubble_game.main_menu.y + 20 \
                    and bubble_game.main_menu.x - 50 <= mouseX <= bubble_game.main_menu.x + 50: # Main Menu
                        mode = 0
                        bubble_game.level=1
                        bubble_game.player.game=True
                        bubble_game.player.play_again=False
                        bubble_game.reset()
                        bubble_game.mode=0 
                        bubble_game.list_modes.append(bubble_game.mode) 
                        bubble_game.paused = False
                    
                elif bubble_game.restart.y - 25 <= mouseY <= bubble_game.restart.y + 25 \
                    and bubble_game.restart.x - 25  <= mouseX <= bubble_game.restart.x + 25: # Restart
                        bubble_game.level=1
                        mode = bubble_game.play_mode
                        bubble_game.player.play_again=True #resets game but not player info
                        bubble_game.reset()
                        bubble_game.did_restart = True
                        bubble_game.startButton = 1
                        bubble_game.mode= 1
                        bubble_game.bubbles = []
                        for i in range(3):
                            bubble_game.bubbles.append(Bubble(Equation(1, bubble_game.terms, bubble_game.play_mode)))
                            bubble_game.change_overlap(bubble_game.bubbles[i], i)                
                        bubble_game.play_mode = mode
                        bubble_game.paused = False
                    
                elif bubble_game.resume.y - 25  <= mouseY <= bubble_game.resume.y + 25 \
                    and bubble_game.resume.x - 25  <= mouseX <= bubble_game.resume.x + 25:
                    bubble_game.paused = False
                
                elif bubble_game.pause_play_mode.y - 25  <= mouseY <= bubble_game.pause_play_mode.y + 25 \
                    and bubble_game.pause_play_mode.x - 25  <= mouseX <= bubble_game.pause_play_mode.x + 25:
                    bubble_game.mode = 3
                    bubble_game.list_modes.append(bubble_game.mode)
                
                elif bubble_game.instr.y - 25  <= mouseY <= bubble_game.instr.y + 25 \
                and bubble_game.instr.x - 25  <= mouseX <= bubble_game.instr.x + 25:
                    bubble_game.instruction_paused = True
                    
################################## INSTRUCTION SCREEN, MODE 2 ##########################################                 
        
    elif bubble_game.mode == 2: #instruction screen 
        if mouseX>0 and mouseX<100 and mouseY > 470: #back button
            bubble_game.list_modes.pop()
            bubble_game.mode = bubble_game.list_modes[-1]

            
        elif mouseX>650 and mouseX<750 and mouseY > 470: #play button 
            bubble_game.level = 1
            bubble_game.mode = 3 #play game 
            bubble_game.list_modes.append(bubble_game.mode)
    
################################## MODE PLAY SCREEN, MODE 3 ##########################################                 
    
    
    elif bubble_game.mode == 3: # Mode of Play
        play_mode = bubble_game.play_mode 
        mode = bubble_game.play_mode
        if 60 < mouseY < 100:
            bubble_game.play_mode = "CLASSIC"
            bubble_game.classicB.clicked = True
            bubble_game.multiplicationB.clicked = False
            for button in bubble_game.multiplication:
                button.clicked = False

        elif 160 < mouseY < 200:
            bubble_game.play_mode = "MULTIPLICATION_ALL"
            bubble_game.multiplicationB.clicked = True
            bubble_game.classicB.clicked = False
            for button in bubble_game.multiplication:
                button.clicked = False
        elif 300 <= mouseY <= 600:
            numbers = ['1', '5', '9', '2', '6', '10', '3', '7', '11', '4', '8', '12']
            for number in bubble_game.int_to_coord:
                x_coord = bubble_game.int_to_coord[number][0]
                y_coord = bubble_game.int_to_coord[number][1]
                if (x_coord - 20 <= mouseX <= x_coord + 20) and \
                   (y_coord - 20 <= mouseY <= y_coord + 20):
                    bubble_game.play_mode = "MULTIPLICATION" + number
                    index = numbers.index(number)
                    bubble_game.multiplication[index].clicked = True
                    bubble_game.classicB.clicked = False
                    bubble_game.multiplicationB.clicked = False
                    for button in bubble_game.multiplication:
                        if button != bubble_game.multiplication[index]:
                            button.clicked = False

        # Pressing buttons             
        if mouseX>0 and mouseX<100 and mouseY > 470: #back  and resume button
            if bubble_game.paused: # Resume game
                bubble_game.play_mode = play_mode # can't change modes and resume
                bubble_game.mode = 1 # game screen
                bubble_game.paused = False
            else: # Back button
                bubble_game.list_modes.pop()
                bubble_game.mode = bubble_game.list_modes[-1]
                
        elif mouseX>650 and mouseX<750 and mouseY > 470: 
            if bubble_game.paused and not (bubble_game.startButton == 0 and bubble_game.level == 1 and bubble_game.rounds == 1): # choosing names : 
                bubble_game.level = 1
                mode = bubble_game.play_mode
                bubble_game.player.play_again=True #resets game but not player info
                startButton = bubble_game.startButton
                bubble_game.reset()
                bubble_game.did_restart = True
                if startButton > 0:
                    bubble_game.startButton = 1
                elif startButton == 0:
                    bubble_game.startButton = 0
                bubble_game.mode= 1
                bubble_game.bubbles = []
                for i in range(3):
                    bubble_game.bubbles.append(Bubble(Equation(1, bubble_game.terms, bubble_game.play_mode)))
                    bubble_game.change_overlap(bubble_game.bubbles[i], i)
                bubble_game.play_mode = mode
                bubble_game.paused = False
            
            elif not bubble_game.paused: # Play Button
                if bubble_game.player.play_again:
                    bubble_game.bubbles = []
                    for i in range(3):
                        bubble_game.bubbles.append(Bubble(Equation(1, bubble_game.terms, bubble_game.play_mode)))
                        bubble_game.change_overlap(bubble_game.bubbles[i], i)
                bubble_game.level = 1
                bubble_game.mode = 1 #play game 
                bubble_game.list_modes.append(bubble_game.mode)
            
            
################################## SCORE SCREEN, MODE 4 ##########################################                 
            
            
    elif bubble_game.mode == 4: #High score screen
        if 680 <= mouseX <= 736 and 220 <= mouseY <= 275 and bubble_game.scoresTranslate<0:
            bubble_game.triangle_one = "#118325"
            bubble_game.triangle_two= "#3583BC"
            
            bubble_game.scoresTranslate += 100
            
        elif 680 <= mouseX <= 736 and 345 <= mouseY <= 400:
            bubble_game.triangle_two = "#118325"
            bubble_game.triangle_one= "#3583BC"
            bubble_game.scoresTranslate -= 100
            
            if - bubble_game.scoresTranslate == (int(len(bubble_game.infoList)*100)):
                bubble_game.scoresTranslate = 0

        elif  200 < mouseY < 300 and mouseX<500: #Main menu button is pressed 
            bubble_game.player.game=True
            bubble_game.level=1
            bubble_game.player.play_again=False #new player will be playing 
            bubble_game.mode=0  
            bubble_game.scoresTranslate = 0
            bubble_game.list_modes.append(bubble_game.mode)
            bubble_game.reset()
              
        elif mouseY > 310 and mouseX < 500 and bubble_game.play_again_button: # Player want to play again
            bubble_game.level=1
            bubble_game.scoresTranslate = 0
            bubble_game.player.play_again=True #resets game but not player info
            bubble_game.reset()
            bubble_game.startButton=1
            bubble_game.mode = 3
            bubble_game.list_modes.append(bubble_game.mode)
            
        else:
             bubble_game.triangle_one= "#3583BC"
             bubble_game.triangle_two= "#3583BC" 
             
        
################################## GAME OVER SCREEN, MODE 5 ##########################################                 
        
        
    elif bubble_game.mode == 7: #game over screen
        bubble_game.play_again_button = True
        
        if mouseX>50 and mouseX<150: #if player wants to play again 
            bubble_game.level=1
            bubble_game.player.play_again=True #resets game but not player info
            bubble_game.reset()
            bubble_game.startButton=1
            bubble_game.mode= 3
            bubble_game.list_modes.append(bubble_game.mode)
            
        elif mouseX>500 and mouseX<600: # Main Menu
            bubble_game.level=1
            bubble_game.player.game=True
            bubble_game.player.play_again=False
            bubble_game.mode=0    
            bubble_game.reset()
            bubble_game.list_modes.append(bubble_game.mode)
                
        elif mouseY>300 and mouseY<500: #high score screen is pressed 
            bubble_game.mode= 4 #highscore screen 
            bubble_game.list_modes.append(bubble_game.mode)
                
################################## WINNING SCREEN, MODE 6 ##########################################                 
                
    elif bubble_game.mode == 6: #winning screen
        bubble_game.play_again_button = True
        
        if mouseX>50 and mouseX<150: #if player wants to play again 
            bubble_game.level=1
            bubble_game.player.play_again=True #resets game but not player info
            bubble_game.reset()
            bubble_game.startButton=1
            bubble_game.mode= 3
            bubble_game.list_modes.append(bubble_game.mode)
            
        elif mouseX>500 and mouseX<600: # Main Menu
            bubble_game.level=1
            bubble_game.player.game=True
            bubble_game.player.play_again=False
            bubble_game.mode=0    
            bubble_game.reset()
            bubble_game.list_modes.append(bubble_game.mode)
                
        elif mouseY>300 and mouseY<500: #high score screen is pressed 
            bubble_game.mode= 4 #highscore screen 
            bubble_game.list_modes.append(bubble_game.mode)
                
################################## SETTINGS SCREEN, MODE 7 ##########################################                 
                
                
    elif bubble_game.mode == 5: #Settings screen 
        if mouseX>0 and mouseX<100 and mouseY > 475: #back button
            
            bubble_game.list_modes.pop()
            bubble_game.mode = bubble_game.list_modes[-1]
            bubble_game.no.clicked = True
            bubble_game.yes.clicked = False
            
        elif mouseX>650 and mouseX<750 and mouseY > 475: #play button 
            bubble_game.level = 1
            bubble_game.mode = 3 #play game 
            bubble_game.list_modes.append(bubble_game.mode)
            bubble_game.no.clicked = True
            bubble_game.yes.clicked = False
            
        elif bubble_game.on_music.y - 50  <= mouseY <= bubble_game.on_music.y + 50 \
            and bubble_game.on_music.x - 50  <= mouseX <= bubble_game.on_music.x + 50 and not bubble_game.on_music.clicked:
                bubble_game.off_music.clicked = False
                bubble_game.on_music.clicked = True
                file.loop()
        
        elif bubble_game.off_music.y - 50  <= mouseY <= bubble_game.off_music.y + 50 \
            and bubble_game.off_music.x - 50  <= mouseX <= bubble_game.off_music.x + 50 and not bubble_game.off_music.clicked:
               bubble_game.off_music.clicked = True
               bubble_game.on_music.clicked = False
               file.stop()
        
        elif bubble_game.noon.y - 50  <= mouseY <= bubble_game.noon.y + 50 \
            and bubble_game.noon.x - 50  <= mouseX <= bubble_game.noon.x + 50:
               bubble_game.background_theme = "NOON" 
               bubble_game.noon.clicked = True
               bubble_game.sunset.clicked = False
               bubble_game.sunrise.clicked = False 
        elif bubble_game.sunset.y - 50  <= mouseY <= bubble_game.sunset.y + 50 \
            and bubble_game.sunset.x - 50  <= mouseX <= bubble_game.sunset.x + 50:
               bubble_game.background_theme = "SUNSET" 
               bubble_game.noon.clicked = False
               bubble_game.sunset.clicked = True
               bubble_game.sunrise.clicked = False 
               
        elif bubble_game.sunrise.y - 50  <= mouseY <= bubble_game.sunrise.y + 100 \
            and bubble_game.sunrise.x - 50  <= mouseX <= bubble_game.sunrise.x + 50:
               bubble_game.background_theme = "SUNRISE"
               bubble_game.noon.clicked = False
               bubble_game.sunset.clicked = False
               bubble_game.sunrise.clicked = True 
               
        elif bubble_game.yes.y - 50  <= mouseY <= bubble_game.yes.y + 50 \
            and bubble_game.yes.x - 50  <= mouseX <= bubble_game.yes.x + 50:
                bubble_game.erase = True
        if bubble_game.erase:
            if bubble_game.window_yes.y - 50  <= mouseY <= bubble_game.window_yes.y + 50 \
            and bubble_game.window_yes.x - 50  <= mouseX <= bubble_game.window_yes.x + 50:
                bubble_game.window_yes.clicked = True
                bubble_game.window_no.clicked = False
                bubble_game.yes.clicked = True
                bubble_game.no.clicked = False
            
                highscore= open("scores.txt",'w') # ab - appends without adding a new line!!
                highscore.write("")
                highscore.close()
                bubble_game.erase = False
            elif bubble_game.window_no.y - 50  <= mouseY <= bubble_game.window_no.y + 50 \
            and bubble_game.window_no.x - 50  <= mouseX <= bubble_game.window_no.x + 50:
                bubble_game.window_yes.clicked = False
                bubble_game.window_no.clicked = True
                bubble_game.erase = False               
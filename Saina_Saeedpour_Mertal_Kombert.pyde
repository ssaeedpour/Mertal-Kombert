#counted used to time when the sound effects are paused and rewinded
counter = 0    
add_library('minim')    
#the boolean for the instruction screen
instruction_var = False
#the boolean for the start screen
start_bool = True
title_coordinates  = [140,100,220,300]
title_size = [80,40]
titles = ["Mertal   Kombert","Press  SPACE   to   Start","Press   i   For   Instructions","Round   1","Round   2","Round   3","Noob   wins","Kitana   Wins", "Press   Space   to   Play   Again",""]
#Deciding which of the indexed of the list titles i'm going to use in the text option
#This just made it easier to switch out words
title_var = [0,0]
endscrn_var = [0,-700,440]
pic_counts = 0

#KITANA VARIABLES
klistindex = 0
#The counts needed for the animation
kitana_count = -1
#The counts needed to time one animation sequence before I needed it to stop 
kmovecounts = 0
#Booleans used for kitana's movements
kbool = [False,False,False,False,False,False,False,False,False]
#below: X and Y position of the character
kitanax = 650
kitanay = 270
khealth = 350
kinc = [0,1]
kfill = [255,255,255]
kwins = 0
kdelay_var = 40
kkeys = [0,0,0,0,0,0] #UP,LEFT,DOWN,RIGHT,CONTROL,SHIFT 

#NOOB VARIABLES
nlistindex = 0
#The counts needed for the animation
noob_count = -1
#The counts needed to time one animation sequence before I needed it to stop 
nmovecounts = 0
#The booleans used for noob's movements
nbool = [False,False,False,False,False,False,False,False]
#below: X and Y position of the character
noobx = 100
nooby = 270
nhealth = 350
ninc = 0
nfill = [255,255,255]
nwins = 0
ndelay_var = 40
nkeys = [0,0,0,0,0,0] #W,A,S,D,E,R,

def setup():
    global minim,font,kitana,kitana_list,noob,noob_list,back,grass,startscrn,kitana_finish,titles,skull,endscrn
    global theme,kpunch,kjump,kkick,kblock,kwins_audio,npunch,njump,nkick,nblock,nwins_audio,round1,round2,round3,instructions,instruction_background
    size (900,500)
    minim = Minim (this)
    theme = minim.loadFile ("theme.mp3")
    round1 = minim.loadFile ("round1.wav")
    round2 = minim.loadFile ("round2.wav")
    round3 = minim.loadFile ("round3.wav")
    #ALL OF KITANA'S AUDIOS
    kpunch = minim.loadFile ("kpunch.wav")
    kjump = minim.loadFile ("kjump.wav")
    kkick = minim.loadFile ("kkick.wav")
    kblock = minim.loadFile ("kblock.wav")
    kwins_audio = minim.loadFile ("kwins.wav")
    #ALL OF NOOB'S AUDIOS
    npunch = minim.loadFile ("npunch.wav")
    njump = minim.loadFile ("njump.wav")
    nkick = minim.loadFile ("nkick.wav")
    nblock = minim.loadFile ("nblock.wav")
    nwins_audio = minim.loadFile ("nwins.wav")
    frameRate (70)
    instruction_background = loadImage ("instruction_background.jpg")
    instructions = loadImage ("instructions.png")
    kitana = loadImage("kitanasheet.png")
    noob = loadImage("noob.png")
    back = loadImage ("background.png")
    grass = loadImage ("grass.png")
    kitana_finish = loadImage ("kitanabow.png")
    skull = loadImage ("skull.png")
    endscrn = loadImage("blood.png")
    font = createFont ("arcadeclassic.ttf",40)
    
    """So the idea I had with the 'kitana_list' and 'noob_list' was that all of the coordinates and numbers used to animate the images in the same order. That way,
    whenever I wanted to call on a single animation, all I'd have to do was change the index of kitana_list/noob_list and it would automatically input the new numbers into 
    the copy function and it would change the animation"""
    
    """Order of list for kitanra: [0] - count * [1], [2]xcoor on pic, [3]ycoor on pic,[4]cut x,[5]cut y,[6]picwidth, [7]picheight, [8]countmax,
    [9] increment for x position,[10] increment for y position,[11] adjustment collision variable, [12]increment for x position, [13]increment for y position"""
    kitana_list = [[700,30,0,35,80,130,190,5,0,0,0,kitana], #KITANA STAND #copy (kitanasheet, 700 - (count*30),0,35,80,400,300,120,170)
                   [715,48,90,50,80,170,195,8,0,20,0,kitana], #KITANA WALK
                   [520,80,1026,70,90,240,210,4,-20,-1,0,kitana], #KITANA PUNCH
                   [280,48,81,50,80,170,180,2,0,30,0,kitana], #KITANA JUMP
                   [600,60,0,32,84,120,200,2,0,0,0,kitana], #KITANA BLOCK
                   [720,80,496,64,80,210,200,6,-50,0,0,kitana], #KITANA KICK
                   [1043,144,0,79,100,240,250,6,0,-60,0,kitana_finish],#FINISHING MOVE
                   [709,70,890,70,90,200,230,10,-50,10,0,kitana] #DEAD ANIMATION #extra number at the end is the alternate count max    
              ]
    """Order of list for noob: [0] + count * [1], [2]xcoor on pic, [3]ycoor on pic,[4]cut x,[5]cut y,[6]picwidth, [7]picheight, [8]countmax,
    [9] increment for x position,[10] increment for y position,[11] adjustment collision variable, [12]increment for x position,[13]increment for y position """
    noob_list = [[54,93,0,50,130,120,200,3,0,0,0], #STAND 
                 [10,50,120,55,120,115,180,6,0,0,0], #WALK
                 [20,70,240,60,140,160,200,3,0,10,0], #PUNCH #might have to change count number
                 [415,60,120,55,150,130,190,2,0,50,0], #JUMP
                 [290,93,0,50,125,120,185,2,0,10,0], #BLOCK
                 [90,112,580,100,110,210,175,5,-50,20,0], #KICK
                 [30,75,1470,79,115,150,150,7,-50,40,-2],#FINISHING MOVE
                 [-120,110,1030,100,200,250,300,8,-100,30,0,0], #DEAD ANIMATION #extra number at the end is the alternate count max
                 ]
   
    
    
def draw():
    global instruction_background,instructions,instruction_var,theme,endscrn_var,title_var,back,kitana,kitana_count,kitana_list,klistindex,kitanax,kitanay,kbool,kwins,nmovecounts,noob,noob_count,noob_list,nlistindex,noobx, nooby ,nmovecounts,nbool,start_bool,titles,nwins
    background (255)
    theme.play()
    #below: if the start_screen boolean is true, play startscreen, if not, play the main game
    if start_bool == False:
        main_game()
        
    else: 
        startscreen() 
    
    #code below: for the instruction page that comes up when instruction_var == True
    if instruction_var:
            #code needed for the little animations to play
            kitana_counter()
            noob_counter()
            image(instruction_background,0,0,900,500)
            image(instructions,0,0,900,400)
            copy (noob,(noob_count *93)+54,0,50,130,140,15,70,100)
            copy (kitana, 700 - (kitana_count*30),0,35,80,700,10,70,100)
            nlistindex = 0
            klistindex = 0
            textFont (font)
            textSize (32)
            text("Press   b   to   go   back",300,450)
            
            


    
def main_game():
        global instructions,endscrn_var,instruction_var,title_size,title_coordinates,endscrn_var,title_var,back,kitana,kitana_count,kitana_list,klistindex,kitanax,kitanay,kbool,kwins,nmovecounts,noob,noob_count,noob_list,nlistindex,noobx, nooby ,nmovecounts,nbool,start_bool,titles,nwins
        image (back,0,0,1000,500) 
        title_size = [80,60]
        textFont (font)
        textSize(title_size[0]) 
        text (titles[title_var[0]],title_coordinates[0],title_coordinates[1]) #Text for "Round..."
        textSize (title_size[1])
        text (titles[title_var[1]],title_coordinates[2],title_coordinates[3]) #Text for Who wins
        kitana_collision()
        noob_collision()
        
        noob_counter()
        kitana_counter()
        winner()
        
        #THIS IS WHERE THE MAIN COPY FUNCTIONS ARE. Whenever I change the list index, it changes the variables here
        #NOOB COPY
        copy(noob, noob_list[nlistindex][0] + (noob_list[nlistindex][1] * noob_count),noob_list[nlistindex][2],noob_list[nlistindex][3],noob_list[nlistindex][4], noobx + noob_list[nlistindex][8], nooby + noob_list[nlistindex][9],noob_list[nlistindex][5],noob_list[nlistindex][6])
        noob_moves()
        
        #KITANA COPY
        copy(kitana_list[klistindex][11] , kitana_list[klistindex][0] - (kitana_list[klistindex][1] * kitana_count),kitana_list[klistindex][2],kitana_list[klistindex][3],kitana_list[klistindex][4], kitanax + kitana_list[klistindex][8], kitanay + kitana_list[klistindex][9],kitana_list[klistindex][5],kitana_list[klistindex][6])                          
        kitana_moves()
        image (grass,0,endscrn_var[2])
        
        
        
def game_reset(): #This function just resets all the variables to their orignial state
    global start_bool,title_var,title_coordinates,title_size,titles,endscrn_var,pic_counts,round1,round2,round3
    global klistindex,kitana_count,kmovements,kbool,kitanax,kitanay,khealth,kinc,kfill,kwins,kdelay_var,kkeys
    global nlistindex,noob_count,nmovements,nbool,noobx,nooby,nhealth,ninc,nfill,nwins,ndelay_var,nkeys
    counter = 0
    start_bool = True
    title_var = [0,0]
    title_coordinates  = [140,100,220,300]
    title_size = [80,40]
    #titles list size is: 8
    titles = ["Mertal   Kombert","Press   SPACE   to   Start","Press   i   For   Instructions","Round   1","Round   2","Round   3","Noob   wins","Kitana   Wins", "Press   Space   to   Play   Again",""]
    endscrn_var = [0,-500,440]
    pic_counts = 0
    
    #KITANA VARIABLES
    klistindex = 0
    kitana_count = -1
    kmovecounts = 0
    kbool = [False,False,False,False,False,False,False,False,False]
    kitanax = 650
    kitanay = 270
    khealth = 350
    kinc = [0,1]
    kfill = [255,255,255]
    kwins = 0
    kdelay_var = 40
    kkeys = [0,0,0,0,0,0] #UP,LEFT,DOWN,RIGHT,CONTROL,SHIFT 
    
    #NOOB VARIABLES
    nlistindex = 0
    noob_count = -1
    nmovecounts = 0
    nbool = [False,False,False,False,False,False,False,False]
    noobx = 100
    nooby = 270
    nhealth = 350
    ninc = 0
    nfill = [255,255,255]
    nwins = 0
    ndelay_var = 40
    nkeys = [0,0,0,0,0,0] #W,A,S,D,E,R,
    
    
def startscreen(): #Starting title screen
    global startscrn,font,titles,title_var,pic_counts,font,title_coordinates
    title_size = [80,40]
    image (back,0,0,900,500)
    #The words that are going into the title. This is the main title function and I just switch out the text from here
    title_coordinates = [155,100,235,300]
    textFont (font)
    textSize(80)
    text (titles[title_var[0]],title_coordinates[0],title_coordinates[1]) #FIRST LINE OF TITLES
    textSize (40)
    text (titles[title_var[1]],title_coordinates[2],title_coordinates[3]) #SECOND LINE OF TITLES
    textSize(32)
    text(titles[2],240,350) #"INSTRUCTIONS" ON STARTSCREEN
    title_var[0] = 0 #TITLE 1= "MERTAL KOMBERT" FOR STARTSCREEN
    title_var [1] = 1 #TITLE 2 = "PRESS SPACE TO START" FOR STARTSCREEN
    #code below is for the blinking animation that "press space to start" has
    pic_counts += 1 
    delay(50)
    if pic_counts % 20 == 0:
        for n in range (400):
            title_var[1] = 9
    else:
        title_var[1] = 1
    
    
        
def winner():
    global counter,instruction_var,kwins_audio,nwins_audio,round1,round2,round3,kbool,kwins,nwins,skull,title_var,nlistindex,klistindex,noob,noob_count,kitana_count,nmovecounts,kmovecounts,ndelay_var,kdelay_var,endscrn,endscrn_var,kistanax,noobx,titles,title_coordinates
    title_coordinates = [300,200,270,300] #Changes the coordinates of the titles so they're more centered 
    #code below: if one of the players win, a little skull appears underneath the health bar to help keep track of how many rounds each person has won
    if kwins == 1: 
        image (skull,500,35,30,30)
    if nwins == 1:
        image (skull,360,35,30,30)
    if kwins == 2:
        image (skull,500,35,30,30)
        image (skull,550,35,30,30)
        kdelay_var = 150
        image(endscrn,endscrn_var[0],endscrn_var[1],1000,700) #This is where the end screen is called and it'sbrought down
        endscrn_var[1] += 50
        endscrn_var[2] += 50
        if endscrn_var[1] >= 0:
            title_coordinates = [230,100,200,200]
            endscrn_var[1] = 0
            title_var[0] = 7
            title_var[1] = 8
            textFont (font)
            textSize(80)
            text (titles[title_var[0]],title_coordinates[0],title_coordinates[1]) #Display who won
            textSize (40)
            text (titles[title_var[1]],title_coordinates[2],title_coordinates[3]) #Display the "press space to play again"
        kmovecounts += 0.5 #This is for noob's falling animation so that when he gets to the point where he's on the ground, he stays there
        klistindex = 6
        nlistindex = 7
        if kmovecounts > 2: #After this, instead of being animated, noob just has one frame
            noob_count = 5
            

     #Almost exact same code as above but for noob   
    if nwins == 2:
        image (skull,360,35,30,30)
        image(skull,310,35,30,30)
        ndelay_var = 150
        nmovecounts += 0.5
        nlistindex = 6
        klistindex = 7
        if nmovecounts > 2:
            kitana_count = 6
        image(endscrn,endscrn_var[0],endscrn_var[1],1000,700)
        endscrn_var[1] += 50
        endscrn_var[2] += 50
        if endscrn_var[1] >= 0:
            title_coordinates = [270,100,200,200]
            endscrn_var[1] = 0
            title_var[0] = 6
            title_var[1] = 8
            textFont (font)
            textSize(80)
            text (titles[title_var[0]],title_coordinates[0],title_coordinates[1])
            textSize (40)
            text (titles[title_var[1]],title_coordinates[2],title_coordinates[3])

    #Code below: Where the program figures out what round it is and when to play the audio that announces the rounds
    if nwins + kwins == 0: #These variables are changed in the collision functions
        title_var [0] = 3
        counter += 1
        round1.play()
        if counter >= 28:
            round1.pause()
            round1.rewind()
            
    elif nwins + kwins == 1:
        counter = 0
        counter += 1
        round2.play()
        if counter >= 20:
            round2.pause()
            round2.rewind()
        title_var[0] = 4
        
    elif nwins +kwins == 2 and (kwins != 2 or nwins != 2):
        counter = 0
        counter += 1
        round3.play()
        if counter >= 25:
            round3.pause()
            round3.rewind()
        title_var[0] = 5
        
    if kbool[3]:
        title_var[1] = 6
        title_coordinates[2] = 310
        

        
        
        
    
def kitana_counter(): #I put the counted that helps with the animation in functions in case I need to call on them later on
    global kitana_count,kitana_list,klistindex,kdelay_var
    if kitana_count >= kitana_list[klistindex][7]:
        kitana_count = 0 - kitana_list[klistindex][10]
    kitana_count += 1
    delay (kdelay_var)
    

def noob_counter():
    global noob_count,noob_list,nlistindex,ndelay_var
    if noob_count >= noob_list[nlistindex][7]: #noob_list[nlistindex][7]
        noob_count = 0 - noob_list[nlistindex][10]
    noob_count += 1
    delay (ndelay_var) #ndelay_var

    
def kitana_moves(): #This is where all of the actions are regulated
    global klistindex,kitanax,kitanay,kbool,kitana_list,kmovecounts,kitana_count,kinc,kdelay_var,kkeys,kpunch,kjump,kkick,kblock
    """Since processing can't detect two keys pressed at once and I need two keys to be detected at the same time, I used a list that 
    switches between zero and one depending on which key is pressed and so the condition for the action to play out is whether or not 
    that variable is a 1. If it is a 1, then the boolean is true and it allows the action to play out until the boolean is later called false"""
    if kkeys [1] == 1: #KITANA FORWARD
          kbool [4] = True
    if kkeys [3] == 1: #KITANA BACKWARDS
          kbool [5] = True
    if kkeys [0] == 1: #KITANA JUMP
            kbool [0] = True 
    if kkeys [4] == 1: #KITANA PUNCH
            kbool [1] = True
    if kkeys [2] == 1: #KITANA BLOCK
            kbool [6] = True
    if kkeys [5] == 1: #KITANA KICK
            kbool[2] = True
    else:
            klistindex = 0
            
    """The jump code was a bit more complicated than the punch and kick. For those, I just let the booleen stay True until it plays out once
    then I make it false. For jump though, I needed to do it frame by frame. I explain the frames below """        
    if kbool[0]: #JUMP CODE: This code let's the jump animation play out
        kjump.play()  #The first line is always the line that plays the audio for that action
        kitana_counter() 
        kitana_count = 0 #First frame is the squating
        klistindex = 3
        kitanay -= 10 #Her Y position starts rising
        if kitanay < 260: #If her y position starts rising  above here...
            kitana_count = 1 #...the frame changes to her when she is in the air
            kitanay -= 70 #then it starts going back down
        if kitanay < 158: #It goes down to here and then the frame changes back to the squat
            kitana_count = 0
            kitanay = 270 #And finally, the y-position is set back to normal
            kbool[0] = False
        else:
            kjump.rewind() #This is where the audio is rewinded so it can be played again

            
    if kbool [1]: #Lets the punch animation play out once
        kpunch.play()
        kitana_counter()
        klistindex = 2
        kmovecounts += 1 
        if kmovecounts >= 2:
            kmovecounts = 0
            kbool [1] = False
            
        else:
            kpunch.rewind()
        

            
    if kbool[2]: #Lets the kick animation play out once
        kkick.play()
        kitana_counter()
        klistindex = 5
        kdelay_var = 100
        kmovecounts += 1
        if kmovecounts >= 4:
            kmovecounts = 0
            kbool [2] = False
            
        else:
            kkick.rewind()

    
    if kbool [4]: #KITANA FORWARD
        klistindex = 1
        kitanax -= kinc[0]  
        if kitanax < 20:
            kinc[0] = 0
        else:
            kinc[0]= 30
        if keyReleased:
            kbool [4] = False
            
    if kbool [5]: #KITANA BACKWARD 
            klistindex = 1
            kitanax += kinc[0]
            if kitanax > 780:
                kinc[0] = 0
            else:
                kinc[0] = 30
            if keyReleased:
                kbool [5] = False
                
    if kbool [6]: #KITANA BLOCK
        kblock.play()
        klistindex = 4
        kitana_count = 1
        if keyReleased:
            kbool[6] = False
        else:
            kblock.rewind()
    
      
        
            
        
            
    
#the code below is the same as the kitana code except for the variables. Concept wise, it's the exact same
def noob_moves(): 
    global nlistindex,noobx,nooby,nbool,noob_list,nmovecounts,noob_count,ninc,nkeys,npunch,njump,nkick,nblock
    if nkeys [3] == 1: #NOOB FORWARD
            nbool [4] = True
    if nkeys [1] == 1: #NOOB BACKWARDS
            nbool [5] = True
    if nkeys [4] ==1: #NOOB PUNCH
            nbool [1] = True
    if nkeys [0] ==1: #NOOB JUMP
            nbool[0] = True
    if nkeys [2] == 1: #NOOB BLOCK
            nbool [6] = True
    if nkeys [5] == 1: #NOOB KICK
            nbool[2] = True
        
    else:
        nlistindex = 0
        
    #NOOB MOVEMENTS THAT NEED TO PLAY OUT ONCE BEFORE STOPPING
    if nbool[0] == True: #JUMP CODE: This code let's the jump animation play out
        njump.play()
        noob_counter()
        noob_count = 1
        nlistindex = 3
        nooby -= 10
        if nooby < 260:
            noob_count = 2
            nooby -= 65
        if nooby < 130:
            noob_count = 1
            nooby = 270
            nbool[0] = False
        else:
            njump.rewind()

            
    if nbool [1]: #Lets the punch animation play out once
        npunch.play()
        noob_counter()
        nlistindex = 2
        nmovecounts += 1 
        if nmovecounts >= 4:
            nbool [1] = False
            nmovecounts = 0
        else:
            npunch.rewind()

            
    if nbool[2]: #Lets the kick animation play out once
        nkick.play()
        nlistindex = 5
        nmovecounts += 0.5
        if nmovecounts >= 3:
            nbool [2] = False
            nmovecounts = 0
    else:
            nkick.rewind()

            
    if nbool [4]: #NOOB FORWARD
        nlistindex = 1
        noobx += ninc
        if noobx > 790:
            ninc = 0
        else:
            ninc = 30
        if keyReleased:
            nbool [4] = False
            
    if nbool [5]: #NOOB BACKWARDS
            nlistindex = 1
            noobx -= ninc
            if noobx < 0:
                ninc = 0
            else:
                ninc = 30
            if keyReleased:
                nbool [5] = False
                
    if nbool [6]: #NOOB BLOCK
            nblock.play()
            noob_count = 1
            nlistindex = 4  
            if keyReleased:
                nbool [6] = False
    else:
                nblock.rewind()
    
            
        

def kitana_collision ():
    global nwins_audio,title_var,kfill,khealth,nbool,noobx,noob_list,nlistindex,kitanax,kitana_list,klistindex,nwins,kmovecounts,titles,title_coordinates,kdelay_var
    fill (kfill[0],kfill[1],kfill[2])
    rect (500,20,khealth,10)
    """This is where the collision happens. The first variable is the block boolean so that means that if the person isn't blocking and they're within
    a certain distance, then there can be damage done.  """
    if kkeys[2] == 0 and (nbool[1] == True or nbool[2] == True) and ( ( (noobx + noob_list[nlistindex][3]) < (kitanax+ kitana_list[klistindex][3]) ) and ( (noobx + noob_list[nlistindex][3]) > (kitanax - kitana_list[klistindex][3]) ) ):
        khealth -= 50
        kfill = [255,0,0] #The colour changing of the health bar
    else:
        kfill = [255,255,255]
    if khealth <= 0: #If the health bar has a width of less than 0...
        kitanax = 650 #Move the characters back to their original positions
        noobx = 100
        kbool [3] = True #"Activate" the animations
        khealth = 0 #Make sure the health bar doesn't go into the negatives
    if kbool[3]: 
        nwins_audio.play()
        khealth += 70
        klistindex = 7
        kmovecounts += 0.25
        kdelay_var = 140
        if kmovecounts >= 4:
            klistindex = 0
        if khealth >=350:
            nwins_audio.rewind()
            khealth = 350
            kdelay_var = 40
            kmovecounts = 0
            nwins += 1
            kitanax = 600
            nwins_audio.pause()
            kbool[3] = False
        
        
        
    
        
    
    
    
def noob_collision():
    global kwins_audio,nhealth,kbool,kitanax,kitana_list,klistindex,kitana_count,noobx,noob_listindex,nlistindex,nfill,kwins,ndelay_var,kdelay_var,titles,nmovecounts,nbool,title_var,noobx,kitanax
    title_var[1] = 9
    title_coordinates[2] = 500
    title_coordinates[3] = 200
    fill (nfill[0],nfill[1],nfill[2])
    rect(40,20,nhealth,10)
    if nkeys[2] == 0 and  (kbool[1] == True or kbool[2] == True) and ( ( (noobx + noob_list[nlistindex][3]) < (kitanax+ kitana_list[klistindex][3]) ) and ( (noobx + noob_list[nlistindex][3]) > (kitanax - kitana_list[klistindex][3]) ) ):
        nhealth -=  50
        nfill = [255,0,0]
    else:
        nfill = [255,255,255]
        
    if nhealth <= 0:
        kitanax = 650
        noobx = 100
        nhealth = 0
        nbool [3] = True
    if nbool[3]:
        kwins_audio.play()
        title_var[1] = 7
        nbool [4] =False
        nhealth += 70
        nlistindex = 7
        nmovecounts += 0.5
        if nmovecounts >= 3.30:
            nlistindex = 0
            kwins_audio.pause()
        if nhealth >=350:
            nhealth = 350
            nmovecounts = 0
            kwins += 1
            kwins_audio.rewind()
            nbool[3] = False
    
    
        
def keyPressed():
    global nkeys,kkeys,start_bool,nwins,kwins,round1,round2,round3,instruction_var
    if keyCode == UP:
        kkeys[0] = 1
    if keyCode == LEFT:
        kkeys[1] = 1
    if keyCode == DOWN:
        kkeys[2] = 1
    if keyCode == RIGHT:
        kkeys[3] = 1
    if keyCode == CONTROL:
        kkeys[4] = 1
    if keyCode == SHIFT:
        kkeys[5] = 1
    if key == "w":
        nkeys[0] = 1
    if key == "a":
        nkeys[1] = 1
    if key == "s":
        nkeys[2] = 1
    if key == "d":
        nkeys[3] = 1
    if key == "e":
        nkeys[4] = 1
    if key == "r":
        nkeys[5] = 1
        

    if key == " " and start_bool == True:
        start_bool = False
    
    
    if key == " " and endscrn_var[1] >= 0 and instruction_var == False:
        start_bool = True
        game_reset()
        
    if key == "i":
        instruction_var = True
    if key == "b" and instruction_var == True:
        instruction_var = False

    

    
        
    
        
    
def keyReleased():
    global nkeys,kkeys
    if keyCode == UP:
        kkeys[0] = 0
    if keyCode == LEFT:
        kkeys[1] = 0
    if keyCode == DOWN:
        kkeys[2] = 0
    if keyCode == RIGHT:
        kkeys[3] = 0
    if keyCode == CONTROL:
        kkeys[4] = 0
    if keyCode == SHIFT:
        kkeys[5] = 0
    if key == "w":
        nkeys[0] = 0
    if key == "a":
        nkeys[1] = 0
    if key == "s":
        nkeys[2] = 0
    if key == "d":
        nkeys[3] = 0
    if key == "e":
        nkeys[4] = 0
    if key == "r":
        nkeys[5] = 0
    
    
    

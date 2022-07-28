import turtle as tr
from random import randrange
import time

#tbg = turtle.Screen()
#tbg.bgcolor("black")
#tbg.title("Arda's Snake & Ladder")


    # Board coordinates set for easier placement

skor1 = 0
skor2 = 0


Xtab = [-150, -50, 50, 150, 250,
            250, 150, 50, -50, -150,
            -150, -50, 50, 150, 250,
            250, 150, 50, -50, -150,
            -150, -50, 50, 150, 250,
            250,250,250,250,250]
    
Ytab = [-250, -250, -250, -250, -250,
            -150, -150, -150, -150, -150,
            -50, -50, -50, -50, -50,
            50, 50, 50, 50, 50,
            150, 150, 150, 150, 150
            ,150, 150, 150, 150, 150]

swan = {
  "1": "monkey",
  "2": "cow",
  "3": "bull",
  "4": "camel",
  "5": "lion"
}
    


def main():

    global skor1
    global skor2

    tr.setup(800,800,0 ,0)              # Main setup, window etc. is being setup alongside turtles
    tr.title("Arda's Snake & Ladder")

    t1 = tr.Turtle()
    t2 = tr.Turtle()

    tr.bgcolor("#253247")

    t1.fillcolor("red")
    t2.fillcolor("blue")
    t1.pendown()
    t2.pendown()
    t1.pensize(2)
    t2.pensize(2)
    t2.pencolor("#c22c1b")
    t1.pencolor("#c22c1b")

    t1.speed(10)            # Drawing begins :3
    t2.speed(10)
    
    t1.forward(300)
    t1.right(90)
    t1.forward(300)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(500)

    for i in range(2):
        
        t1.left(90)
        t1.forward(100)
        t1.left(90)
        t1.forward(500)
        t1.right(90)
        t1.forward(100)
        t1.right(90)
        t1.forward(500)


    t2.forward(300)
    t2.left(90)
    t2.forward(200)
    t2.left(90)
    t2.forward(500)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(500)

    for i in range(2):
        
        t2.right(90)
        t2.forward(100)
        t2.right(90)
        t2.forward(500)
        t2.left(90)
        t2.forward(100)
        t2.left(90)
        t2.forward(500)
    
    t2.penup()
    t1.penup()
    
    t2.left(90)
    t2.forward(70)
    t2.left(90)
    t2.forward(470)


    # Adding numbers, on each line they are done in a 5 times loop with helvetica font style

    t2.pencolor("#e3e3e3")

    for i in range(1, 26):
        sy = str(i)
        t2.goto(Xtab[i-1],Ytab[i-1])
        t2.write(sy, True, align="center", font=("Calibri", 18, "bold", "italic"))

    #Now our objects will be created as turtles.
    # each will use a single object to 

    
    tl1 = tr.Turtle()
    tl1.penup()
    tr.addshape("ladder1.gif")
    tl1.shape("ladder1.gif")
    tl1.goto(30,90)

    tl2 = tr.Turtle()
    tl2.penup()
    tr.addshape("ladder2.gif")
    tl2.shape("ladder2.gif")
    tl2.goto(-90,-100)

    tl3 = tr.Turtle()
    tl3.penup()
    tr.addshape("ladders.gif")
    tl3.shape("ladders.gif")
    tl3.goto(265,-170)

    tl4 = tr.Turtle()
    tl4.penup()
    tr.addshape("snake3.gif")
    tl4.shape("snake3.gif")
    tl4.goto(-170,-120)

    tl5 = tr.Turtle()
    tl5.penup()
    tr.addshape("snake2.gif")
    tl5.shape("snake2.gif")
    tl5.goto(50,-200)

    tl6 = tr.Turtle()
    tl6.penup()
    tr.addshape("snake.gif")
    tl6.shape("snake.gif")
    tl6.goto(130,40)

    # Scoring is defined

    
    #kor1s = str(skor1)
  #  skor2s = str(skor2)
   # print("Player 1: ", skor1s, "Player 2: ", skor2s)
    #score= Player 1': skor1s
     #      Player 2: skor2s
    
    t0 = tr.Turtle()
    tc = tr.Turtle()
    t0.penup()
    tc.penup()

    t2.goto(170, 320)
    t2.pendown()
 #   t2.write(score, True, align="center", font=("Calibri", 20, "bold", "italic"))
    

    tr.addshape("at.gif")
    t1.shape("at.gif")
    t1.forward(100)


    uh = tr.Turtle()
    tr.addshape("at2.gif")
    uh.shape("at2.gif")
    uh.penup()
    uh.forward(200)
    uh.left(90)
    uh.forward(240)


    def gameplay():

        global skor1
        global skor2
       
        pos1=1
        pos2=1

        # Added two other character selection, Monkey and Lion respectively!

        t0.goto(Xtab[pos1-1],Ytab[pos1-1])
        animal1c = str(input("Which character do you want for first player? {Monkey, Cow, Bull, Camel or Lion} Enter 1, 2, 3, 4 or 5"))
        animal1 = (swan[animal1c])
        
        tr.addshape(animal1 +".gif")
        t0.shape(animal1 +".gif")

        tc.goto(Xtab[pos2-1],Ytab[pos2-1])
        animal2c = str(input("Which character do you want for second player? {Monkey, Cow, Bull, Camel or Lion} Enter 1, 2, 3, 4 or 5"))
        animal2 = (swan[animal2c])
        
        tr.addshape(animal2 +".gif")
        tc.shape(animal2 +".gif")
    
        animal1 = animal1.capitalize()
        animal2 = animal2.capitalize()
    
        zar = tr.Turtle()
        zar.penup()
        zar.forward(-300)

        for i in range(1, 7):
            tr.addshape(str(i) + ".gif") # Dice is being set here

        winner = tr.Turtle()            # Winning prompt is set here
        tr.addshape("win.gif")
        winner.shape("win.gif")
        winner.ht()
    
        while pos1 < 25 and pos2 < 25:
        
            input("Press Enter to roll dice for player 2!")
            pos1r = (randrange(1,6))
            zar.shape(str(pos1r)+".gif")
            print("You roll" + " " + str(pos1r))
            pos1 = pos1 + pos1r 
        
           # print(t0.pos())


            yuru = pos1r
            yu1 = pos1 - pos1r
            for i in range(yuru): 
                t0.setpos(Xtab[yu1 + i], Ytab[yu1 + i])
                time.sleep(0.4)
            
            if pos1 == 5:                               #Ladders and Snakes are here, transportation according to array
                pos1 = 15
                print(animal1 + " used the ladder")
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 8:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 3
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 9:
                print(animal1 + " used the ladder")
                pos1 = 12
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 18:
                print(animal1 + " used the ladder")
                pos1 = 23
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 20:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 1
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 24:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 14
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])

            print(animal1 + " is at position " + str(pos1))

            if pos1 > 24:
                skor1 = skor1 + 1
                winner.st()
                print("Scores", skor1, ' : ', skor2)
                ceap = str(input("Wanna play again? y or n"))
                ceap = ceap.capitalize()
                if  ceap == "Y":
                    winner.ht()
                    gameplay()
                if ceap == "N":
                    exit()

            input("Press Enter to roll dice for player 2!")
            pos2r = (randrange(1,6))
            zar.shape(str(pos2r)+".gif")
            print("You roll" +  " " + str(pos2r))
            pos2 = pos2 + pos2r
        
        
            #print(tc.pos())
            yuru2 = pos2r
            yu2 = pos2 - pos2r 
            for i in range(yuru2): 
                tc.setpos(Xtab[yu2 + i], Ytab[yu2 + i])
                time.sleep(0.4)


            if pos2 == 5:
                print(animal2 + " used the ladder")
                pos2 = 15
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 8:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 3
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 9:
                print(animal2 + " used the ladder")
                pos2 = 12
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 18:
                print(animal2 + " used the ladder")
                pos2 = 23
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 20:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 1
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 24:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 14
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])

            print(animal2 + " is at position " + str(pos2))

            
            if pos2 > 24 and pos1 < 25:
                skor2 = skor2 + 1
            
            if pos1 > 24 or pos2 > 24:
                winner.st()
                print("Scores", skor1, ' : ', skor2)
                ceap = str(input("Wanna play again? y or n"))
                ceap = ceap.capitalize()
                if  ceap == "Y":
                    winner.ht()
                    gameplay()
                if ceap == "N":
                    exit()
    gameplay()
            

main()


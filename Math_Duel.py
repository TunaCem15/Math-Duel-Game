from turtle import *
from random import *
from time import *
from pygame import mixer
mixer.init()
win = mixer.Sound("win.wav")
lose = mixer.Sound("loss audio 2.wav")
mixer.music.load("background_math.mp3")
turn = randint(1,3)
gameturn = 0
p1_score = 0
p2_score = 0
p3_score = 0
hideturtle()
main = Turtle()
p1 = Turtle()
p2 = Turtle()
p3 = Turtle()
e_f = Turtle()
e_p = Turtle()
e_b = Turtle()
n_f = Turtle()
n_p = Turtle()
n_b = Turtle()
h_f = Turtle()
h_p = Turtle()
h_b = Turtle()
op1 = Turtle()
op2 = Turtle()
op3 = Turtle()
op4 = Turtle()
op1.speed(3000)
op2.speed(3000)
op3.speed(3000)
op4.speed(3000)
turn_t = Turtle()
turn_t.speed(3000)
timer = Turtle()
timer.speed(3000)
warn = Turtle()
warn.speed(3000)
warn.color("white")
warn.penup()
warn.goto(-700,0)
back = Turtle()
back.speed(3000)
back.penup()
back.shapesize(4)
back.shape("square")
back.color("red")
back.goto(575,-270)
p1_item = Turtle()
p2_item = Turtle()
p3_item = Turtle()
p1.hideturtle()
p2.hideturtle()
p3.hideturtle()
e_f.hideturtle()
e_p.hideturtle()
e_b.hideturtle()
n_f.hideturtle()
n_p.hideturtle()
n_b.hideturtle()
h_f.hideturtle()
h_p.hideturtle()
h_b.hideturtle()
p1_turn = Turtle()
p2_turn = Turtle()
p3_turn = Turtle()
p1_turn.hideturtle()
p2_turn.hideturtle()
p3_turn.hideturtle()
op1.hideturtle()
op2.hideturtle()
op3.hideturtle()
op4.hideturtle()
turn_t.hideturtle()
timer.hideturtle()
warn.hideturtle()
back.hideturtle()
main_screen = getscreen()
main_screen.title("Math Duel")
main_screen.bgcolor("aquamarine")
current_screen = "main"
selected_q_difficulty = None
easy_func = 3
easy_poly = 3
easy_bi = 3
normal_func = 3
normal_poly = 3
normal_bi = 3
hard_func = 3
hard_poly = 3
hard_bi = 3
total_q = 27
time = 0
player_1_time_spent = 0
player_2_time_spent = 0
player_3_time_spent = 0
q_end = False
lqc = None
player_1_item = None
player_2_item = None
player_3_item = None
Extrap_1 = False
Extrap_2 = False
Extrap_3 = False
Multiplier_1 = False
Multiplier_2 = False
Multiplier_3 = False
a_list = list()
ef_list = list()
ep_list = list()
eb_list = list()
nf_list = list()
np_list = list()
nb_list = list()
hf_list = list()
hp_list = list()
hb_list = list()
ef_1list = ["If f(x) = x^2 + 3x -5, what is f(5) equal to?",15,20,25,35]
ef_2list = ["If f: R - {a} -> R and f(x) = 5x+3/3x-15, what is a equal to?",3,15,-5,5]
ef_3list = ["If f(x) is a constant function, what is f(5) + f(1) / f(9138) equal to?",5,1523,-2,2]
ef_list.append(ef_1list)
ef_list.append(ef_2list)
ef_list.append(ef_3list)
ep_1list = ["P(x) = (2a-6)x^5-4x^(b+2) + 3x^2 - 7 If the degree of the given polynomial is 4, what is the sum of a+b?",15,10,25,5]
ep_2list = ["If P(x) = 3x^2 -5x +2 , Q(x) = 2x^2 -3x -4, what is the coefficent of the x^3 term upon their multiplication?",19,0,-5,-19]
ep_3list = ["If (x+a)*(bx+3) = 2x^2 -3x -9, what is the sum of a+b?",1,0,2,-1]
ep_list.append(ep_1list)
ep_list.append(ep_2list)
ep_list.append(ep_3list)
eb_1list = ["If the expression (5x-7y)^n has 15 terms, what is n equal to?",-15,-14,15,14]
eb_2list = ["What is the constant term of (2x-5y+3)^4?",12,-12,-81,81]
eb_3list = ["What is the constant term of (x  -  2/√x)^6?",60,40,120,240]
eb_list.append(eb_1list)
eb_list.append(eb_2list)
eb_list.append(eb_3list)
nf_1list = ["f is a linear function. If f(5) = -7 and f(2) = 11, what is f(0)?",-19,19,-23,23]
nf_2list = ["If f(x) = x-2/3 and g(x) = 2x-9/3 , what is (3f-g)(3)?",0,1,-1,2]
nf_3list = ["If f: R - {-2/3} -> R - {a} and f(x) = 9x+1/3x+2, what is a?",5,12,9,3]
nf_list.append(nf_1list)
nf_list.append(nf_2list)
nf_list.append(nf_3list)
np_1list = ["P(x) = x^3 + 5x - 2, Q(x) = x + 3. What is the remainder R(x) polynomial upon the division of P(x) by Q(x)?",22,11,44,-44]
np_2list = ["If deg[P(x)/Q(x)] = 4 and deg[P(x)]/deg[Q(x)] = 3 what is deg[P(x)]?",3,2,5,6]
np_3list = ["P(x) = x^2 -3√2*x + 4. What is the remainder upon dividing the given polynomial with x - √2?",1,-1,4,0]
np_list.append(np_1list)
np_list.append(np_2list)
np_list.append(np_3list)
nb_1list = ["(3x^4 - 2y^3)^n. If the expansion of the given expression includes the term A*x^8*y^15, what number is n equal to?",5,6,8,7]
nb_2list = ["(3x^2 + 2)^(n+12). If the constant term of the expansion of the given expression is 4^(2n-3), what is n equal to?",3,7,4,6]
nb_3list = ["(x^3-2y^2)^6 = x^18-...+ A * x^p * y^k +... If the sum of p and k is 13 in the given equality, what is A equal to?",192,-180,-224,-192]
nb_list.append(nb_1list)
nb_list.append(nb_2list)
nb_list.append(nb_3list)
hf_1list = ["If f(1-3x) = 3x+4 and g(-x+3) = 5, what is (fog)(1) equal to?",5,4,-4,-5]
hf_2list = ["4-(fog)(x)/g(x)+1 = x-2. If f(x) = 3x-2/5, what is g(0) equal to?",-5,5,"32/7","-32/7"]
hf_3list = ["If f,g: R -> R, g(x) = 3x-5 and (fog^-1)^(-1)(x) = 6x-17: find the f(x) function.","-x+4/2","x-4/2","x+16/2","x+4/2"]
hf_list.append(hf_1list)
hf_list.append(hf_2list)
hf_list.append(hf_3list)
hp_1list = ["If the P(x) = x^4 + (3a+1)x^3 + 9x^2 + bx + 2 polynomial is fully divisible by (x+1)^3, what is a*b equal to?",-14,7,-7,14]
hp_2list = ["If deg[P(x)] = 3 and If the given polynomial is fully divisible by 2x-1,x+4 and x+1, what is P(8)/P(3) equal to?",5,-9,3,18]
hp_3list = ["If P(x) = x^2014 + x^2013 + 3, what is the remainder upon the division between the given polynomial and x^2 - x + 1?","x-2","2+x","-2+x","2-x"]
hp_list.append(hp_1list)
hp_list.append(hp_2list)
hp_list.append(hp_3list)
hb_1list = ["Given the expansion of (√a+b)^n in terms of the decreasing powers of a, the coefficient of the fourth-to-last term is equal to the coefficient of the fifteenth-to-last term. What is the value of n?",15,16,18,17]
hb_2list = ["What is the middle term in the expansion of the expression (2x - 1/√x)^4?",24,"-24x^2","24/x","24x"]
hb_3list = ["a is a real number. (2x - 6y + a -4)^4. If the sum of the given expression's expansion's term's coefficents are equal to the constant term, what is a equal to?",2,3,5,6]
hb_list.append(hb_1list)
hb_list.append(hb_2list)
hb_list.append(hb_3list)
chosen_q = None
chosen_q_class = None
def drawplayeritem1(a):
    if a == "Extrap":
        p1_item.write("+1", font = ("Arial",30,"normal"))
    elif a == "Multiplier":
        p1_item.write("x2", font = ("Arial",30,"normal"))
    elif a == "Thief":
        p1_item.write("T", font = ("Arial",30,"normal"))
    else:
        pass
def drawplayeritem2(a):
    if a == "Extrap":
        p2_item.write("+1", font = ("Arial",30,"normal"))
    elif a == "Multiplier":
        p2_item.write("x2", font = ("Arial",30,"normal"))
    elif a == "Thief":
        p2_item.write("T", font = ("Arial",30,"normal"))
    else:
        pass
def drawplayeritem3(a):
    if a == "Extrap":
        p3_item.write("+1", font = ("Arial",30,"normal"))
    elif a == "Multiplier":
        p3_item.write("x2", font = ("Arial",30,"normal"))
    elif a == "Thief":
        p3_item.write("T", font = ("Arial",30,"normal"))
    else:
        pass
def turnonextrap():
    global Extrap_1,Extrap_2,Extrap3,player_1_item,player_2_item,player_3_item,turn, current_screen
    if current_screen != "main":
        warn.write("You can't use an Extrap now!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
    elif turn == 1:
        if player_1_item == "Extrap":
            Extrap_1 = True
            player_1_item = None
            p1_item.clear()
        else:
            warn.write("You don't have an Extrap!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    elif turn == 2:
        if player_2_item == "Extrap":
            Extrap_2 = True
            player_2_item = None
            p2_item.clear()
        else:
            warn.write("You don't have an Extrap!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    else:
        if player_3_item == "Extrap":
            Extrap_3 = True
            player_3_item = None
            p3_item.clear()
        else:
            warn.write("You don't have an Extrap!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
def turnonmultiplier():
    global Multiplier_1,Multiplier_2,Multiplier_3,player_1_item,player_2_item,player_3_item,turn, current_screen
    if current_screen != "main":
        warn.write("You can't use a Multiplier now!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
    if turn == 1:
        if player_1_item == "Multiplier":
            Multiplier_1 = True
            player_1_item = None
            p1_item.clear()
        else:
            warn.write("You don't have a Multiplier!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    elif turn == 2:
        if player_2_item == "Multiplier":
            Multiplier_2 = True
            player_2_item = None
            p2_item.clear()
        else:
            warn.write("You don't have a Multiplier!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    else:
        if player_3_item == "Multiplier":
            Multiplier_3 = True
            player_3_item = None
            p3_item.clear()
        else:
            warn.write("You don't have a Multiplier!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
def thief():
    global turn,player_1_item,player_2_item,player_3_item,p1_name,p2_name,p3_name, current_screen
    if current_screen != "main":
        warn.write("You can't use a Thief now!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
    if turn == 1:
        if player_1_item == "Thief":
            warn.write("Check the console, please", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
            a = input("What player do you want to use Thief on? Write their player number.")
            if a == "1":
                print("You can't steal from yourself! Get out!")
            elif a == "2":
                if player_2_item != None:
                    print("Stole ",p2_name + "'s",player_2_item+".")
                    player_1_item = player_2_item
                    player_2_item = None
                    p1_item.clear()
                    p2_item.clear()
                    drawplayeritem1(player_1_item)
                    drawplayeritem2(player_2_item)
                else:
                    print(p2_name,"Doesn't have an item.")
            elif a == "3":
                if player_3_item != None:
                    print("Stole ",p3_name + "'s",player_3_item+".")
                    player_1_item = player_3_item
                    player_3_item = None
                    p1_item.clear()
                    p3_item.clear()
                    drawplayeritem1(player_1_item)
                    drawplayeritem3(player_3_item)
                else:
                    print(p3_name,"Doesn't have an item.")
            else:
                print("Invalid response.")
        else:
            warn.write("You don't have a Thief!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    elif turn == 2:
        if player_2_item == "Thief":
            warn.write("Check the console, please", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
            a = input("What player do you want to use Thief on? Write their player number.")
            if a == "2":
                print("You can't steal from yourself! Get out!")
            elif a == "1":
                if player_1_item != None:
                    print("Stole ",p1_name + "'s",player_1_item+".")
                    player_2_item = player_1_item
                    player_1_item = None
                    p1_item.clear()
                    p2_item.clear()
                    drawplayeritem1(player_1_item)
                    drawplayeritem2(player_2_item)
                else:
                    print(p1_name,"Doesn't have an item.")
            elif a == "3":
                if player_3_item != None:
                    print("Stole ",p3_name + "'s",player_3_item+".")
                    player_2_item = player_3_item
                    player_3_item = None
                    p2_item.clear()
                    p3_item.clear()
                    drawplayeritem2(player_2_item)
                    drawplayeritem3(player_3_item)
                else:
                    print(p3_name,"Doesn't have an item.")
            else:
                print("Invalid response.")
        else:
            warn.write("You don't have a Thief!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
    else:
        if player_3_item == "Thief":
            warn.write("Check the console, please", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
            a = input("What player do you want to use Thief on? Write their player number.")
            if a == "3":
                print("You can't steal from yourself! Get out!")
            elif a == "2":
                if player_2_item != None:
                    print("Stole ",p2_name + "'s",player_2_item+".")
                    player_3_item = player_2_item
                    player_2_item = None
                    p2_item.clear()
                    p3_item.clear()
                    drawplayeritem2(player_2_item)
                    drawplayeritem3(player_3_item)
                else:
                    print(p2_name,"Doesn't have an item.")
            elif a == "1":
                if player_1_item != None:
                    print("Stole ",p1_name + "'s",player_1_item+".")
                    p1_item.clear()
                    p3_item.clear()
                    player_3_item = player_1_item
                    player_1_item = None
                    drawplayeritem3(player_3_item)
                else:
                    print(p1_name,"Doesn't have an item.")
            else:
                print("Invalid response.")
        else:
            warn.write("You don't have a Thief!", font = ("Arial",40,"normal"))
            sleep(1)
            warn.clear()
def rewarditem():
    global turn,player_1_item,player_2_item,player_3_item
    a = randint(1,2)
    if a == 2:
        pass
    else:
        b = randint(1,3)
        if b == 1:
            if turn == 1:
                if player_1_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_1_item}. Would you like to swap your item with the Extrap? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Extrap. Good luck with the remainder of your game!")
                        player_1_item = "Extrap"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 1 has received the Extrap!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_1_item = "Extrap"
            elif turn == 2:
                if player_2_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_2_item}. Would you like to swap your item with the Extrap? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Extrap. Good luck with the remainder of your game!")
                        player_2_item = "Extrap"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 2 has received the Extrap!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_2_item = "Extrap"
            elif turn == 3:
                if player_3_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_3_item}. Would you like to swap your item with the Extrap? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Extrap. Good luck with the remainder of your game!")
                        player_3_item = "Extrap"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 3 has received the Extrap!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_3_item = "Extrap"
                                
        elif b == 2:
            if turn == 1:
                if player_1_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_1_item}. Would you like to swap your item with the Multiplier? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Multiplier. Good luck with the remainder of your game!")
                        player_1_item = "Multiplier"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 1 has received the Multiplier!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_1_item = "Multiplier"
            elif turn == 2:
                if player_2_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_2_item}. Would you like to swap your item with the Multiplier? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Multiplier. Good luck with the remainder of your game!")
                        player_2_item = "Multiplier"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 2 has received the Multiplier!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_2_item = "Multiplier"
            elif turn == 3:
                if player_3_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_3_item}. Would you like to swap your item with the Multiplier? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Multiplier. Good luck with the remainder of your game!")
                        player_3_item = "Multiplier"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 3 has received the Multiplier!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_3_item = "Multiplier"
        else:
            if turn == 1:
                if player_1_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_1_item}. Would you like to swap your item with the Thief? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Thief. Good luck with the remainder of your game!")
                        player_1_item = "Thief"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 1 has received the Thief!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_1_item = "Thief"
            elif turn == 2:
                if player_2_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_2_item}. Would you like to swap your item with the Thief? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Thief. Good luck with the remainder of your game!")
                        player_2_item = "Thief"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 2 has received the Thief!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_2_item = "Thief"
            elif turn == 3:
                if player_3_item != None:
                    warn.write("Check the console, please.",font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    itemq = input(f"You already have the item {player_3_item}. Would you like to swap your item with the Thief? Respond with y to confirm swap.")
                    if itemq == "y":
                        print("Your former item has been swapped for the Thief. Good luck with the remainder of your game!")
                        player_3_item = "Thief"
                    else:
                        print("You will keep your item. Good luck with the rest of your game!")
                else:
                    warn.write("Player 3 has received the Thief!", font = ("Arial",40,"normal"))
                    sleep(1)
                    warn.clear()
                    player_3_item = "Thief"
def editscore():
    global turn,selected_q_difficulty,gameturn, lqc,p1_score,p2_score,p3_score,Extrap_1,Multiplier_1,Extrap_2,Multiplier_2,Extrap_3,Multiplier_3
    if lqc == True:
        if turn == 1:
            if selected_q_difficulty == "easy":
                if Extrap_1 == True or Multiplier_1 == True:
                    p1_score += 2
                    if Extrap_1 == True:
                        Extrap_1 = False
                    elif Multiplier_1 == True:
                        Multiplier_1 = False
                else:
                    p1_score += 1
            elif selected_q_difficulty == "normal":
                if Extrap_1 == True:
                    p1_score += 3
                    Extrap_1 = False
                elif Multiplier_1 == True:
                    p1_score += 4
                    Multiplier_1 = False
                else:
                    p1_score += 2
            elif selected_q_difficulty == "hard":
                if Extrap_1 == True:
                    p1_score += 4
                    Extrap_1 = False
                elif Multiplier_1 == True:
                    p1_score += 6
                    Multiplier_1 = False
                else:
                    p1_score += 3
        elif turn == 2:
            if selected_q_difficulty == "easy":
                if Extrap_2 == True or Multiplier_2 == True:
                    p2_score += 2
                    if Extrap_2 == True:
                        Extrap_2 = False
                    elif Multiplier_2 == True:
                        Multiplier_2 = False
                else:
                    p2_score += 1
            elif selected_q_difficulty == "normal":
                if Extrap_2 == True:
                    p2_score += 3
                    Extrap_2 = False
                elif Multiplier_2 == True:
                    p2_score += 4
                    Multiplier_2 = False
                else:
                    p2_score += 2
            elif selected_q_difficulty == "hard":
                if Extrap_2 == True:
                    p2_score += 4
                    Extrap_2 = False
                elif Multiplier_2 == True:
                    p2_score += 6
                    Multiplier_2 = False
                else:
                    p2_score += 3
        else:
            if selected_q_difficulty == "easy":
                if Extrap_3 == True or Multiplier_3 == True:
                    p3_score += 2
                    if Extrap_3 == True:
                        Extrap_3 = False
                    elif Multiplier_3 == True:
                        Multiplier_3 = False
                else:
                    p3_score += 1
            elif selected_q_difficulty == "normal":
                if Extrap_3 == True:
                    p3_score += 3
                    Extrap_3 = False
                elif Multiplier_3 == True:
                    p3_score += 4
                    Multiplier_3 = False
                else:
                    p3_score += 2
            elif selected_q_difficulty == "hard":
                if Extrap_3 == True:
                    p3_score += 4
                    Extrap_3 = False
                elif Multiplier_3 == True:
                    p3_score += 6
                    Multiplier_3 = False
                else:
                    p3_score += 3
    elif lqc == False:
        if turn == 1:
            if selected_q_difficulty == "easy":
                if Multiplier_1 == True:
                    p1_score -= 3
                    Multiplier_1 = False
                else:
                    pass
            elif selected_q_difficulty == "normal":
                if Multiplier_1 == True:
                    p1_score -= 2
                    Multiplier_1 = False
                else:
                    pass
            elif selected_q_difficulty == "hard":
                if Multiplier_1 == True:
                    p1_score -= 3
                    Multiplier_1 = False
                else:
                    pass
            if Extrap_1 == True:
                Extrap_1 = False
        elif turn == 2:
            if selected_q_difficulty == "easy":
                if Multiplier_2 == True:
                    p2_score -= 3
                    Multiplier_2 = False
                else:
                    pass
            elif selected_q_difficulty == "normal":
                if Multiplier_2 == True:
                    p2_score -= 2
                    Multiplier_2 = False
                else:
                    pass
            elif selected_q_difficulty == "hard":
                if Multiplier_2 == True:
                    p2_score -= 3
                    Multiplier_2 = False
                else:
                    pass
            if Extrap_2 == True:
                Extrap_2 = False
        elif turn == 3:
            if selected_q_difficulty == "easy":
                if Multiplier_3 == True:
                    p3_score -= 3
                    Multiplier_3 = False
                else:
                    pass
            elif selected_q_difficulty == "normal":
                if Multiplier_3 == True:
                    p3_score -= 2
                    Multiplier_3 = False
                else:
                    pass
            elif selected_q_difficulty == "hard":
                if Multiplier_3 == True:
                    p3_score -= 3
                    Multiplier_3 = False
                else:
                    pass
            if Extrap_3 == True:
                Extrap_3 = False
    else:   
        pass
    gameturn += 1
def tick(a):
    global q_end, player_1_time_spent, player_2_time_spent, player_3_time_spent
    while q_end == False:
        if a == 0:
            timer.write(a, font = ("Arial",25,"normal"))
        sleep(1)
        timer.clear()
        a += 1
        timer.write(a, font = ("Arial",25,"normal"))
        if q_end == True:
            break
    if turn == 1:
        player_1_time_spent += a
    elif turn == 2:
        player_2_time_spent += a
    else:
        player_3_time_spent += a
    a == 0
def turncolor():
    global turn,gameturn
    if gameturn == 0:
        if turn == 1:
            p1_turn.color("green")
            p2_turn.color("red")
            p3_turn.color("red")
        else:
            if turn == 2:
                p2_turn.color("green")
                p1_turn.color("red")
                p3_turn.color("red")
            else:
                if turn == 3:
                    p3_turn.color("green")
                    p2_turn.color("red")
                    p1_turn.color("red")
    else:
        if turn >= 3:
            turn = 1
            p1_turn.color("green")
            p2_turn.color("red")
            p3_turn.color("red")
        else:
            turn += 1
            if turn == 2:
                p2_turn.color("green")
                p1_turn.color("red")
                p3_turn.color("red")
            elif turn == 3:
                p3_turn.color("green")
                p2_turn.color("red")
                p1_turn.color("red")
class Question():
    def __init__(self,q,w1,w2,w3,c):
        self.qu = q
        self.wr1 = w1
        self.wr2 = w2
        self.wr3 = w3
        self.cor = c
    def insert_q(self):
        global a_list
        a_list.append(self.wr1)
        a_list.append(self.wr2)
        a_list.append(self.wr3)
        a_list.append(self.cor)
        shuffle(a_list)
        main.goto(-323,110)
        main.write(self.qu, font = ("Arial",10,"normal"))
        op1.showturtle()
        op1.penup()
        op1.goto(-80,50)
        op1.write(str(a_list[0]), font = ("Arial",10,"normal"))
        op1.shapesize(4)
        op1.goto(-65,10)
        op1.shape("square")
        op1.color("black")
        op2.showturtle()
        op2.penup()
        op2.goto(-80,-60)
        op2.write(str(a_list[1]), font = ("Arial",10,"normal"))
        op2.shapesize(4)
        op2.goto(-65,-100)
        op2.shape("square")
        op2.color("black")
        op3.showturtle()
        op3.penup()
        op3.goto(80,50)
        op3.write(str(a_list[2]), font = ("Arial",10,"normal"))
        op3.shapesize(4)
        op3.goto(65,10)
        op3.shape("square")
        op3.color("black")
        op4.showturtle()
        op4.penup()
        op4.goto(80,-60)
        op4.write(str(a_list[3]), font = ("Arial",10,"normal"))
        op4.shapesize(4)
        op4.goto(65,-100)
        op4.shape("square")
        op4.color("black")
def draw_main_screen():
    global current_screen,p1_name,p2_name,p3_name,p1_score,p2_score,p3_score,easy_bi,easy_func,easy_poly,normal_bi,normal_func,normal_poly,hard_func,hard_bi,hard_poly,gameturn,chosen_q,chosen_q_class,selected_q_difficulty,q_end,lqc,player_1_item,player_2_item,player_3_item
    chosen_q = None
    chosen_q_class = None
    selected_q_difficulty = None
    q_end = False
    lqc = None
    current_screen = "main"
    main.clear()
    main.speed(10000)
    main.penup()
    main.goto(-770,275)
    main.pendown()
    main.forward(350)
    main.left(90)
    main.forward(150)
    main.penup()
    main.goto(-760,375)
    main.write("Player 1 Name:", font = ("Arial",10,"normal"))
    main.goto(-670,375)
    main.write(p1_name, font = ("Arial",10,"normal"))
    main.goto(-760,355)
    main.write("Player Score: ", font = ("Arial",10,"normal"))
    p1.showturtle()
    p1.speed(3000)
    p1.penup()
    p1.goto(-680,355)
    p1.write(str(p1_score), font = ("Arial",10,"normal"))
    p1.left(90)
    p1.hideturtle()
    p1_turn.showturtle()
    p1_turn.speed(3000)
    p1_turn.shape("circle")
    p1_turn.shapesize(3)
    p1_turn.penup()
    p1_turn.goto(-730,315)
    main.goto(-420,275)
    main.right(90)
    main.pendown()
    main.forward(350)
    main.left(90)
    main.forward(150)
    main.penup()
    main.goto(-415,375)
    main.write("Player 2 Name:", font = ("Arial",10,"normal"))
    main.goto(-325,375)
    main.write(p2_name, font = ("Arial",10,"normal"))
    main.goto(-415,355)
    main.write("Player Score: ", font = ("Arial",10,"normal"))
    p2.showturtle()
    p2.speed(3000)
    p2.penup()
    p2.goto(-335,355)
    p2.write(str(p2_score), font = ("Arial",10,"normal"))
    p2.pendown()
    p2.left(90)
    p2.hideturtle()
    p2_turn.showturtle()
    p2_turn.speed(3000)
    p2_turn.shape("circle")
    p2_turn.shapesize(3)
    p2_turn.penup()
    p2_turn.goto(-385,315)
    main.goto(-70,275)
    main.right(90)
    main.pendown()
    main.forward(350)
    main.left(90)
    main.forward(150)
    main.penup()
    main.goto(-65,375)
    main.write("Player 3 Name:", font = ("Arial",10,"normal"))
    main.goto(25,375)
    main.write(p3_name, font = ("Arial",10,"normal"))
    main.goto(-65,355)
    main.write("Player Score: ", font = ("Arial",10,"normal"))
    p3.showturtle()
    p3.speed(3000)
    p3.penup()
    p3.goto(15,355)
    p3.write(str(p3_score), font = ("Arial",10,"normal"))
    p3.pendown()
    p3.left(90)
    p3.hideturtle()
    p3_turn.showturtle()
    p3_turn.speed(3000)
    p3_turn.shape("circle")
    p3_turn.shapesize(3)
    p3_turn.penup()
    p3_turn.goto(-35,315)
    turncolor()
    main.begin_fill()
    main.color("aquamarine4")
    main.goto(-650,250)
    main.pendown()
    main.left(180)
    main.forward(567)
    main.left(90)
    main.forward(1200)
    main.left(90)
    main.forward(567)
    main.left(90)
    main.forward(1200)
    main.end_fill()
    main.color("black")
    main.penup()
    main.left(90)
    main.forward(159)
    main.left(90)
    main.forward(30)
    main.write("Binomials", font = ("Arial",25,"normal"))
    main.right(90)
    main.forward(159)
    main.left(90)
    main.write("Functions", font = ("Arial",25,"normal"))
    main.right(90)
    main.forward(159)
    main.left(90)
    main.write("Polynomials", font = ("Arial",25,"normal"))
    main.forward(175)
    main.right(90)
    main.forward(90)
    main.right(180)
    main.pendown()
    main.forward(567)
    main.penup()
    main.left(90)
    main.forward(205)
    main.left(150)
    main.pendown()
    main.forward(237)
    main.right(150)
    main.forward(205)
    main.right(90)
    main.goto(-650,250)
    main.right(90)
    main.forward(205)
    main.right(90)
    main.forward(120)
    main.left(90)
    main.forward(995)
    main.left(90)
    main.forward(120)
    main.left(90)
    main.forward(995)
    main.right(180)
    main.penup()
    main.forward(331)
    main.right(90)
    main.pendown()
    main.forward(120)
    main.left(90)
    main.penup()
    main.forward(331)
    main.left(90)
    main.pendown()
    main.forward(120)
    main.penup()
    main.goto(-650,250)
    main.left(180)
    main.forward(239)
    main.left(90)
    main.pendown()
    main.forward(205)
    main.left(180)
    main.penup()
    main.forward(205)
    main.left(90)
    main.forward(159)
    main.left(90)
    main.pendown()
    main.forward(205)
    main.penup()
    main.goto(-650,250)
    main.right(90)
    main.pendown()
    main.forward(567)
    main.left(90)
    main.forward(1200)
    main.left(90)
    main.forward(567)
    main.left(90)
    main.forward(1200)
    main.penup()
    main.goto(-570,210)
    main.left(180)
    main.write("Difficulty",font = ("Arial",20,"normal"))
    main.goto(-630,150)
    main.write("Topic",font = ("Arial",20,"normal"))
    main.goto(-650,250)
    main.forward(340)
    main.right(90)
    main.forward(75)
    main.left(90)
    main.write("Easy", font = ("Arial",25,"normal"))
    main.forward(301)
    main.write("Normal", font = ("Arial",25,"normal"))
    main.forward(350)
    main.write("Hard", font = ("Arial",25,"normal"))
    main.goto(-650,250)
    main.right(90)
    main.goto(-445,11)
    main.left(90)
    main.pendown()
    main.forward(995)
    main.penup()
    main.goto(-445,11)
    main.right(90)
    main.forward(159)
    main.left(90)
    main.pendown()
    main.forward(995)
    main.penup()
    main.goto(-650,250)
    main.forward(536)
    main.right(90)
    main.pendown()
    main.goto(main.xcor(),-317)
    main.left(90)
    main.penup()
    main.goto(main.xcor(),250)
    main.forward(331)
    main.right(90)
    main.pendown()
    main.goto(main.xcor(),-317)
    main.penup()
    main.goto(-325,100)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    e_b.speed(3000)
    e_b.penup()
    e_b.goto(-240,100)
    e_b.left(90)
    e_b.write(str(easy_bi), font = ("Arial",10,"normal"))
    e_b.shape("square")
    e_b.shapesize(3)
    e_b.goto(-277,60)
    main.forward(125)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    e_f.speed(3000)
    e_f.penup()
    e_f.goto(-240,-25)
    e_f.left(90)
    e_f.write(str(easy_func), font = ("Arial",10,"normal"))
    e_f.shape("square")
    e_f.shapesize(3)
    e_f.goto(-277,-65)
    main.forward(155)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    e_p.speed(3000)
    e_p.penup()
    e_p.goto(-240,-180)
    e_p.left(90)
    e_p.write(str(easy_poly), font = ("Arial",10,"normal"))
    e_p.shape("square")
    e_p.shapesize(3)
    e_p.goto(-277,-220)
    main.goto(6,100)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    n_b.speed(3000)
    n_b.penup()
    n_b.goto(91,100)
    n_b.left(90)
    n_b.write(str(normal_bi), font = ("Arial",10,"normal"))
    n_b.shape("square")
    n_b.shapesize(3)
    n_b.goto(53,60)
    main.forward(125)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    n_f.speed(3000)
    n_f.penup()
    n_f.goto(91,-25)
    n_f.left(90)
    n_f.write(str(normal_func), font = ("Arial",10,"normal"))
    n_f.shape("square")
    n_f.shapesize(3)
    n_f.goto(53,-65)
    main.forward(155)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    n_p.speed(3000)
    n_p.penup()
    n_p.goto(91,-180)
    n_p.left(90)
    n_p.write(str(normal_poly), font = ("Arial",10,"normal"))
    n_p.shape("square")
    n_p.shapesize(3)
    n_p.goto(53,-220)
    main.goto(337,100)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    h_b.speed(3000)
    h_b.penup()
    h_b.goto(422,100)
    h_b.left(90)
    h_b.write(str(hard_bi), font = ("Arial",10,"normal"))
    h_b.shape("square")
    h_b.shapesize(3)
    h_b.goto(384,60)
    main.forward(125)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    h_f.speed(3000)
    h_f.penup()
    h_f.goto(422,-25)
    h_f.left(90)
    h_f.write(str(hard_func), font = ("Arial",10,"normal"))
    h_f.shape("square")
    h_f.shapesize(3)
    h_f.goto(384,-65)
    main.forward(155)
    main.write("Questions left:", font = ("Arial",10,"normal"))
    h_p.speed(3000)
    h_p.penup()
    h_p.goto(422,-180)
    h_p.left(90)
    h_p.write(str(hard_poly), font = ("Arial",10,"normal"))
    h_p.shape("square")
    h_p.shapesize(3)
    h_p.goto(384,-220)
    main.goto(600,355)
    main.write("Turn:", font = ("Arial",25,"normal"))
    turn_t.showturtle()
    turn_t.penup()
    turn_t.goto(680,355)
    turn_t.write(str(gameturn), font = ("Arial",25,"normal"))
    turn_t.hideturtle()
    p1_item.showturtle()
    p1_item.speed(3000)
    p1_item.penup()
    p1_item.goto(-600,315)
    drawplayeritem1(player_1_item)
    p1_item.hideturtle()
    p2_item.showturtle()
    p2_item.speed(3000)
    p2_item.penup()
    p2_item.goto(-255,315)
    drawplayeritem2(player_2_item)
    p2_item.hideturtle()
    p3_item.showturtle()
    p3_item.speed(3000)
    p3_item.penup()
    p3_item.goto(95,315)
    drawplayeritem3(player_3_item)
    p3_item.hideturtle()
    e_b.showturtle()
    e_f.showturtle()
    e_p.showturtle()
    n_b.showturtle()
    n_f.showturtle()
    n_p.showturtle()
    h_b.showturtle()
    h_f.showturtle()
    h_p.showturtle()
def hideallturt():
    main.clear()
    p1.clear()
    p1.hideturtle()
    p2.clear()
    p2.hideturtle()
    p3.clear()
    p3.hideturtle()
    p1_turn.hideturtle()
    p2_turn.hideturtle()
    p3_turn.hideturtle()
    e_b.clear()
    e_b.hideturtle()
    e_f.clear()
    e_f.hideturtle()
    e_p.clear()
    e_p.hideturtle()
    n_b.clear()
    n_b.hideturtle()
    n_f.clear()
    n_f.hideturtle()
    n_p.clear()
    n_p.hideturtle()
    h_b.clear()
    h_b.hideturtle()
    h_f.clear()
    h_f.hideturtle()
    h_p.clear()
    h_p.hideturtle()
    turn_t.clear()
    turn_t.hideturtle()
    p1_item.clear()
    p2_item.clear()
    p3_item.clear()
def draw_question_screen_e_b(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, easy_bi
    if easy_bi > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "easy"
        main.penup()
        chosen_q = choice(eb_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        eb_list.remove(chosen_q)
        easy_bi -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_e_f(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, easy_func
    if easy_func > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "easy"
        main.penup()
        chosen_q = choice(ef_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        ef_list.remove(chosen_q)
        easy_func -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_e_p(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, easy_poly
    if easy_poly > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "easy"
        main.penup()
        chosen_q = choice(ep_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        ep_list.remove(chosen_q)
        easy_poly -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_n_b(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, normal_bi
    if normal_bi > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "normal"
        main.penup()
        chosen_q = choice(nb_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        nb_list.remove(chosen_q)
        normal_bi -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_n_f(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty,normal_func
    if normal_func > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "normal"
        main.penup()
        chosen_q = choice(nf_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        nf_list.remove(chosen_q)
        normal_func -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_n_p(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, normal_poly
    if normal_poly > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "normal"
        main.penup()
        chosen_q = choice(np_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        np_list.remove(chosen_q)
        normal_poly -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_h_b(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, hard_bi
    if hard_bi > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "hard"
        main.penup()
        chosen_q = choice(hb_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        hb_list.remove(chosen_q)
        hard_bi -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_h_f(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty,hard_func
    if hard_func > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "hard"
        main.penup()
        chosen_q = choice(hf_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        hf_list.remove(chosen_q)
        hard_func -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_question_screen_h_p(x,y):
    global current_screen , a_list, chosen_q, chosen_q_class, selected_q_difficulty, hard_poly
    if hard_poly > 0:
        current_screen = "question"
        hideallturt()
        selected_q_difficulty = "hard"
        main.penup()
        chosen_q = choice(hp_list)
        main.goto(-323,110)
        chosen_q_class = Question(chosen_q[0],chosen_q[1],chosen_q[2],chosen_q[3],chosen_q[4])
        chosen_q_class.insert_q()
        hp_list.remove(chosen_q)
        hard_poly -= 1
        main.goto(-75,300)
        main.write("Time:", font = ("Arial",25,"normal"))
        timer.showturtle()
        timer.penup()
        timer.goto(10,300)
        timer.hideturtle()
        tick(time)
    else:
        warn.write("There are no questions left on that topic.", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def option1(x,y):
    global a_list, chosen_q, q_end, turn, gameturn, selected_q_difficulty, lqc
    if q_end == False:
        if a_list[0] == chosen_q[4]:
            warn.write("Your answer is correct!", font = ("Arial",40,"normal"))
            win.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = True
            rewarditem()
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
        else:
            warn.write("Your answer is incorrect!", font = ("Arial",40,"normal"))
            lose.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = False
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
    else:
        warn.write("You have already answered the question!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def option2(x,y):
    global a_list, chosen_q, q_end, turn, gameturn, selected_q_difficulty, lqc
    if q_end == False:
        if a_list[1] == chosen_q[4]:
            warn.write("Your answer is correct!", font = ("Arial",40,"normal"))
            win.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = True
            rewarditem()
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
        else:
            warn.write("Your answer is incorrect!", font = ("Arial",40,"normal"))
            lose.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = False
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
    else:
        warn.write("You have already answered the question!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def option3(x,y):
    global a_list, chosen_q, q_end, turn, gameturn, selected_q_difficulty, lqc
    if q_end == False:
        if a_list[2] == chosen_q[4]:
            warn.write("Your answer is correct!", font = ("Arial",40,"normal"))
            win.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = True
            rewarditem()
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
        else:
            warn.write("Your answer is incorrect!", font = ("Arial",40,"normal"))
            sleep(1)
            lose.play()
            warn.clear()
            q_end = True
            lqc = False
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
    else:
        warn.write("You have already answered the question!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def option4(x,y):
    global a_list, chosen_q, q_end, turn, gameturn, selected_q_difficulty, lqc
    if q_end == False:
        if a_list[3] == chosen_q[4]:
            warn.write("Your answer is correct!", font = ("Arial",40,"normal"))
            win.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = True
            rewarditem()
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
        else:
            warn.write("Your answer is incorrect!", font = ("Arial",40,"normal"))
            lose.play()
            sleep(1)
            warn.clear()
            q_end = True
            lqc = False
            editscore()
            back.showturtle()
            back.goto(575,-270)
            back.write("Back", font = ("Arial",25,"normal"))
            back.goto(610,-315)
    else:
        warn.write("You have already answered the question!", font = ("Arial",40,"normal"))
        sleep(1)
        warn.clear()
def draw_results_screen():
    global current_screen,player_1_time_spent,player_2_time_spent,player_3_time_spent,p1_score,p2_score,p3_score
    current_screen = "results"
    main.penup()
    main.goto(-100,0)
    main.write("Our game is now over!", font = ("Arial",25,"normal"))
    sleep(0.5)
    main.clear()
    main.write("Thank you for playing Math Duel!", font = ("Arial",25,"normal"))
    sleep(0.5)
    main.clear()
    main.goto(65,200)
    main.write("Score", font = ("Arial",10,"normal"))
    main.goto(200,200)
    main.write("Total time spent (s)", font = ("Arial",10,"normal"))
    main.goto(-75,100)
    main.write("Player 1", font = ("Arial",10,"normal"))
    main.goto(75,100)
    main.write(str(p1_score), font = ("Arial",10,"normal"))
    main.goto(250,100)
    main.write(str(player_1_time_spent), font = ("Arial",10,"normal"))
    main.goto(-75,0)
    main.write("Player 2", font = ("Arial",10,"normal"))
    main.goto(75,0)
    main.write(str(p2_score), font = ("Arial",10,"normal"))
    main.goto(250,0)
    main.write(str(player_2_time_spent), font = ("Arial",10,"normal"))
    main.goto(-75,-100)
    main.write("Player 3", font = ("Arial",10,"normal"))
    main.goto(75,-100)
    main.write(str(p3_score), font = ("Arial",10,"normal"))
    main.goto(250,-100)
    main.write(str(player_3_time_spent), font = ("Arial",10,"normal"))
    
def backtomain(x,y):
    back.clear()
    back.hideturtle()
    global q_end,chosen_q,chosen_q_class,selected_q_difficulty, lqc, total_q, a_list
    op1.clear()
    op1.hideturtle()
    op2.clear()
    op2.hideturtle()
    op3.clear()
    op3.hideturtle()
    op4.clear()
    op4.hideturtle()
    timer.clear()
    timer.hideturtle()
    chosen_q = None
    chosen_q_class = None
    selected_q_difficulty = None
    q_end = False
    lqc = None
    a_list = []
    main.clear()
    main.left(90)
    total_q -= 1
    if total_q <= 0:
        draw_results_screen()
    else:
        draw_main_screen()
p1_name = input("Enter the name of the 1st player.")
while len(p1_name) >= 18:
    print("The name is too long. Please try again.")
    p1_name = input("Enter the name of the 1st player.")
p2_name = input("Enter the name of the 2nd player.")
while len(p2_name) >= 18:
    print("The name is too long. Please try again.")
    p2_name = input("Enter the name of the 2nd player.")
p3_name = input("Enter the name of the 3rd player.")
while len(p3_name) >= 18:
    print("The name is too long. Please try again.")
    p3_name = input("Enter the name of the 3rd player.")
print("It is recommended to read the game instructions before playing.")
draw_main_screen()
mixer.music.play(-1)
e_b.onclick(draw_question_screen_e_b)
e_f.onclick(draw_question_screen_e_f)
e_p.onclick(draw_question_screen_e_p)
n_b.onclick(draw_question_screen_n_b)
n_f.onclick(draw_question_screen_n_f)
n_p.onclick(draw_question_screen_n_p)
h_b.onclick(draw_question_screen_h_b)
h_f.onclick(draw_question_screen_h_f)
h_p.onclick(draw_question_screen_h_p)
op1.onclick(option1)
op2.onclick(option2)
op3.onclick(option3)
op4.onclick(option4)
back.onclick(backtomain)
main_screen.onkey(turnonextrap,"e")
main_screen.onkey(turnonmultiplier,"m")
main_screen.onkey(thief,"t")
main_screen.listen()
mainloop()

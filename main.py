import random
lst = ["Snake", "Water", "Gun"]
b=random.choice(lst)
n = 0
t = 10
c = 0
h = 0
while n != 10:
    a = input("Press S for Snake\nW for Water\nG for Gun\nEnter your Choice : ")
    if (a == 'S' and b == 'Water'):
        h=h+1
        print("Snake drinks the water")
        print("You Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    elif (a == 'W' and b == 'Snake'):
        c=c+1
        print("Snake drinks the water")
        print("Computer Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    elif (a == 'S' and b == 'Gun'):
        c=c+1
        print("Snake is killed by the Gun")
        print("Computer Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    elif (a == 'G' and b == 'Snake'):
        h=h+1
        print("Snake is killed by the Gun")
        print("You Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    elif (a == 'G' and b == 'Water'):
        c=c+1
        print("Gun sink in the water")
        print("Computer Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    elif (a == 'W' and b == 'Gun'):
        h=h+1
        print("Gun sink in the water")
        print("You Win 1 point")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    else:
        c=c
        h=h
        print("Tie!You both have the same choice")
        print(f"Your Point {h} and computer point {c}")
        t=t-1
        print(f"{t} Chances left")
    n = n + 1
print("Game Over")
if c>h:
    print(f"Computer Wins!!!\nComputer Point={c} and Your Points={h}")
elif c<h:
    print(f"You Wins!!!\nComputer Point={c} and Your Points={h}")
else:
    print(f"Tie!!!Both have same points\nComputer Point={c} and Your Points={h}")
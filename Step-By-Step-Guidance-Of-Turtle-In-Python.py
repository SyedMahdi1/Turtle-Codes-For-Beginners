#First We Add Module Name Turtle
import turtle
#Now Lets a Window I will Name Window You Can Write Anything Whatever You Like. It's All Up To You

Window = turtle.Screen()
#Our Window Name Is Name Is Nothing
Window.title("Name Is Nothing")
#Now Let's Add Runner Which Will Move. I will name it Runner1Killer. Because It Like This Name. You can write anything.

Runner1Killer1 = turtle.Turtle()

# Here we add a turtle screen name Window and a runner name Runner1Killer
# Now Let's change the color of our runner because I dont like default black color. i will chose cyan color means sky blue color. You can chose anything you want to add.

Runner1Killer1.color("Cyan")

# Our runner has color cyan

# Now Let's make the runner move forward
Runner1Killer1.fd(100)

# It's speed Is Slow I want more Speed

# I will do this

Runner1Killer1.speed(3)

# Now I want to change the direction of the runner in right direction.
# Remember we cannot move the runner in right direction. We only change the angle

Runner1Killer1.rt(90)
# Now Lets forward the Runner
Runner1Killer1.fd(100)
# When we do this things many times we get a square

Runner1Killer1.rt(90)
Runner1Killer1.fd(100)
Runner1Killer1.rt(90)
Runner1Killer1.fd(100)
# Finally we got a square
# But It Took so much time and lines we can do this step to make our square speedily

for _ in range(4):
    Runner1Killer1.fd(100)
    Runner1Killer1.rt(90)
# Yes we make a sqaure in less time. Now listen 'for in range' u need to learn and in (4) is the sides of square means in next line fd 100 you can chose anything and remember if the number is 4 in brackets then you have to divide by 360 and whatever answer you got enter in angle option (rt or lt). if you want to make hexagon it has 6 sides divide now divide the answer to 360 and whatever answer you get enter in rt or lt
#Simple

#Now Lets change the pensize of our runner

Runner1Killer1.pensize(4)

#Now Lets Make A circle
Runner1Killer1.circle(50)
#50 is the radius
#now lets stop the terminal by using the code which is given below

Window.exitonclick()
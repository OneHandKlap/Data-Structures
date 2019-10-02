import turtle
import random

def tree(branchLen,t,angle=0):
    if branchLen<=25:
        t.pencolor('green')
    else:
        t.pencolor('#8a5103')
    if branchLen<=5:
        return
    else:
        rand_angle=random.randrange(5,25) #between 5 and 25 degrees of angle seemed most natural looking to me  
        rand_branch_reduction = random.randrange(5,10) #I found that a smaller factor of reduction increased the over all size of the tree, making it look more natural
        t.pensize((branchLen/75)*10) # the pensize is a function of the branch length, as the branch decreases in length, so does the pen size
        t.forward(branchLen)
        t.right(rand_angle)
        tree(branchLen-rand_branch_reduction,t,rand_angle) 
        t.left(rand_angle*2)
        tree(branchLen-rand_branch_reduction,t,rand_angle)
        t.right(rand_angle)
        t.backward(branchLen)
        t.color("#8a5103") #nicer shade of brown#

def main():
    t=turtle.Turtle()
    myWin = turtle.Screen()
    turtle.tracer(0) #turns off the tracer so that the image is generated automatically
    t.left(90)
    t.up()
    t.backward(200) #modified so my larger tree would fit on the page
    t.down()
    t.color("green")
    tree(75,t)
    turtle.getscreen().getcanvas().postscript(file="tree.ps")
    myWin.exitonclick()

def power(x,n,acc):
    if n==0:
        return acc
    else:
        acc=acc*x
        return (power(x,n-1,acc))

def powerH(x,n):
    if n ==1:
        return x
    else:
        if n%2==0:
            return (powerH(x,n//2)*powerH(x,n//2))
        else:
            return (powerH(x,n//2)*powerH(x,n//2))*x

def C(n,k):
    if k==0 or k==n:
        return 1
    else:
        return C(n-1,k)+C(n-1,k-1)
main()


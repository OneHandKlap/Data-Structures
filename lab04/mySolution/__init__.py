import turtle
import random

def tree(branchLen,t,angle=0):
    if branchLen<=10:
        t.pencolor('green')
    else:
        t.pencolor('brown')
    if branchLen<=5:
        return
    else:
        rand_angle=random.randrange(5,20)
        rand_branch_reduction = random.randrange(5,int(25*(branchLen/75))+5)
        t.pensize((branchLen/75)*10)
        t.forward(branchLen)
        t.right(rand_angle)
        tree(branchLen-rand_branch_reduction,t,rand_angle)
        t.left(rand_angle*2)
        tree(branchLen-rand_branch_reduction,t,rand_angle)
        t.right(rand_angle)
        t.backward(branchLen)

def main():
    t=turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

def power(x,n,acc):
    if n==0:
        return acc
    else:
        acc=acc*x
        return (power(x,n-1,acc))

print("power result:" +str(power(2,4,1)))

def powerH(x,n):
    if n ==1:
        return x
    else:
        if n%2==0:
            return (powerH(x,n//2)*powerH(x,n//2))
        else:
            return (powerH(x,n//2)*powerH(x,n//2))*x

print("powerH result:" +str(powerH(2,6)))

def C(n,k,acc=0):
    if k==0 or k==n:
        return 1
    else:
        return C(n-1,k)+C(n-1,k-1)

print("C result:"+str(C(5,4)))


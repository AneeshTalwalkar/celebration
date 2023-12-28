
from random import choice
plyer=0
co=0
rps = ["rock", "paper", "scissors"]

for i in range(5):
  player = input("choose - rock, paper or scissors: ")
  computer = choice(rps)
  print("Computer chose: " + computer)

  if player == "rock" and computer == "rock":
    print("Tie!")
  elif player == "rock" and computer == "paper":
    print("Computer wins")
    co+=1
  elif player == "rock" and computer == "scissors":
    print( "Player wins")
    plyer+=1
  elif player == "paper" and computer == "rock":
    print( "Player wins")
    plyer+=1
  elif player == "paper" and computer == "paper":
    print("Tie!")
  elif player == "paper" and computer == "scissors":
    print("Computer wins")
    co+=1
  elif player == "scissors" and computer == "rock":
    print("Computer wins")
    co+=1
  elif player == "scissors" and computer == "paper":
    print("Player wins")
    plyer+=1

  elif player == "scissors" and computer == "scissors":
    print("Tie")
  else:
    print("Invalid input")

print()

print ("Score of computer:",co)
print ("Score of player:",plyer)
if co>plyer:
  print("computer won the tournament")
if co<plyer:
  print( "player won the tournament")
if co==plyer:
  print("it was a tie")

'''from turtle import *
import turtle
t = turtle.Turtle()
t.width(4)
t.speed(3)
turtle.Screen().bgcolor("Black")
t.color("cyan")


t.lt(90)
t.fd (100)
t.lt(30)
t.fd(70)
t.rt(180)
t.fd(70)
t.lt(150)

t.rt(30)
t.fd(75)
t.rt(180)
t.fd(75)
t.rt(150+180)
t.fd(100)


def space ():
  t.pu()
  t.lt(90)
  t.fd(80)
  t.lt(90)
  t.pd()
space()


t.rt(90)
t.fd(80)
t.lt(180)
t.fd(80)
t.rt(90)
t.fd(70)
t.rt(90)
t.fd(80)
t.rt(180)
t.fd(80)

t.rt(90)
t.fd(70)
t.rt(90)
t.fd(90)
t.rt(180)
t.fd(90)
t.lt(90)
t.fd(140)


t.pu()
t.lt(90)
t.fd(120)
t.lt(90)
t.pd()


t.rt(90)
t.fd(80)
t.lt(180)
t.fd(80)
t.rt(90)
t.fd(70)
t.rt(90)
t.fd(80)
t.rt(180)
t.fd(80)
t.rt(90)
t.fd(70)
t.rt(90)
t.fd(90)
t.rt(180)
t.fd(90)
t.lt(90)
t.fd(140)


t.pu()
t.lt(90)
t.fd(150)
t.lt(90)
t.pd()


t.fd(140)
t.rt(90)
t.fd(70)
t.rt(180)
t.fd(140)'''
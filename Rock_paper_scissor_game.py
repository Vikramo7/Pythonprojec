import random
print("......welcome to rock paper scissors game...")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print(""" 
1.paper vs rock --> paper
2. rock vs scissors --> rock
3. scissor vs paper --> scissors""")

print("""choices are:
1.rock
2.paper
3.scissors""")
choice = int(input("enter your choice frm 1-3:"))

if choice == 1:
    user_choice = "rock"
elif choice == 2:
    user_choice = "paper"
else:
    user_choice = "scissors"

print("the user's choice is",user_choice)
print("Now it is computer's turns")

computer = random.randint(1,3)

if computer == 1:
    comp_choice == "rock"
elif computer == 2:
    comp_choice = "paper"
else:
    comp_choice = "scissors"

print("the computer's choice is :",comp_choice)

if ((user_choice == "paper" and com_choice == "rock") or (user_choice == "rock" and comp_choice == "paper")):
    print("paper wins")
    result = "paper"
elif ((user_choice == "rock" and comp_choice == "scissors") or (user_choice == "rock" and comp_choice == "scissors")):
    print("rock wins")
    result = "rock"
elif (user_choice == comp_choice):
    print("it's a tie")
    result = "tie"
else:
    print("scissors wins")
    result = "scissors"



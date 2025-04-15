import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
bot = random.randint(1,2)
if choice == 0:
    print(f"You choose: {rock}\n")
elif choice == 1:
    print(f"You choose: {paper}\n")
elif choice == 2:
    print(f"You choose: {scissors}\n")
else:
    print("Invalid choice")

if bot == 0:
    print(f"Computer chooses: {rock}\n")
elif bot == 1:
    print(f"Computer chooses: {paper}\n")
elif bot == 2:
    print(f"Computer chooses: {scissors}\n")
else:
    print("Invalid choice")


def game(a,b):
    if a == b:
        print("It's a draw!")
    elif a < b:
        if choice == 0 and bot == 2:
            print("You win")
        else:
            print("The computer wins")
    elif a > b:
        if choice == 2 and bot == 0:
            print("The computer wins!")
        else:
            print("You win")


game(choice,bot)
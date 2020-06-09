import random

def comp_choice():
    choice = random.randint(1,3)
    if choice == 1:
        return "batu"
    elif choice == 2:
        return "gunting"
    else:
        return "kertas"

def battle(human, computer):
    if choice == computer:
        return ("Tie!")
    if choice == "batu" and computer == "kertas":
        return ("Computer Wins")
    if choice == "batu" and computer == "gunting":
        return ("Human Wins")
    if choice == "kertas" and computer == "gunting":
        return ("Computer Wins")
    if choice == "kertas" and computer == "batu":
        return ("Human Wins")
    if choice == "gunting" and computer == "batu":
        return ("Computer Wins")
    if choice == "gunting" and computer == "kertas":
        return ("Computer wins")

again = "y"

print ( "Computer Vs Human\n"
        "===Suit Battle===\n")

while again != "n":
    print("Mau Keluarin Apa?")
    choice = input ("Batu / Gunting / Kertas\n").lower()

    if choice == "batu" or choice == "gunting" or choice == "kertas":
        computer = comp_choice()
        print(f"{choice} Vs {computer}")
        print (battle(choice, computer))
        
        again = input("Mo gulat lagi (y/n)? ")

    else:
        print("Invalid Input")
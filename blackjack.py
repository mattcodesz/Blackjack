import csv
import random
def playerProfile():
    f = open("profiles.txt", "a+")
    fields = []
    field = []
    profile = ''
    while(len(profile) != 3):
        profile = input("Please enter your 3 initials so that your profile can be saved (ex:ABC): \n").upper()
        if(len(profile) != 3):
            print("\nPlease enter only 3 letters or numbers")
            continue
    found = False
    with open("profiles.txt") as f:
        search = f.readlines()
    f = open("profiles.txt", "a+")
    for line in search: 
        if(profile in line):
            found = True
    if(found == True):
        with open('profiles.txt', 'r') as f:
            for line in f:
                fields.append(line.strip().split())
        f.close()
        rows = len(fields)
        for i in range(rows):
            if(fields[i][0] == profile):
                field.append(fields[i][0])
                field.append(fields[i][1])
                field.append(fields[i][2])
                field.append(fields[i][3])
        return field, profile
    else:
        f.write(profile + " 1000" + ' 0' + ' 0\n')
        with open('profiles.txt', 'r') as f:
            for line in f:
                fields.append(line.strip().split())
        f.close()
        rows = len(fields)
        for i in range(rows):
            if(fields[i][0] == profile):
                field.append(fields[i][0])
                field.append(fields[i][1])
                field.append(fields[i][2])
                field.append(fields[i][3])
        return field, profile

def update(field, lst1, lst2):
    fields = []
    del lst1[:]
    del lst2[:]
    if(field[1] < 50):
        print("You have ran out of money! Your profile will be reset to default amounts.")
        field[1] = 1000
        field[2] = 0
        field[3] = 0
    with open('profiles.txt', 'r') as f:
        for line in f:
            fields.append(line.strip().split())
    rows = len(fields)
    for i in range(rows):
       if(fields[i][0] == field[0]):
           fields[i][1] = field[1]
           fields[i][2] = field[2]
           fields[i][3] = field[3]
    with open('profiles.txt', 'w', newline='') as f:
        writer = csv.writer(f,delimiter=' ')
        for lst in fields:
            writer.writerow(lst)
    return lst1, lst2

def dealCards(cards):
    card1 = random.randint(1, 10)
    card2 = random.randint(1, 10)
    if(card1 == 1):
        tempcard = 11
        if(tempcard + card2 <=21):
            card1 = tempcard
        else:
            card1 = 1
    if(card2 == 1):
        tempcard = 11
        if(tempcard + card1 <=21):
            card2 = tempcard
        else:
            card2 = 1
    cards.append(card1)
    cards.append(card2)
    return cards

def hit(cards, case):
    choice = 1
    if(case == True):
        total = sum(cards)
        print("\nYour cards total to:", total)
        while(choice != 2):
            choice = int(input("\nPress 1 if you want to hit, press 2 if you want to stay: "))
            if(choice == 1):
                pass
                #Use random function to to get a new card and append it to the card list
                #Need a loop so the user can keep hitting till they are satisfied
                #if user hits 21 break out of function with a return statement that lets the program know that the user won
                #once back in the main function, you need to add 1 to field[2]; which is the field that keeps track of wins
                #if the user goes above 21; break out of function and add 1 to field[3]
            if(choice == 2):
                break
    elif(case == false):
        pass
        #check if sum is less than 17; if it is, hit until it is 17 or greater.
        
def compare(pCards, dCards):
    pass
    #Assuming that the hit function checks if there are any automatic wins or losses; this function will check to see if the player or the dealer is closer to 21
    #Whoever is closer wins
    #returns some value letting the program know if the player wins or loses
    
    
def main():
    choice = 0
    field, profile = playerProfile()
    playerCards = []
    dealerCards = []
    while(choice != 2):
        print("\nYou are currently playing on profile:", profile)
        choice = int(input("\nPress 1 to play the game, press 2 to exit the game, press 3 to load a different profile\n"))
        if(choice == 2):
            break
        if(choice != 1 and choice != 2 and choice != 3):
            print("Error: You have entered an incorrect value")
            continue
        if(choice == 3):
            field, profile = playerProfile()
            continue
        field[1] = int(field[1])
        field[2] = int(field[2])
        field[3] = int(field[3])
        money = field[1]
        bet = 0
        while(bet < 50 or bet > 500):
            bet = int(input("\nPlease enter a bet between $50 and $500: "))
            if(bet < 50 or bet > 500):
                print("You have entered an incorrect amount")
                continue
            if(bet > money):
                print("You dont have that much money!")
                continue
            else:
                break
        dealCards(playerCards)
        dealCards(dealerCards)
        print("\nYour cards are:", *playerCards)
        print("\nThe dealer has cards: *", dealerCards[1])
        hit(playerCards, True)
        #put this function in an if statement that checks if the player won or lost in the previous function; If the player won or lost then it is not necessary to run this part
        #if ???:
            #hit(dealerCards, False)
        compare(playerCards, dealerCards)
        #if player wins; add bet to field[1](money field); subtract if player loses
        #add 1 to the win or losses field depending on the result
        
        update(field, playerCards, dealerCards)

main()

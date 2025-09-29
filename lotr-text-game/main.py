import time
import random
import os
import json

file_path = os.path.abspath(__file__)

def get_quest():
    quest_str = os.environ.get('QUEST')
    if quest_str:
        quest_list = json.loads(quest_str)
        return quest_list
    else:
        return False

def check_inventory():
    inventory_str = os.environ.get('INVENTORY')
    if inventory_str:
        inventory_list = json.loads(inventory_str)
        return inventory_list
    else:
        return False


def player_attack(type):
    goblin_health = int(os.environ.get('GOBLIN_HEALTH'))
    
    if type == "hand":
        if random.randint(0, 10) >= 5:
            damage = random.randint(1, 2)
        else:
            damage = False
    else:
        if random.randint(0, 10) >= 3:
            damage = random.randint(2, 5)
        else:
            damage = False
    
    if damage != False:
        new_goblin_health = goblin_health - damage
        os.environ['GOBLIN_HEALTH'] = str(new_goblin_health)

        if int(os.environ.get('GOBLIN_HEALTH')) <= 0:
            kill = True
        else:
            kill = False
    else:
        kill = False
    
    return damage, kill

def goblin_attack():
    player_health = int(os.environ.get('PLAYER_HEALTH'))

    if random.randint(0, 10) >= 3:
        damage = random.randint(1, 3)
    else:
        damage = False
    
    if damage != False:
        new_player_health = player_health - damage
        os.environ['PLAYER_HEALTH'] = str(new_player_health)

        if int(os.environ.get('PLAYER_HEALTH')) <= 0:
            kill = True
        else:
            kill = False
    else:
        kill = False
    
    player_health = str(os.environ.get('PLAYER_HEALTH'))
    
    return damage, kill, player_health


print("** Welcome to the LOTR Text based adventure! **\n")
pname = input("What is your first name, adventurer? ").title()
plname= input("What is your last name? ").title()
print(f"Welcome to Middle Earth, {pname}!\n")

print("Welcome to Middle Earth! This vast landscape has been \nthe realm where many an adventure have takem place. \nNow it's your turn...\n")
time.sleep(3)

print("You open your eyes to the sight of the rolling green hills of Hobbiton.")
time.sleep(2)
print("Suddenly you here a voice from behind!\n")
time.sleep(2)

print(f"[voice]: {pname}! I told you not to fall asleep in the hammock again!\n")
time.sleep(1)
turn_choice = ["Turn around", "Don't turn around"]
for i, name in enumerate(turn_choice, 1):
    print(f"{i}. {name}")

turn_choice = input("Choice: (pick a number) ")

if turn_choice == "1":
    print("\nYou see that it is your mother\n")

    dialog_one = ["Sorry, Mom", "It's so comfortable!", "Whatever..."]
    for i, name in enumerate(dialog_one, 1):
        print(f"{i}. {name}")
    
    dialog_one_choice = input("Choice: ")
    dialog_one_key = int(dialog_one_choice) - 1
    print(f"\n[you]: {dialog_one[dialog_one_key]}")

    if dialog_one_choice == "1":
        print("[mom]: It's alright, but Mr. Hogg is asking for you at the depot.\n")
    elif dialog_one_choice == "2":
        print(f"[mom: I know, {pname}, but then I can't find you out here! Anyway, Mr. Hogg is asking for you at the depot.\n")
    elif dialog_one_choice == "3":
        print(f"[mom]: {pname}! That is very rude! Now go down to the depot, Mr. Hogg is looking for you!\n")

    dialog_two = ["Okay", "Ugh", "Did he say anything else?"]
    for i, name in enumerate(dialog_two, 1):
        print(f"{i}. {name}")
    dialog_two_choice = input("Choice: ")
    dialog_two_key = int(dialog_two_choice) - 1
    print(f"[you]: {dialog_two[dialog_two_key]}")

    if dialog_two_choice == "1":
        print("[mom]: Alright, just head on down there soon.")
        time.sleep(1)
        print("[mom]: ** walks away **\n")
        time.sleep(2)
        # Fixed: Use json.dumps() instead of str() to properly serialize the list
        os.environ['QUEST'] = json.dumps(["Visit Mr. Hogg at the depot"])
        print("\nNew quest: Visit Mr. Hogg at the depot")
    elif dialog_two_choice == "2":
        print("[mom]: Well I'm sorry but he said it was urgent! Now get on down there.")
        time.sleep(1)
        print("[mom]: ** walks away **\n")
        time.sleep(2)
        # Fixed: Use json.dumps() instead of str() to properly serialize the list
        os.environ['QUEST'] = json.dumps(["Visit Mr. Hogg at the depot"])
        print("\nNew quest: Visit Mr. Hogg at the depot")
    elif dialog_two_choice == "3":
        print("[mom]: Well, he said it was urgent but other then that he didn't mention anything...\nyou should get down there soon. I'm gonna make dinner.")
        time.sleep(1)
        print("[mom]: ** walks away **\n")
        time.sleep(2)
        # Fixed: Use json.dumps() instead of str() to properly serialize the list
        os.environ['QUEST'] = json.dumps(["Visit Mr. Hogg at the depot"])
        print("\nNew quest: Visit Mr. Hogg at the depot")

elif turn_choice == "2":
    print()
    dialog_one = ["Who are you?", "Go away!"]
    for i, name in enumerate(dialog_one, 1):
        print(f"{i}. {name}")
    dialog_one_choice = input("Choice: ")
    dialog_one_key = int(dialog_one_choice) - 1
    print(f"[you]: {dialog_one[dialog_one_key]}")

    if dialog_one_choice == "1":
        print("[voice]: *scoffs*\n")
        time.sleep(1)
        print("You here footsteps as the voice walks away...\n")
        time.sleep(1)
        print("The sweet mountain air washes over you as you fall back asleep...\n")
        time.sleep(1)
        play_again = input("Thanks for playing! Would you like to play again? (Y/n)").strip()

        if play_again.lower() == "y":
            print()
            time.sleep(1)
            os.system(f"python3 {file_path}")
        elif play_again.lower() == "":
            print()
            time.sleep(1)
            os.system(f"python3 {file_path}")
        else:
            exit("Thanks for playing!")
    elif dialog_one_choice == "2":
        print(f"[mom]: {pname} {plname}!! How dare you, I am your mother! Now go to the depot because Mr. Hogg is expecting you.")
        print("You here footsteps as your mom walks away...")
        time.sleep(2)
        # Fixed: Use json.dumps() instead of str() to properly serialize the list
        os.environ['QUEST'] = json.dumps(["Visit Mr. Hogg at the depot"])
        print("\nNew quest: Visit Mr. Hogg at the depot")

while True:
    print("\nWhat would you like to do?")
    actions = ["Check quest","Check inventory", "Go to depot", "Go back to sleep"]
    for i, name in enumerate(actions, 1):
        print(f"{i}. {name}")
    action_one = input("Choice: ")

    if action_one == "1":
        print()
        quest_check = get_quest()
        if quest_check == False:
            print("You have no quests at the moment")
            time.sleep(3)
            continue
        else:
            for i, name in enumerate(quest_check, 1):
                print(f"{i}. {name}")
            time.sleep(3)
            continue
    elif action_one == "2":
        print()
        inventory_check = check_inventory()
        if inventory_check == False:
            print("You have no items in your inventory")
            time.sleep(3)
            continue
        else:
            for i, name in enumerate(inventory_check, 1):
                print(f"{i}. {name}")
            time.sleep(3)
            continue
    elif action_one == "3":
        print("\nYou get up from the hammock and walk down the dirt path to the depot...")
        time.sleep(1)
        print("\nYou pass a number of other homes and people conversing as you make your way down")
        time.sleep(1)
        print("\nAs you approach the depot you see chaos as a Goblin destroys merchandise.\nYou spy Mr. Hogg looking at the scene in dismay.\n")
        time.sleep(2)

        print(f"[mr. hogg]: {pname}! Please help! we just got a shipment in from Bree and this\ngoblin has come to destory it all!\n")
        time.sleep(1)
        os.environ['QUEST'] = json.dumps(["Kill the goblin!"])
        print("Quest updated: kill the goblin!")
        break
    elif action_one == "4":
        print("\nYou lean your head back in the hammock and drift back to sleep as the cool\nspring air washes over you...")
        time.sleep(2)

        play_again = input("Thanks for playing! Would you like to play again? (Y/n)").strip()

        if play_again.lower() == "y":
            print()
            time.sleep(1)
            os.system(f"python3 {file_path}")
        elif play_again.lower() == "":
            print()
            time.sleep(1)
            os.system(f"python3 {file_path}")
        else:
            exit("Thanks for playing!")
while True:
    print("\nWhat would you like to do?")
    actions = ["Battle the goblin", "Talk to Mr. Hogg", "Check inventory", "Check quest"]
    for i, name in enumerate(actions, 1):
        print(f"{i}. {name}")
    action_two = input("Choice: ")

    if action_two == "1":
        time.sleep(1)
        print("\n** you have entered battle with a goblin! **\n")
        os.environ['GOBLIN_HEALTH'] = str(10)
        os.environ['PLAYER_HEALTH'] = str(8)
        time.sleep(1)
        print("[goblin]: *stares at you menacingly*\n")

        inventory_check = check_inventory()
        if inventory_check == False:
            weapon = "hand"
        else:
            weapon = "sword"

        goblin_alive = True

        while goblin_alive:
            if bool(os.environ.get('TURN')) == True:
                attacks = ["Slashes at", "hits", "attacks"]
                attack_type = random.choice(attacks)
                print(f"\nThe goblin {attack_type} you!")
                time.sleep(2)
                damage, kill, player_health = goblin_attack()

                if damage == False:
                    print("\nThe goblin misses!")
                    os.environ['TURN'] = str("")
                    continue

                print(f"\nThe goblin did {damage} damage! You have {player_health} HP left.")
                if kill == True:
                    print("\n GAME OVER! You died :(")
                    time.sleep(2)
                    game_over = input("Thanks for playing! Would you like to play again? (Y/n)").strip()

                    if game_over.lower() == "y" or game_over.lower() == "":
                        print()
                        os.system(f"python3 {file_path}")
                    else:
                        exit(f"Goodbye, {pname} {plname}.")
                else:
                    print("You've still got some fight in you!")
                os.environ['TURN'] = str("")
                continue

            print("\nWhat would you like to do?")
            actions = ["Attack", "Leave"]
            for i, name in enumerate(actions, 1):
                print(f"{i}. {name}")
            action_three = input("Choice: ")

            if action_three == "1":
                if weapon == "sword":
                    print("You attack with Mr. Hogg's sword!")
                    time.sleep(2)
                    damage, kill = player_attack("sword")
                    
                    if damage == False:
                        print("\nYour attack failed!")
                        os.environ['TURN'] = str(True)
                        continue

                    print(f"\nYou dealt {damage} damage!\n")
                    if kill == True:
                        print("** You killed the goblin! **")
                        goblin_alive = False
                        break
                    else:
                        not_dead = ["It's not dead yet!", "Keep attacking!"]
                        print(f"{random.choice(not_dead)}")
                    os.environ['TURN'] = str("True")
                    continue
                elif weapon == "hand":
                    print("You don't have any weapons so you attack with your fists!")
                    time.sleep(2)
                    damage, kill = player_attack("hand")

                    if damage == False:
                        print("\nYour attack failed!")
                        os.environ['TURN'] = str(True)
                        continue

                    print(f"You dealt {damage} damage!\n")
                    if kill == True:
                        print("** You killed the goblin! **")
                        goblin_alive = False
                        break
                    else:
                        print(f"It's not dead yet!")
                    os.environ['TURN'] = str(True)
                    continue
            elif action_three == "2":
                break

        if action_three == "2":
            print("\nYou turn around and run back up the path from the depot.")
            time.sleep(2)
            print("\nYou here a voice from behind...")
            time.sleep(1)
            print("\n[mr. hogg]: Coward!!")
            time.sleep(1)
            print("\nYou arrive back at your home.")
            print("\nWhat would you like to do?")
            actions = ["Return to the depot", "Go eat dinner"]
            for i, name in enumerate(actions, 1):
                print(f"{i}. {name}")
            action_four = input("Choice: ")

            if action_four == "1":
                print("\nYou run back down the path.")
                time.sleep(1)
                print("\n[mr. hogg]: Oh good, you've returned. Now please help me!")
                time.sleep(1)
                continue
            elif action_four == "2":
                time.sleep(1)
                print("You smell the delicious scent of shepard's pie and cakes coming from your door as you\nwalk inside.")
                print(f"\n[mom]: Is that you, {pname}?\n")

                dialog_three = ["Yep!", "Indeed", "No"]
                for i, name in enumerate(dialog_three, 1):
                    print(f"{i}. {name}")
                dialog_three_choice = input("Choice: ")
                dialog_three_key = int(dialog_three_choice) - 1
                print(f"[you]: {dialog_three[dialog_three_key]}")
                time.sleep(1)
                if dialog_three_choice == "3":
                    print("[mom]: Haha, now com get something to eat...")
                elif int(os.environ.get('PLAYER_HEALTH')) < 8:
                    print("[mom]: Glad you're home- but you sound a little banged up! Come get some food and get better.")
                else:
                    print("[mom]: Glad you're home. Now come get some dinner.")
                
                time.sleep(2)
                play_again = input("Thanks for playing! Would you like to play again? (Y/n)").strip()

                if play_again.lower() == "y":
                    print()
                    time.sleep(1)
                    os.system(f"python3 {file_path}")
                elif play_again.lower() == "":
                    print()
                    time.sleep(1)
                    os.system(f"python3 {file_path}")
                else:
                    exit("Thanks for playing!")
        elif not goblin_alive:
            time.sleep(2)
            print(f"[mr. hogg]: Great job, {pname}! To thank you for your service, I'd like to give you some of the\nmoney I'll make from this shipment you saved.")
            print("\n** You got 50 silver pennies! **")
            time.sleep(2)
            print("As you walk back up to the house, you can see smoke coming from the chimney.\nOnce more, you fall asleep in the hammock and await your mothers call...")
            print("\n** The End **")
            exit()

    elif action_two == "2":
        print(f"\n[mr. hogg]: Thank you for coming to help, {pname}.\nYou should take my sword to assist you in battle.")
        os.environ['INVENTORY'] = json.dumps(["Sword"])
        time.sleep(1)
        print("\n** You got a new item: Mr: Hogg's sword **\n")
        time.sleep(2)
        continue

    elif action_two == "3":
        inventory_check = check_inventory()
        if inventory_check == False:
            print("You have no items in your inventory")
            time.sleep(3)
            continue
        else:
            for i, name in enumerate(inventory_check, 1):
                print(f"{i}. {name}")
            time.sleep(3)
            continue

    elif action_two == "4":
        quest_check = get_quest()
        if quest_check == False:
            print("You have no quests at the moment")
            time.sleep(3)
            continue
        else:
            for i, name in enumerate(quest_check, 1):
                print(f"{i}. {name}")
            time.sleep(3)
            continue

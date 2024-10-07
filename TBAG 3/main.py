from room import Room
from character import Enemy, Friend
from item import Item

small_cavern = Room("Small Cavern")
small_cavern.set_description("You wake up dizzy and confused on a stone floor in a small cavern, not knowing where you are. "
"You see the floor is littered with dead rats. As you stand to your feet, you see a message carved onto the stone wall. "
"It reads 'Welcome to the SkillCity dungeon, you will need all your knowledge to escape as only the wisest can survive.' "
"The only exit is a corridor leading to a noisy sounding room.")

kitchen = Room("kitchen")
kitchen.set_description("A mouldy looking cooking area")

ballroom = Room("ballroom")
ballroom.set_description("A vast mirrored room, that was probably once spectactular but is now disheveled and covered in dust")

dining_hall = Room("Dining_hall")
dining_hall.set_description("A large room with a long table and ornate decorations")

bridge_room = Room("Bridge Room")
bridge_room.set_description("A precarious bridge over some water guarded by a troll")

final_chamber = Room("Final Chamber")
final_chamber.set_description ("The final challenge awaits here")

dead_rat = Item()
dead_rat.set_name("dead rat")
dead_rat.set_description("A small, lifeless rat. It's not very pleasant, but it might come in handy.")
small_cavern.set_item(dead_rat)

key = Item()
key.set_name("key")
key.set_description("A small rusty key that looks like it could open a door.")



dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Welcome to the dungeon. You will not leave here alive")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

giant_python = Enemy("Giant Python", "A terrifying twenty-foot long snake blocking your way")
giant_python.set_weakness("sword")
final_chamber.set_character(giant_python)

aaron = Friend("Aaron", "A handsome and intelligent, cloaked, majestic-looking magical figure.")
ballroom.set_character(aaron)

devito = Enemy("Devito", "A  down on his luck troll who guards the bridge.")
devito_dealt_with = False
bridge_room.set_character(devito)

chefbobby = Friend("Bobby The Chef", "A friendly ogre who loves cooking.")
chefbobby.set_conversation("Hello! You must be the latest student of the bootcamp. I'd love to help you, but I need to prepare tonight's dinner.")
chefbobby.set_favorite_gift("dead rat")
kitchen.set_character(chefbobby) 

ballroom.lock_room()

small_cavern.link_room(kitchen, "south")
kitchen.link_room(small_cavern, "north")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west", is_locked=True)
ballroom.link_room(dining_hall, "east")
ballroom.link_room(bridge_room, "west")
bridge_room.link_room(ballroom, "east")
bridge_room.link_room(final_chamber, "west")
final_chamber.link_room(bridge_room, "east")

inventory = []
current_room = small_cavern

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        if current_room == bridge_room and command == "west" and not devito_dealt_with:
            print("Devito is blocking your way and will not let you move past.")
        else:
            current_room = current_room.move(command, inventory)

    elif command == "talk":
        if isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Devito":
            print(f"{inhabitant.name}: Oh god, another adventurer. Look mate, I'll be blunt. I'm skint and unloved and this is my only job, so I can't let you pass. Nothing personal.")
        elif isinstance(inhabitant, Friend) and inhabitant.get_name() == "Aaron":
            inhabitant.ask_riddle(inventory)
        elif inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to.")

    elif command == "offer gift":
        if isinstance(inhabitant, Friend) and inhabitant.get_name() == "Bobby The Chef":
            gift = input("What gift would you like to offer? ").lower()
            if gift in [item.get_name().lower() for item in inventory]:
                result = inhabitant.offer_gift(gift)
                if result:
                    inventory.remove(next(item for item in inventory if item.get_name().lower() == gift))
                    inventory.append(result)
                    print("Cheese has been added to your inventory.")
            else:
                print(f"You don't have a {gift} to offer.")
        else:
            print("There is no one here to offer a gift to.")

    elif command == "hug":
        if isinstance(inhabitant, Friend):
            inhabitant.hug()
        elif isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Devito":
            result = inhabitant.hug()
            if result:
                print("You can now cross the bridge to the final room.")
                devito_dealt_with = True
        else:
            print("There is no one here to hug.")

    elif command == "take":
        if current_room.get_item() is not None:
            item = current_room.get_item()
            print(f"You have picked up the {item.get_name()}.")
            inventory.append(item)
            current_room.remove_item()
        else:
            print("There is nothing to take.")

    elif command == "fight":
        if inhabitant is not None:
            item_to_fight_with = input("What will you fight with? ").lower()
            print([item.get_name() for item in inventory])
            if item_to_fight_with in [item.get_name().lower() for item in inventory]:
                result = inhabitant.fight(item_to_fight_with)

                if result and item_to_fight_with == "sword" and isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Giant Python":
                    print("Congratulations. You have mastered The Python and have completed the SkillCity dungeon.")
                    print("You are truly the best student we have ever had and will receive an exemplary grade along with a glowing LinkedIn recommendation!")
                    print("Well done!")
                    break

                elif result and isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Dave":
                    print("Dave's lactose intolerant body melts under the cheese and as he dies, drops a small iron key.")
                    key = Item()
                    key.set_name("key")
                    key.set_description("A small iron key.")
                    inventory.append(key)
                    print("You have received a key.")

                    current_room.set_character(None)

                elif not result:
                    print("You lost the fight! Now you are dead and the game is over. Not nice, is it?")
                    break
            else:
                print(f"{inhabitant.name} crushes you, puny adventurer. You have been defeated.")
                print("The game is over!")
                break
        else:
            print("There is no one to fight here.")

    elif command == "bribe":
        if isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Devito":
            amount = int(input("How much will you bribe with? "))
            result = inhabitant.bribe(amount)
            if result:
                print("You can now cross the bridge to the final room.")
                devito_dealt_with = True
            else:
                print("Devito did not accept your bribe.")
        elif isinstance(inhabitant, Friend) and inhabitant.get_name() == "Aaron":
            print(f"{inhabitant.name}: How dare you insult my integrity by suggesting I could be bribed!")
            print(f"{inhabitant.name}: You are banished from SkillCity and will never be able to code again!")
            print(f"{inhabitant.name}: You are forced to work at Subway for the rest of your life!")
            exit("GAME OVER: Aaron has killed you for trying to bribe him.")
        else:
            print("There is no one here to bribe.")

    elif command == "steal":
        if isinstance(inhabitant, Enemy):
            result = inhabitant.steal()
            if result:
                print(f"You successfully stole from {inhabitant.name}.")
            else:
                print(f"{inhabitant.name} caught you stealing!")
        else:
            print("There's no one here to steal from.")

    elif command == "sleep":
        if isinstance(inhabitant, Enemy) and inhabitant.get_name() == "Devito":
            result = inhabitant.sleep()
            if result:
                print("You have put Devito to sleep! You can now cross the bridge to the final room.")
                devito_dealt_with = True
        elif isinstance(inhabitant, Enemy):
            result = inhabitant.sleep()
            if result:
                print(f"{inhabitant.name} is now asleep.")
            else:
                print(f"{inhabitant.name} is still awake.")
        else:
            print("There is no one here to send to sleep.")

    else:
        print("I don't understand that command. Try a better command!")

from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Welcome to the dungeon. You will not leave here alive")
dave.talk()
dave.set_weakness("banana")
print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with) 
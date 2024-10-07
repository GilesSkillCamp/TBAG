from item import Item
class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True

    def get_name(self): 
        return self.name

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = "cheese"
        self.is_asleep = False

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item.lower() == self.weakness.lower():
            print(f"You fend off {self.name} with the {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
        return False


    def bribe(self, amount):
        if amount >= 10:
            print(f"{self.name}: Yes, finally the money I need to feed my family! You can pass!")
            return True
        else:
            print(f"{self.name}: That's not enough! I can't let you pass for that little!")
            return False

    def hug(self):
        print(f"{self.name}: Awww, no one's ever hugged me like that before. Go on, you can pass!")
        return True

    def sleep(self):
        if not self.is_asleep:
            print(f"{self.name}: Yaaawn... I guess I could use a nap... *snoring*")
            self.is_asleep = True
            return True
        else:
            print(f"{self.name} is already asleep.")
            return False

    def steal(self):
        print(f"You attempt to steal from {self.name}.")
        if not self.is_asleep:
            print(f"{self.name} catches you and you're in trouble!")
            return False
        else:
            print(f"You successfully steal from {self.name} while he's asleep.")
            return True


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favorite_gift = None

    def set_favorite_gift(self, gift):
        self.favorite_gift = gift

    def hug(self):
        print(f"You give {self.name} a big hug. {self.name} smiles warmly at you.")
        print(f"{self.name}: Yeah, this is extremely awkward and uncomfortable. Please don't do that.")

    def offer_gift(self, gift):
        if gift.lower() == self.favorite_gift.lower():
            print(f"[{self.name}] says: Ahhh perfect, that's just what I need to prepare tonight's dinner for the SkillCity staff.")
            print("Tell you what, as a thanks, if old Dave is giving you trouble, use this.")
            print("The poor 'ol blight is lactose intolerant. This will sort him out for you.")
            cheese = Item()
            cheese.set_name("cheese")
            cheese.set_description("A moldy, smelly block of cheese")
            print("You have received cheese.")
            return cheese
        else:
            print(f"{self.name}: Hmm, that's not what I need right now.")
            return False

    def greet(self):
        print(f"[{self.name}] says: Hello! You must be the latest student of the bootcamp. I'd love to help you, but I need to prepare tonight's dinner.")

    def ask_riddle(self, inventory):
        print(f"{self.name}: So I see you have made it this far, but we do not allow just anyone to escape the SkillCity Dungeon!")
        print(f"{self.name}: You must prove your knowledge by answering these three difficult riddles.")
        
        print(f"{self.name}: Can you tell me, brave adventurer, what the symbols HTML stand for?")
        answer1 = input("Your answer: ").lower()
        if answer1 == "hypertext markup language":
            print(f"{self.name}: Not bad brave student, but tell me do you know what the incantation 'CSS' means?")
            
            answer2 = input("Your answer: ").lower()
            if answer2 == "cascading style sheets":
                print(f"{self.name}: Almost impressive, maybe you have been paying attention in your training after all!")
                print(f"{self.name}: Here is your final test, can you tell me what 'SQL' signifies?")
                
                answer3 = input("Your answer: ").lower()
                if answer3 == "structured query language":
                    print(f"{self.name}: Well done, you may be SkillCity's brightest student yet!")
                    print(f"{self.name}: Take this sword. You will need it to conquer the final challenge of SkillCity.")
                    
                    sword = Item()
                    sword.set_name("sword")
                    sword.set_description("A sharp, magical blade that glows with power.")
                    inventory.append(sword)
                    print("You have received a sword!")

                    print(f"{self.name}: You may now proceed to the next room.")
                else:
                    print(f"{self.name}: Bah, you failed the final test. Go revise more!")
                    print("GAME OVER.")
                    exit()
            else:
                print(f"{self.name}: Bah, you failed the second test. Go revise more!")
                print("GAME OVER.")
                exit() 
        else:
            print(f"{self.name}: Bah, you are not smart enough to conquer the dungeon. Go revise more!")
            print("GAME OVER.")
            exit()


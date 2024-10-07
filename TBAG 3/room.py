class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.is_locked = False

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def lock_room(self):
        self.is_locked = True

    def unlock_room(self):
        self.is_locked = False

    def link_room(self, room_to_link, direction, is_locked=False):
        self.linked_rooms[direction] = (room_to_link, is_locked)

    def get_details(self):
        print(f"You are in the {self.name}")
        print("-----------------------------")
        print(self.description)
        for direction, (room, is_locked) in self.linked_rooms.items():
            lock_status = " (locked)" if is_locked else ""
            print(f"The {room.get_name()} is {direction}{lock_status}")
        if self.item:
            print(f"There is an item here: {self.item.get_name()}")

    def move(self, direction, inventory):
        if direction in self.linked_rooms:
            next_room, is_locked = self.linked_rooms[direction]
            if is_locked:
                key_found = any(item.get_name() == "key" for item in inventory)
                if key_found:
                    print("You use the key to unlock the door.")
                    self.unlock_room()
                else:
                    print("The door is locked. You need a key to open it.")
                    return self
            return next_room
        else:
            print("You can't go that way!")
            return self

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def remove_item(self):
        self.item = None
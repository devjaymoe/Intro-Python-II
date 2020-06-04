# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.inventory = []
    
    def move(self, direction):
        if direction == 'n':
            if self.room.n_to is not None:
                self.room = self.room.n_to
            else:
                return print('This way does not lead anywhere...')
        elif direction == 's':
            if self.room.s_to is not None:
                self.room = self.room.s_to
            else:
                return print('This way does not lead anywhere...')
        elif direction == 'e':
            if self.room.e_to is not None:
                self.room = self.room.e_to
            else:
                return print('This way does not lead anywhere...')
        elif direction == 'w':
            if self.room.w_to is not None:
                self.room = self.room.w_to
            else:
                return print('This way does not lead anywhere...')

    def check_room(self):
        if len(self.room.room_items) >= 1:
            for x in self.room.room_items:
                print(x)
        else:
            print('No items in this room')

    def pickup_item(self, item):
        self.inventory = self.inventory.append(item)

    def check_inventory(self):
        for x in self.inventory:
            print(x)
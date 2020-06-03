# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
    
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
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room

    def here(self):
        return f'I am in the {self.room} room'
    
    def move(self, direction):
        